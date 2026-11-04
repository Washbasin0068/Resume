#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = ["textual>=0.80"]
# ///
"""TUI tạo CV theo role (và JD nếu có). Mỗi lần ra 2 loại CV, 1 trang A4:
  - Human: 2 cột, đẹp, nộp cho người đọc.
  - ATS  : 1 cột, chữ thuần, nộp cho máy đọc.
Nội dung lấy từ profile.json (ngân hàng nội dung), chọn & xếp theo độ khớp với role/JD.
Không bịa kỹ năng: thứ JD đòi mà profile không có chỉ được báo là "thiếu".

  uv run cvtui.py                         # mở TUI
  uv run cvtui.py --role "DevOps" [--jd jd.txt] [--lang EN,VI]   # không TUI
  uv run cvtui.py --check                 # tự kiểm tra logic chọn nội dung
"""
import argparse
import html
import json
import os
import re
import shutil
import sys

import build_cvs as B

ROOT = B.ROOT
OUT = os.path.join(ROOT, "out")
PROFILE = json.load(open(os.path.join(ROOT, "profile.json"), encoding="utf-8"))
LIMITS = dict(exp=7, proj=3, group_items=8, groups=7)


def has(text, word):
    return re.search(r"(?<![\w])" + re.escape(word) + r"(?![\w])", text) is not None


def analyze(role, jd=""):
    """Trả về điểm tag + danh sách khớp/thiếu."""
    role_l, jd_l = role.lower(), jd.lower()
    both = role_l + "\n" + jd_l
    tags = {}
    for tag, words in PROFILE["aliases"].items():
        n = sum(3 * has(role_l, w) + min(2, jd_l.count(w)) * has(jd_l, w) for w in words)
        if n:
            tags[tag] = n
    if not tags:
        tags = {"fullstack": 3}
    matched, known = [], set()
    for g in PROFILE["skills"]:
        for it in g["items"]:
            ms = it.get("m", [it["n"].lower()])
            known.update(ms)
            if any(has(both, m) for m in ms):
                matched.append(it["n"])
    gaps = [w for w in PROFILE["watchlist"] if has(both, w) and w not in known]
    return dict(tags=tags, matched=matched, gaps=gaps, text=both)


def score(item, a):
    s = item.get("w", 0) + sum(a["tags"].get(t, 0) for t in item.get("t", []))
    ms = item.get("m", [item.get("n", "")]) if isinstance(item.get("n"), str) else []
    return s + (8 if any(m and has(a["text"], m) for m in ms) else 0)


def pick(role, jd=""):
    """Chọn nội dung (còn thừa để cắt dần cho vừa 1 trang). Mỗi list: (điểm, dữ liệu)."""
    a = analyze(role, jd)
    top = lambda lst, n: sorted(lst, key=lambda x: -x[0])[:n]
    exp = top([(score(e, a), e) for e in PROFILE["experience"]], LIMITS["exp"])
    proj = top([(score(p, a), p) for p in PROFILE["projects"]], LIMITS["proj"])
    groups = []
    for g in PROFILE["skills"]:
        its = top([(score(i, a), i) for i in g["items"]], LIMITS["group_items"])
        its = [x for x in its if x[0] > 0 or len(its) <= 3]
        if its:
            groups.append([sum(s for s, _ in its), g, its])
    groups = sorted(groups, key=lambda x: -x[0])[: LIMITS["groups"]]
    return a, exp, proj, groups


def make_role(title, a, exp, proj, groups):
    """Dựng dict role cho build_cvs.build_html từ phần đã chọn."""
    t = html.escape(title.strip())
    yrs = PROFILE["years"]
    out = {"id": "custom", "file": "Custom", "title_en": t, "title_vi": t, "badge_en": t.upper(), "badge_vi": t.upper()}
    flat = [i["n"] for _, g, its in groups for _, i in its]
    flat = sorted(flat, key=lambda n: -max([score(i, a) for g in PROFILE["skills"] for i in g["items"] if i["n"] == n] or [0]))
    top5 = ", ".join(flat[:5])
    out["summary_en"] = (
        f"{t} with {yrs['en']} years of experience building and operating enterprise web platforms. "
        f"Hands-on with {top5}. Delivered reporting, authentication and data platforms to production. "
        "AI graduate; automates workflows with Python."
    )
    out["summary_vi"] = (
        f"{t} với {yrs['vi']} năm kinh nghiệm xây dựng và vận hành nền tảng web doanh nghiệp. "
        f"Thực chiến với {top5}. Đã đưa nền tảng báo cáo, xác thực và dữ liệu lên production. "
        "Tốt nghiệp AI; tự động hóa quy trình bằng Python."
    )
    for k in ("en", "vi"):
        out["exp_" + k] = [e[k] for _, e in exp]
        out["projects_" + k] = [(p["n"][k], p["tech"], [p[k]]) for _, p in proj]
        out["skills_" + k] = [(g["g"][k] + ":", ", ".join(i["n"] for _, i in its)) for _, g, its in groups]
    return out


def trim(exp, proj, groups):
    """Bỏ phần điểm thấp nhất. False nếu hết gì để bỏ."""
    if len(exp) > 4:
        exp.pop()
    elif len(proj) > 2:
        proj.pop()
    elif len(exp) > 3:
        exp.pop()
    else:
        g = max((g for g in groups if len(g[2]) > 1), key=lambda g: len(g[2]), default=None)
        if not g:
            return False
        g[2].pop()
    return True


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "", s.title()) or "Role"


def generate(role, jd="", langs=("EN", "VI"), log=print, name="", title="", avatar=""):
    """Sinh {lang × (Human, ATS)} PDF 1 trang vào out/<slug>/. Trả về danh sách file.
    role: để chọn nội dung. title: chức danh hiển thị (mặc định = role). name/avatar: để trống = mặc định."""
    title = title.strip() or role
    name = name.strip()
    avatar = os.path.expanduser(avatar.strip())
    if avatar and not os.path.isfile(avatar):
        raise FileNotFoundError(f"Không thấy ảnh: {avatar}")
    a, exp, proj, groups = pick(role, jd)
    d = os.path.join(OUT, slug(role))
    os.makedirs(d, exist_ok=True)
    img = "Avatar" + (os.path.splitext(avatar)[1].lower() if avatar else ".png")
    shutil.copy(avatar or B.AVATAR, os.path.join(d, img))
    who = slug(name) if name else "VuHuuDo"
    files = []
    for lang in langs:
        for kind, tag in (("human", "Human"), ("ats", "ATS")):
            e, p, g = list(exp), list(proj), [[s, gr, list(i)] for s, gr, i in groups]
            while True:
                base = f"CV_{who}_{slug(title)}_{lang}_{tag}"
                hp, pp = os.path.join(d, base + ".html"), os.path.join(d, base + ".pdf")
                with open(hp, "w", encoding="utf-8") as f:
                    f.write(B.build_html(make_role(title, a, e, p, g), lang, kind, name or None).replace('src="Avatar.png"', f'src="{img}"'))
                pages = B.build_pdf(hp, pp)
                if pages in ("1", "?") or not trim(e, p, g):
                    break
            log(f"{'OK ' if pages == '1' else 'LỖI'} {pages} trang  {os.path.relpath(pp, ROOT)}")
            files.append(pp)
    return files


def report(role, jd=""):
    a, exp, proj, groups = pick(role, jd)
    tags = ", ".join(f"{k}({v})" for k, v in sorted(a["tags"].items(), key=lambda x: -x[1]))
    lines = [f"Hướng role : {tags}", f"Khớp       : {', '.join(a['matched']) or '-'}"]
    lines.append(f"THIẾU (JD đòi, CV chưa có — không tự thêm): {', '.join(a['gaps']) or '-'}")
    return "\n".join(lines)


def check():
    a = analyze("DevOps Engineer", "Docker, Kubernetes, CI/CD, Prometheus, AWS")
    assert a["tags"]["devops"] > a["tags"].get("frontend", 0), a["tags"]
    assert {"kubernetes", "aws"} <= set(a["gaps"]) and "Docker" in a["matched"], a
    _, exp, _, groups = pick("Frontend React developer")
    assert "React" in exp[0][1]["en"] or "UI" in exp[0][1]["en"], exp[0][1]["en"]
    assert groups[0][1]["g"]["en"] == "Frontend", groups[0][1]["g"]
    assert pick("zzz")[0]["tags"] == {"fullstack": 3}
    print("check OK")


def run_tui():
    from textual import work
    from textual.app import App, ComposeResult
    from textual.containers import Horizontal, Vertical
    from textual.widgets import Button, Checkbox, Footer, Header, Input, RichLog, Static, TextArea

    class CVApp(App):
        TITLE = "CV Generator — Vũ Hữu Đô"
        CSS = """
        #left {width: 50%; padding: 0 1;} #right {width: 50%; padding: 0 1;}
        TextArea {height: 8;} #log {height: 1fr; border: round $accent;}
        #ana {height: 10; border: round $primary; padding: 0 1;}
        """
        BINDINGS = [("ctrl+g", "gen", "Tạo CV"), ("ctrl+q", "quit", "Thoát")]

        def compose(self) -> ComposeResult:
            yield Header()
            with Horizontal():
                with Vertical(id="left"):
                    yield Static("Role muốn ứng tuyển (để chọn nội dung):")
                    yield Input(placeholder="vd: Backend .NET Developer", id="role")
                    yield Static("Chức danh hiển thị trên CV (trống = như role):")
                    yield Input(placeholder="vd: Senior Backend Engineer", id="title")
                    yield Static("Họ tên (trống = mặc định):")
                    yield Input(placeholder="Vu Huu Do / Vũ Hữu Đô", id="name")
                    yield Static("Ảnh đại diện — đường dẫn (trống = mặc định):")
                    yield Input(placeholder="~/Pictures/avatar.jpg", id="avatar")
                    yield Static("Job description (tuỳ chọn, dán vào để khớp từ khóa tốt hơn):")
                    yield TextArea(id="jd")
                    with Horizontal():
                        yield Checkbox("Tiếng Anh (EN)", True, id="en")
                        yield Checkbox("Tiếng Việt (VI)", True, id="vi")
                    yield Button("Tạo 2 loại CV  (Ctrl+G)", variant="success", id="go")
                with Vertical(id="right"):
                    yield Static("Phân tích:")
                    yield Static("Nhập role để xem phân tích.", id="ana")
                    yield Static("Kết quả:")
                    yield RichLog(id="log", wrap=True, markup=False)
            yield Footer()

        def vals(self):
            return self.query_one("#role", Input).value.strip(), self.query_one("#jd", TextArea).text

        def opts(self):
            q = lambda i: self.query_one(i, Input).value.strip()
            return dict(title=q("#title"), name=q("#name"), avatar=q("#avatar"))

        def refresh_ana(self):
            r, j = self.vals()
            self.query_one("#ana", Static).update(report(r, j) if r else "Nhập role để xem phân tích.")

        def on_input_changed(self, e):
            self.refresh_ana()

        def on_text_area_changed(self, e):
            self.refresh_ana()

        def on_button_pressed(self, e):
            self.action_gen()

        def action_gen(self):
            r, j = self.vals()
            langs = [l for l, i in (("EN", "#en"), ("VI", "#vi")) if self.query_one(i, Checkbox).value]
            log = self.query_one("#log", RichLog)
            if not r or not langs:
                log.write("Cần nhập role và chọn ít nhất 1 ngôn ngữ.")
                return
            log.write(f"Đang tạo CV cho: {r} ...")
            self.render_job(r, j, langs, self.opts())

        @work(thread=True, exclusive=True)
        def render_job(self, r, j, langs, o):
            log = self.query_one("#log", RichLog)
            w = lambda m: self.call_from_thread(log.write, m)
            try:
                generate(r, j, langs, w, **o)
                w(f"Xong. Human = nộp người đọc, ATS = nộp máy đọc. Thư mục: out/{slug(r)}/")
            except Exception as ex:  # noqa: BLE001
                w(f"Lỗi: {ex}")

    CVApp().run()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--role")
    ap.add_argument("--jd", help="file chứa job description")
    ap.add_argument("--lang", default="EN,VI")
    ap.add_argument("--title", default="", help="chức danh hiển thị (mặc định = role)")
    ap.add_argument("--name", default="", help="họ tên (mặc định theo từng ngôn ngữ)")
    ap.add_argument("--avatar", default="", help="đường dẫn ảnh đại diện")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        check()
    elif a.role:
        jd = open(a.jd, encoding="utf-8").read() if a.jd else ""
        print(report(a.role, jd))
        generate(a.role, jd, a.lang.upper().split(","), name=a.name, title=a.title, avatar=a.avatar)
    else:
        run_tui()
