#!/usr/bin/env python3
"""Build toàn bộ CV: HTML (build/out/) -> PDF (cv/).

Nguồn dữ liệu:  content/profile.py  +  content/cvs/*.py
Mẫu trình bày:  templates/ats.html (1 cột)  và  templates/visual.html (2 cột)

Chạy:  ./build.sh   (hoặc: python3 build.py; đặt CHROME=... nếu Chrome khác chromium)
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from content import profile                       # noqa: E402
from content.cvs import CVS                       # noqa: E402

CHROME = os.environ.get("CHROME", "chromium")
AVATAR = ROOT / "assets" / "avatar.png"
HTML_OUT = ROOT / "build" / "out"
PDF_OUT = ROOT / "cv"
STYLE_NAME = {"ats": "ATS", "visual": "Visual"}
TEMPLATES = {
    "ats": (ROOT / "templates" / "ats.html").read_text(encoding="utf-8"),
    "visual": (ROOT / "templates" / "visual.html").read_text(encoding="utf-8"),
}


# ------------------------------------------------------------ render bits ---
def render_skills(items, style):
    if style == "ats":
        return "\n".join(f"    <p><b>{k}</b> {v}</p>" for k, v in items)
    return "\n".join(
        f'        <div class="skill-row"><div class="skill-category">{k}</div>'
        f'<div class="skill-details">{v}</div></div>'
        for k, v in items
    )


def render_bullets(items):
    return "\n".join(f"      <li>{b}</li>" for b in items)


def render_projects(projects, style):
    blocks = []
    for name, tech, bullets in projects:
        if style == "ats":
            bl = "\n".join(f"      <li>{b}</li>" for b in bullets)
            blocks.append(
                f'  <div class="proj">\n    <p class="name">{name}</p>\n'
                f'    <p class="tech">{tech}</p>\n    <ul>\n{bl}\n    </ul>\n  </div>'
            )
        else:
            bl = "\n".join(f"        <li>{b}</li>" for b in bullets)
            blocks.append(
                f'      <div class="project-block">\n        <div class="project-title">{name}</div>\n'
                f'        <div class="project-tech">{tech}</div>\n'
                f'        <ul class="bullet-list">\n{bl}\n        </ul>\n      </div>'
            )
    return "\n".join(blocks)


def render_contacts(lang):
    return "\n".join(
        f"        <li>{profile.icon(kind)}<span>{text}</span></li>"
        for kind, text in profile.CONTACT_ITEMS[lang]
    )


def render_languages(lang):
    return "\n".join(
        f"        <li><strong>{label}:</strong> {level}</li>"
        for label, level in profile.LANGUAGES[lang]["items"]
    )


def render_soft_skills(cv, lang):
    items = cv.get(f"soft_skills_{lang}")
    if not items:
        return ""
    lis = "\n".join(f"        <li>• {i}</li>" for i in items)
    return (
        f'    <div class="sidebar-section">\n'
        f'      <h2>{profile.LABELS[lang]["soft_skills"]}</h2>\n'
        f'      <ul class="soft-list">\n{lis}\n      </ul>\n'
        f'    </div>'
    )


# ------------------------------------------------------------------ build ---
def build_html(cv, lang, style):
    labels = profile.LABELS[lang]
    title = cv[f"title_{lang}"]
    if style == "ats":
        mapping = {
            "{{HTML_LANG}}": lang,
            "{{DOC_TITLE}}": f'{profile.NAME[lang]} — {title} — CV',
            "{{NAME}}": profile.NAME[lang],
            "{{TITLE}}": title,
            "{{CONTACT}}": profile.CONTACT_LINE[lang],
            "{{L_SUMMARY}}": labels["summary"],
            "{{SUMMARY}}": cv[f"summary_{lang}"],
            "{{L_SKILLS}}": labels["skills_ats"],
            "{{SKILLS}}": render_skills(cv[f"skills_{lang}"], "ats"),
            "{{L_EXPERIENCE}}": labels["experience"],
            "{{JOB_TITLE}}": profile.JOB[lang]["title"],
            "{{JOB_ORG}}": profile.JOB[lang]["org"],
            "{{JOB_META}}": profile.JOB[lang]["meta"],
            "{{BULLETS}}": render_bullets(cv[f"exp_{lang}"]),
            "{{L_PROJECTS}}": labels["projects"],
            "{{PROJECTS}}": render_projects(cv[f"projects_{lang}"], "ats"),
            "{{L_EDU_LANG}}": labels["education_languages"],
            "{{EDUCATION_LINE}}": (
                f'{profile.EDUCATION[lang]["ats"]} &nbsp;·&nbsp; {profile.LANGUAGES[lang]["ats"]}'
            ),
        }
    else:
        mapping = {
            "{{HTML_LANG}}": lang,
            "{{DOC_TITLE}}": f'{profile.NAME[lang]} — {title} — CV',
            "{{NAME}}": profile.NAME[lang],
            "{{BADGE}}": cv[f"badge_{lang}"],
            "{{L_CONTACT}}": labels["contact"],
            "{{CONTACTS}}": render_contacts(lang),
            "{{L_SUMMARY}}": labels["summary"],
            "{{SUMMARY}}": cv[f"summary_{lang}"],
            "{{L_EDUCATION}}": labels["education"],
            "{{EDU_STRONG}}": profile.EDUCATION[lang]["strong"],
            "{{EDU_LINE}}": profile.EDUCATION[lang]["line"],
            "{{EDU_YEARS}}": profile.EDUCATION[lang]["years"],
            "{{L_LANGUAGES}}": labels["languages"],
            "{{LANGUAGES}}": render_languages(lang),
            "{{SOFT_SKILLS_SECTION}}": render_soft_skills(cv, lang),
            "{{L_EXPERIENCE}}": labels["experience"],
            "{{JOB_TITLE}}": profile.JOB[lang]["title"],
            "{{JOB_ORG}}": profile.JOB[lang]["org"],
            "{{JOB_META}}": profile.JOB[lang]["meta"],
            "{{BULLETS}}": render_bullets(cv[f"exp_{lang}"]),
            "{{L_PROJECTS}}": labels["projects"],
            "{{PROJECTS}}": render_projects(cv[f"projects_{lang}"], "visual"),
            "{{L_SKILLS}}": labels["skills"],
            "{{SKILLS}}": render_skills(cv[f"skills_{lang}"], "visual"),
        }
    html = TEMPLATES[style]
    for key, value in mapping.items():
        html = html.replace(key, value)
    return html


def build_pdf(html_path: Path, pdf_path: Path) -> str:
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        info = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True).stdout
        for line in info.splitlines():
            if line.startswith("Pages:"):
                return line.split(":")[1].strip()
    except FileNotFoundError:
        pass
    return "?"


def main() -> int:
    failures = []
    for cv in CVS:
        html_dir = HTML_OUT / cv["id"]
        pdf_dir = PDF_OUT / cv["id"]
        html_dir.mkdir(parents=True, exist_ok=True)
        pdf_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(AVATAR, html_dir / "avatar.png")

        for lang, style in cv["outputs"]:
            base = f'CV_VuHuuDo_{cv["file"]}_{lang.upper()}_{STYLE_NAME[style]}'
            html_path = html_dir / f"{base}.html"
            pdf_path = pdf_dir / f"{base}.pdf"
            html_path.write_text(build_html(cv, lang, style), encoding="utf-8")
            pages = build_pdf(html_path, pdf_path)
            ok = pages == "1"
            if not ok:
                failures.append(base)
            print(f'  {cv["id"]:<18} {lang.upper()} {style:<6} ->  cv/{cv["id"]}/{base}.pdf'
                  f'  [{"OK" if ok else f"⚠ {pages} trang"}]')

    print()
    if failures:
        print("THẤT BẠI: các bản sau không vừa 1 trang:", ", ".join(failures))
        return 1
    print(f"Hoàn tất: {sum(len(c['outputs']) for c in CVS)} PDF trong cv/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
