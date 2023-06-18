import uuid
from reactpy import component, html
from typing import Optional, Any
from reactpy_router import link
from src.app.types.style import IStyle
from src.app.components.icon.component import IconComponent
from src.app.components.column.component import ColumnComponent
from src.app.components.button.style import (
    default_styles,
    primary_styles,
    secondary_styles,
    success_styles,
    danger_styles,
    warning_styles,
    info_styles,
    light_styles,
    dark_styles,
    link_styles,
)


@component
def ButtonComponent(
    type: str,
    content: str,
    iconText: str = "",
    iconPosition: str = "left",
    linkTo: str = "",
    id: str = "",
    customStyle: Optional[IStyle] = None,
):
    """
    Componente Button.

    Args:
        type: str (primary, secondary, success, danger, warning, info, light, dark, link, outlined)
        text: str.
        icon: opcional. Ícono a mostrar en el botón.
        iconPosition: str (opcional, por defecto es "left"). Posición del ícono ("left" o "right").
        linkTo: str (opcional, por defecto es una cadena vacía).
        id: str (opcional, por defecto es una cadena vacía).
        customStyle: dict (opcional, por defecto es None).

    Returns:
        Retorna un componente Button.

    """
    styles = default_styles.copy()
    variant = type.split("-")[0]
    outlined = type.split("-")[1] if len(type.split("-")) > 1 else None

    styles.update(get_style(variant))

    if outlined is not None:
        styles.update(get_outlined_style(styles))

    if customStyle is not None:
        styles.update(customStyle)

    # Cambiar los estilos cuando el mouse pasa por encima del botón
    def handle_mouse_over(event):
        updated_styles = get_hover_style(styles)
        styles.update(updated_styles)

    # Restaurar los estilos cuando el mouse sale del botón
    def handle_mouse_out(event):
        restored_styles = get_restore_style(styles)
        styles.update(restored_styles)

    id = id if id != "" else str(uuid.uuid4())

    button_content = [content]

    if iconText != "":
        if iconPosition == "left":
            button_content.insert(0, IconComponent(iconText))
        else:
            button_content.append(IconComponent(iconText))

    button = html.button(
        {
            "id": id,
            "style": styles,
            "on_mouseover": handle_mouse_over,
            "on_mouseout": handle_mouse_out,
        },
        button_content,
    )

    if linkTo != "":
        return link(button, to=linkTo)

    return button


def get_style(variant: str) -> dict:
    styles_map = {
        "primary": primary_styles,
        "secondary": secondary_styles,
        "success": success_styles,
        "danger": danger_styles,
        "warning": warning_styles,
        "info": info_styles,
        "light": light_styles,
        "dark": dark_styles,
        "link": link_styles,
    }
    return styles_map.get(variant, default_styles)


def get_outlined_style(styles: dict) -> dict:
    return {
        "border": "1px solid",
        "color": styles["background-color"],
        "background-color": "transparent",
        "border-color": styles["background-color"],
        "border-style": "solid",
        "border-width": "1px",
    }


def get_hover_style(styles: dict) -> dict:
    return {
        "background-color": styles["color"],
        "color": styles["background-color"],
    }


def get_restore_style(styles: str) -> dict:
    return {
        "background-color": styles["color"],
        "color": styles["background-color"],
    }
