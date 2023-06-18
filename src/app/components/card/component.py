import uuid
from reactpy import component, html
from typing import Optional, Any
from src.app.types.style import IStyle
from src.app.components.card.style import (
    default_styles,
    title_styles,
    body_styles,
    footer_styles,
)

@component
def CardComponent(
    title: Any | str = "",
    body: Any | str = "",
    footer: Any | str = "",
    id: str = "",
    customStyle: Optional[IStyle] = None,
):
    """
    Componente Card con estilo Material Design.

    Args:
        title: str. Título del card.
        body: str. Contenido del card.
        footer: str (opcional, por defecto es una cadena vacía). Pie de página del card.
        id: str (opcional, por defecto es una cadena vacía). ID del card.
        customStyle: dict (opcional, por defecto es None). Estilos personalizados del card.

    Returns:
        Retorna un componente Card con estilo Material Design.

    """
    styles = default_styles.copy()

    if customStyle is not None:
        styles.update(customStyle)

    id = id if id != "" else str(uuid.uuid4())

    if isinstance(body, str):
        card_title = html.h3({"style": title_styles}, title)
    else:
        card_title = html.div({"style": title_styles}, title)

    if isinstance(body, str):
        card_body = html.p({"style": body_styles}, body)
    else:
        card_body = html.div({"style": body_styles}, body)

    if isinstance(footer, str):
        card_footer = html.p({"style": footer_styles}, footer)
    else:
        card_footer = html.div({"style": footer_styles}, footer)

    return html.div({"id": id, "style": styles}, [card_title, card_body, card_footer])
