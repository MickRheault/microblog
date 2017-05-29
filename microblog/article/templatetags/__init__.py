from markdown import markdown

from microblog.settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
)


def markdownify(content):
    md = markdown(
        text=content,
        extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
    )
    return md