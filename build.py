import os
import shutil
from pathlib import Path
from markdown_it import MarkdownIt

ROOT_DIR = Path(__file__).parent
CONTENT_DIR = ROOT_DIR / "content"
TEMPLATE_DIR = ROOT_DIR / "templates"
STATIC_DIR = ROOT_DIR / "static"
OUTPUT_DIR = ROOT_DIR / "output"

POSTS_DIRNAME = Path("posts")

md = MarkdownIt("commonmark").enable('table')

def load_template(name: str) -> str:
    template_path = TEMPLATE_DIR / name
    if not template_path.exists():
        template_path = TEMPLATE_DIR / "base.html"
    return template_path.read_text(encoding="utf-8")

def insert_template(input_html: str, insertion: str, name: str) -> str:
    return input_html.replace(f"{{{{ {name} }}}}", insertion)

def insert_placeholders(template: str, replacements: dict[str, str]) -> str:
    result = template
    for placeholder, value in replacements.items():
        result = insert_template(result, value, placeholder)
    return result

def build_nav(links: dict[str, str]) -> str:
    return "\n".join(
        f'<a href="{href}">{label}</a>'
        for label, href in links.items()
    )

def build_post_entries(links, titles) -> str:
    post = []
    for href, title in zip(links, titles):
        post.append(f'<a class="blog-post-card" href="{href}">{title}</a>')
    return "\n".join(post)

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
        content_html = md.render(md_file.read_text(encoding="utf-8"))

        # load html template
        template_name = md_file.stem + ".html"
        template = load_template(template_name)

        # pre-process themplate to insert archetypes
        _templates = TEMPLATE_DIR.rglob("_*.html")
        replacements: dict[str, str] = {}
        for _tem in _templates:
            _tem_html = _tem.read_text(encoding="utf-8")
            _tem_tag = _tem.name.removeprefix("_").removesuffix(".html")
            replacements[_tem_tag] = _tem_html
        template = insert_placeholders(template, replacements)

        # determine which pages are in the nav
        nav_links = {
            "Home": f"/{OUTPUT_DIR.stem}/index.html",
            "Blog": f"/{OUTPUT_DIR.stem}/blog.html",
            "Resume": f"/{OUTPUT_DIR.stem}/resume.html",
        }

        post_links = []
        for post in (CONTENT_DIR / POSTS_DIRNAME).rglob("*.md"):
            post_link = (POSTS_DIRNAME / post.stem).with_suffix(".html")
            post_links.append("/output/" + post_link.as_posix())
        
        post_titles = []

        for post in (CONTENT_DIR / POSTS_DIRNAME).rglob("*.md"):
            title = None
            with post.open(encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break
            post_titles.append(title)

        replacements = {
            "content": content_html,
            "title": md_file.stem,
            "nav": build_nav(nav_links),
            "posts": build_post_entries(post_links, post_titles),
        }

        # decide on final html
        final_html = insert_placeholders(template, replacements)

        # write out final html
        out_path.write_text(final_html, encoding="utf-8")

if __name__ == "__main__":
    build()