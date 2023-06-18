import uuid
from reactpy import component, html
from typing import Optional, Any
from src.app.types.style import IStyle
from src.app.components.row.style import (
    default_styles,
)


@component
def RowComponent(
    content: Any,
    id: str = "",
    customStyle: Optional[IStyle] = None,
):
    """
    Componente Row.

    Args:
        content: contenido.
        id: str (opcional, por defecto es una cadena vacía).
        customStyle: dict (opcional, por defecto es None).

    Returns:
        Retorna un componente Row.

    """
    styles = default_styles.copy()

    if customStyle is not None:
        styles.update(customStyle)

    id = id if id != "" else str(uuid.uuid4())
    row = html.div(
        {
            "id": id,
            "style": styles,
        },
        content,
    )
    return row
