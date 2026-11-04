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
import unicodedata
from urllib.parse import quote

import build_cvs as B

ROOT = B.ROOT
OUT = os.path.join(ROOT, "out")
PROFILES = os.path.join(ROOT, "profiles")
TAX = json.load(open(os.path.join(ROOT, "taxonomy.json"), encoding="utf-8"))
LIMITS = dict(exp=7, proj=3, group_items=8, groups=7)
REQUIRED = ("name", "job", "education", "languages", "summary", "experience", "projects", "skills")
P = None  # hồ sơ đang dùng; đặt bởi use_profile()


def list_profiles():
    return sorted(d for d in os.listdir(PROFILES)
                  if d != "_template" and os.path.isfile(os.path.join(PROFILES, d, "profile.json")))


def use_profile(ref):
    """ref = id trong profiles/ hoặc đường dẫn thư mục/file profile.json."""
    global P
    path = ref if os.path.exists(ref) else os.path.join(PROFILES, ref)
    path = os.path.join(path, "profile.json") if os.path.isdir(path) else path
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Không thấy hồ sơ '{ref}'. Có: {', '.join(list_profiles()) or '(chưa có)'}")
    P = json.load(open(path, encoding="utf-8"))
    P["_dir"], P["_id"] = os.path.dirname(os.path.abspath(path)), os.path.basename(os.path.dirname(os.path.abspath(path)))
    miss = [k for k in REQUIRED if k not in P]
    if miss:
        raise ValueError(f"Hồ sơ thiếu mục: {', '.join(miss)} (xem profiles/_template/profile.json)")
    return P


def new_profile(pid):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", pid) or pid == "_template":
        raise ValueError("id chỉ gồm chữ, số, - và _")
    dst = os.path.join(PROFILES, pid)
    if os.path.exists(dst):
        raise FileExistsError(f"Đã có profiles/{pid}")
    shutil.copytree(os.path.join(PROFILES, "_template"), dst)
    return os.path.join(dst, "profile.json")


def tx(v, lang):
    """Giá trị chuỗi hoặc {en,vi} -> chuỗi (thiếu ngôn ngữ thì lấy en)."""
    if isinstance(v, dict) and ("en" in v or "vi" in v):
        return v.get(lang, v.get("en", ""))
    return v


def esc(text):
    """Văn bản thuần -> HTML an toàn; **x** -> <b>x</b>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(str(text), quote=False))


def ctx_for(lang, name_override=""):
    k = lang.lower()
    t = lambda v: esc(tx(v, k))
    ed = tx(P["education"], k)
    edu = f"<b>{esc(ed['degree'])}</b> — {esc(ed['school'])} ({esc(ed['period'])})"
    langs = tx(P["languages"], k)
    job, link = P["job"], lambda u: u if u.startswith("http") else "https://" + u
    contacts = [("pin", t(P.get("location", "")))]
    if P.get("phone"):
        contacts.append(("phone", esc(P["phone"])))
    if P.get("email"):
        contacts.append(("mail", f'<a href="mailto:{esc(P["email"])}">{esc(P["email"])}</a>'))
    for key, kind in (("github", "github"), ("linkedin", "linkedin")):
        if P.get(key):
            contacts.append((kind, f'<a href="{esc(link(quote(P[key], safe=":/%")))}">{esc(P[key])}</a>'))
    contacts = [c for c in contacts if c[1]]
    return dict(
        name=esc(name_override or tx(P["name"], k)), avatar="Avatar.png", education=edu,
        contacts=contacts, contact_line=" &bull; ".join(re.sub(r"<[^>]+>", "", c[1]) for c in contacts),
        job=f"{t(job['title'])} — {t(job['company'])}", job_meta=t(job["meta"]),
        job_title=t(job["title"]), company=t(job["company"]).upper(),
        languages=" · ".join(f"{esc(a)} ({esc(b).lower()})" for a, b in langs),
        langs_li="".join(f"<li><strong>{esc(a)}:</strong> {esc(b)}</li>" for a, b in langs),
    )


def has(text, word):
    return re.search(r"(?<![\w])" + re.escape(word) + r"(?![\w])", text) is not None


def analyze(role, jd=""):
    """Trả về điểm tag + danh sách khớp/thiếu."""
    role_l, jd_l = role.lower(), jd.lower()
    both = role_l + "\n" + jd_l
    tags = {}
    for tag, words in TAX["aliases"].items():
        n = sum(3 * has(role_l, w) + min(2, jd_l.count(w)) * has(jd_l, w) for w in words)
        if n:
            tags[tag] = n
    if not tags:
        tags = {"fullstack": 3}
    matched, known = [], set()
    for g in P["skills"]:
        for it in g["items"]:
            ms = it.get("m", [it["n"].lower()])
            known.update(ms)
            if any(has(both, m) for m in ms):
                matched.append(it["n"])
    gaps = [w for w in TAX["watchlist"] if has(both, w) and w not in known]
    return dict(tags=tags, matched=matched, gaps=gaps, text=both)


def score(item, a):
    s = item.get("w", 0) + sum(a["tags"].get(t, 0) for t in item.get("t", []))
    ms = item.get("m", [item.get("n", "")]) if isinstance(item.get("n"), str) else []
    return s + (8 if any(m and has(a["text"], m) for m in ms) else 0)


def pick(role, jd=""):
    """Chọn nội dung (còn thừa để cắt dần cho vừa 1 trang). Mỗi list: (điểm, dữ liệu)."""
    a = analyze(role, jd)
    top = lambda lst, n: sorted(lst, key=lambda x: -x[0])[:n]
    exp = top([(score(e, a), e) for e in P["experience"]], LIMITS["exp"])
    proj = top([(score(p, a), p) for p in P["projects"]], LIMITS["proj"])
    groups = []
    for g in P["skills"]:
        its = top([(score(i, a), i) for i in g["items"]], LIMITS["group_items"])
        its = [x for x in its if x[0] > 0 or len(its) <= 3]
        if its:
            groups.append([sum(s for s, _ in its), g, its])
    groups = sorted(groups, key=lambda x: -x[0])[: LIMITS["groups"]]
    return a, exp, proj, groups


def make_role(title, a, exp, proj, groups):
    """Dựng dict role cho build_cvs.build_html từ phần đã chọn (đã escape HTML)."""
    t = esc(title.strip())
    out = {"id": "custom", "file": "Custom", "title_en": t, "title_vi": t, "badge_en": t.upper(), "badge_vi": t.upper()}
    best = lambda n: max([score(i, a) for g in P["skills"] for i in g["items"] if i["n"] == n] or [0])
    flat = sorted((i["n"] for _, g, its in groups for _, i in its), key=lambda n: -best(n))
    for k in ("en", "vi"):
        out["summary_" + k] = esc(tx(P["summary"], k).format(
            title=title.strip(), years=tx(P.get("years", ""), k), skills=", ".join(flat[:5])))
        out["exp_" + k] = [esc(tx(e, k)) for _, e in exp]
        out["projects_" + k] = [(esc(tx(p["n"], k)), esc(p.get("tech", "")), [esc(tx(p, k))]) for _, p in proj]
        out["skills_" + k] = [(esc(tx(g["g"], k)) + ":", esc(", ".join(i["n"] for _, i in its))) for _, g, its in groups]
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
    s = unicodedata.normalize("NFKD", s.replace("đ", "d").replace("Đ", "D")).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "", s.title()) or "Role"


def denylist():
    """Từ cấm riêng của hồ sơ (profiles/<id>/denylist.txt, mỗi dòng 1 từ, # = chú thích). Không commit."""
    f = os.path.join(P["_dir"], "denylist.txt")
    if not os.path.isfile(f):
        return []
    return [w.strip().lower() for w in open(f, encoding="utf-8") if w.strip() and not w.startswith("#")]


def leaks(html_text, words):
    text = html.unescape(re.sub(r"<[^>]+>", " ", html_text)).lower()
    return [w for w in words if has(text, w)]


def generate(role, jd="", langs=("EN", "VI"), log=print, name="", title="", avatar=""):
    """Sinh {lang × (Human, ATS)} PDF 1 trang vào out/<hồ-sơ>/<role>/. Trả về [(đường dẫn, ok)].
    role: để chọn nội dung. title: chức danh hiển thị (mặc định = role). name/avatar: trống = lấy từ hồ sơ."""
    title = title.strip() or role
    name = name.strip()
    avatar = os.path.expanduser(avatar.strip())
    if not avatar and P.get("avatar"):
        avatar = os.path.join(P["_dir"], os.path.expanduser(P["avatar"]))
    if avatar and not os.path.isfile(avatar):
        raise FileNotFoundError(f"Không thấy ảnh: {avatar}")
    a, exp, proj, groups = pick(role, jd)
    d = os.path.join(OUT, P["_id"], slug(role))
    os.makedirs(d, exist_ok=True)
    img = "Avatar" + (os.path.splitext(avatar)[1].lower() if avatar else ".png")
    if avatar:
        shutil.copy(avatar, os.path.join(d, img))
    files, deny = [], denylist()
    for lang in langs:
        who = slug(name or tx(P["name"], lang.lower()))
        for kind, tag in (("human", "Human"), ("ats", "ATS")):
            e, p, g = list(exp), list(proj), [[s, gr, list(i)] for s, gr, i in groups]
            while True:
                base = f"CV_{who}_{slug(title)}_{lang}_{tag}"
                hp, pp = os.path.join(d, base + ".html"), os.path.join(d, base + ".pdf")
                ctx = ctx_for(lang, name)
                ctx["avatar"] = img if avatar else ""
                doc = B.build_html(make_role(title, a, e, p, g), lang, kind, ctx=ctx)
                with open(hp, "w", encoding="utf-8") as f:
                    f.write(doc)
                pages = B.build_pdf(hp, pp)
                if pages in ("1", "?") or not trim(e, p, g):
                    break
            bad = leaks(doc, deny)
            ok = pages == "1" and not bad
            log(f"{'OK ' if ok else 'LỖI'} {pages} trang  {os.path.relpath(pp, ROOT)}"
                + (f"  RÒ RỈ từ cấm: {', '.join(bad)}" if bad else ""))
            files.append((pp, ok))
    return files


def report(role, jd=""):
    a, exp, proj, groups = pick(role, jd)
    tags = ", ".join(f"{k}({v})" for k, v in sorted(a["tags"].items(), key=lambda x: -x[1]))
    lines = [f"Hướng role : {tags}", f"Khớp       : {', '.join(a['matched']) or '-'}"]
    lines.append(f"THIẾU (JD đòi, CV chưa có — không tự thêm): {', '.join(a['gaps']) or '-'}")
    return "\n".join(lines)


def check():
    use_profile("vuhuudo")
    a = analyze("DevOps Engineer", "Docker, Kubernetes, CI/CD, Prometheus, AWS")
    assert a["tags"]["devops"] > a["tags"].get("frontend", 0), a["tags"]
    assert {"kubernetes", "aws"} <= set(a["gaps"]) and "Docker" in a["matched"], a
    _, exp, _, groups = pick("Frontend React developer")
    assert "React" in exp[0][1]["en"] or "UI" in exp[0][1]["en"], exp[0][1]["en"]
    assert groups[0][1]["g"]["en"] == "Frontend", groups[0][1]["g"]
    assert pick("zzz")[0]["tags"] == {"fullstack": 3}
    c = ctx_for("EN")
    assert c["name"] == "Vu Huu Do" and "<a " in c["contacts"][2][1], c
    assert tx({"w": 1, "en": "a", "vi": "b"}, "vi") == "b" and tx({"degree": "x"}, "en") == {"degree": "x"}
    assert slug("Vũ Hữu Đô") == "VuHuuDo" and esc("A & <b>") == "A &amp; &lt;b&gt;"
    import tempfile
    global PROFILES
    old, PROFILES = PROFILES, tempfile.mkdtemp()
    shutil.copytree(os.path.join(old, "_template"), os.path.join(PROFILES, "_template"))
    try:
        use_profile(os.path.basename(os.path.dirname(new_profile("t1"))))
        assert list_profiles() == ["t1"] and P["_id"] == "t1"
        open(os.path.join(P["_dir"], "denylist.txt"), "w").write("# x\nAcme Corp\n")
        assert denylist() == ["acme corp"] and leaks("<p>at ACME&nbsp;Corp</p>".replace("&nbsp;", " "), denylist())
        assert not any(c[0] == "linkedin" for c in ctx_for("VI")["contacts"])
        try:
            new_profile("t1"); raise SystemExit("phải báo lỗi trùng id")
        except FileExistsError:
            pass
    finally:
        PROFILES = old
    print("check OK")


def run_tui():
    from textual import work
    from textual.app import App, ComposeResult
    from textual.containers import Horizontal, Vertical
    from textual.widgets import Button, Checkbox, Footer, Header, Input, RichLog, Select, Static, TextArea

    class CVApp(App):
        TITLE = "CV Generator — Vũ Hữu Đô"
        CSS = """
        #left {width: 50%; padding: 0 1;} #right {width: 50%; padding: 0 1;}
        TextArea {height: 8;} #log {height: 1fr; border: round $accent;}
        #ana {height: 10; border: round $primary; padding: 0 1;}
        """
        BINDINGS = [("ctrl+g", "gen", "Tạo CV"), ("ctrl+q", "quit", "Thoát")]

        def compose(self) -> ComposeResult:
            ids = list_profiles()
            yield Header()
            with Horizontal():
                with Vertical(id="left"):
                    yield Static("Hồ sơ (người dùng):")
                    yield Select([(p, p) for p in list_profiles()], value=ids[0], allow_blank=False, id="profile")
                    yield Static("Role muốn ứng tuyển (để chọn nội dung):")
                    yield Input(placeholder="vd: Backend .NET Developer", id="role")
                    yield Static("Chức danh hiển thị trên CV (trống = như role):")
                    yield Input(placeholder="vd: Senior Backend Engineer", id="title")
                    yield Static("Họ tên (trống = mặc định):")
                    yield Input(placeholder="theo hồ sơ", id="name")
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

        def on_mount(self):
            use_profile(str(self.query_one("#profile", Select).value))

        def on_select_changed(self, e):
            use_profile(str(e.value))
            self.refresh_ana()

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
                w(f"Xong. Human = nộp người đọc, ATS = nộp máy đọc. Thư mục: out/{P['_id']}/{slug(r)}/")
            except Exception as ex:  # noqa: BLE001
                w(f"Lỗi: {ex}")

    CVApp().run()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", help="id hồ sơ trong profiles/ (hoặc đường dẫn profile.json)")
    ap.add_argument("--new", metavar="ID", help="tạo hồ sơ mới từ mẫu rồi thoát")
    ap.add_argument("--list", action="store_true", help="liệt kê hồ sơ")
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
    elif a.list:
        print("\n".join(list_profiles()) or "(chưa có hồ sơ)")
    elif a.new:
        print("Đã tạo", new_profile(a.new), "— sửa file này rồi chạy lại.")
    else:
        ids = list_profiles()
        if not ids and not a.profile:
            sys.exit("Chưa có hồ sơ. Tạo: uv run cvtui.py --new <id>")
        pid = a.profile or (ids[0] if len(ids) == 1 else None)
        if a.role:
            if not pid:
                sys.exit(f"Chọn hồ sơ bằng --profile ({', '.join(ids)})")
            use_profile(pid)
            jd = open(a.jd, encoding="utf-8").read() if a.jd else ""
            print(report(a.role, jd))
            res = generate(a.role, jd, a.lang.upper().split(","), name=a.name, title=a.title, avatar=a.avatar)
            sys.exit(0 if all(ok for _, ok in res) else 1)
        else:
            use_profile(pid or ids[0])
            run_tui()
