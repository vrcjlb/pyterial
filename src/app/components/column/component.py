import uuid
from reactpy import component, html
from typing import Optional, Any
from src.app.types.style import IStyle
from src.app.components.column.style import (
    one_styles,
    two_styles,
    three_styles,
    four_styles,
    five_styles,
    six_styles,
    seven_styles,
    eight_styles,
    nine_styles,
    ten_styles,
    eleven_styles,
    twelve_styles,
)


@component
def ColumnComponent(
    content: Any,
    id: str = "",
    size: int = 12,
    customStyle: Optional[IStyle] = None,
):
    """
    Componente Column.

    Args:
        content: contenido.
        id: str (opcional, por defecto es una cadena vacía).
        size: int (opcional, por defecto es 12).
        customStyle: dict (opcional, por defecto es None).

    Returns:
        Retorna un componente Column.

    """
    if size == 1:
        styles = one_styles.copy()
    elif size == 2:
        styles = two_styles.copy()
    elif size == 3:
        styles = three_styles.copy()
    elif size == 4:
        styles = four_styles.copy()
    elif size == 5:
        styles = five_styles.copy()
    elif size == 6:
        styles = six_styles.copy()
    elif size == 7:
        styles = seven_styles.copy()
    elif size == 8:
        styles = eight_styles.copy()
    elif size == 9:
        styles = nine_styles.copy()
    elif size == 10:
        styles = ten_styles.copy()
    elif size == 11:
        styles = eleven_styles.copy()
    elif size == 12:
        styles = twelve_styles.copy()
    else:
        styles = twelve_styles.copy()

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
