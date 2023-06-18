import uuid
from reactpy import component, html
from typing import List, Optional, Any
from src.app.types.style import IStyle
from src.app.components.button.component import ButtonComponent


@component
def NavbarComponent(
    content: Any,
    customStyle: Optional[IStyle] = None,
):
    """
    Componente Navbar.

    Args:
        brand: str. Texto del logotipo o nombre de la marca.
        nav_content: (Components). Lista de enlaces de la barra de navegación. Cada enlace debe ser un diccionario con las claves "text" y "url".
        customStyle: dict (opcional, por defecto es None). Estilos personalizados para la barra de navegación.

    Returns:
        Retorna un componente Navbar.

    """
    navbar_styles = {
        "display": "flex",
        "justify-content": "space-between",
        "align-items": "center",
        "padding": "4px 16px",
        "height": "56px",
        "background-color": "#f8f9fa",
        "box-shadow": "0 2px 4px 0 rgba(0,0,0,0.1)",
        "box-sizing": "border-box",
    }

    if customStyle is not None:
        navbar_styles.update(customStyle)

    return html.nav(
        {"style": navbar_styles},
        content,
    )
