import os
import shutil
from pathlib import Path
from markdown_it import MarkdownIt

ROOT_DIR = Path(__file__).parent
OUTPUT_DIR = ROOT_DIR / "output"
CONTENT_DIR = ROOT_DIR / "content"
TEMPLATE_DIR = ROOT_DIR / "templates"
STATIC_DIR = ROOT_DIR / "static"

md = MarkdownIt("commonmark").enable('table')

def load_template(name: str) -> str:
    template_path = TEMPLATE_DIR / name
    if not template_path.exists():
        template_path = TEMPLATE_DIR / "base.html"
    return template_path.read_text(encoding="utf-8")

def insert_template(input_html: str, insertion: str, name: str) -> str:
    return input_html.replace("{{ {} }}".format(name), insertion)

def copy_static(src, dst):
    if src.exists():
        shutil.copytree(src, dst)

def build():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    # copy static content
    copy_static(STATIC_DIR, OUTPUT_DIR / "static")

    # build site
    for md_file in CONTENT_DIR.rglob("*.md"):
        rel_path = md_file.relative_to(CONTENT_DIR)
        out_path = (OUTPUT_DIR / rel_path).with_suffix(".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # render md to html
        html = md.render(md_file.read_text(encoding="utf-8"))

        # load html template
        template_name = md_file.stem + ".html"
        template = load_template(template_name)

        # insert content
        content_inserted_html = insert_template(template, html, "content")

        # insert title
        title_inserted_html = insert_template(content_inserted_html, md_file.stem, "title")

        # decide on final html
        final_html = title_inserted_html

        # write out final html
        out_path.write_text(final_html, encoding="utf-8")

        # print the result
        print(f"built {out_path}")

if __name__ == "__main__":
    build()