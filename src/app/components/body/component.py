from reactpy import component, html
from typing import Any


@component
def BodyComponent(
    content: Any,
    customStyle: str = None,
):
    normalizecss = "*{font-family: 'Roboto'; } body { margin: 0; font-size: 16px; } html { height: 100%; } body { min-height: 100%; }"
    if customStyle:
        normalizecss = normalizecss + customStyle.get("globalCss", "")
    resetDom = html.style(normalizecss)
    font = (
        html.head(
            html.link(
                {
                    "rel": "stylesheet",
                    "href": "https://fonts.googleapis.com/css?family=Roboto&display=swap",
                }
            ),
            html.link(
                {
                    "rel": "stylesheet",
                    "href": "https://fonts.googleapis.com/icon?family=Material+Icons",
                }
            )
        ),
    )
    return html.div(
        font,
        resetDom,
        content,
    )
