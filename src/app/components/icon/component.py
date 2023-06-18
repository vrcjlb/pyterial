from reactpy import component, html


@component
def IconComponent(
    icon: str,
    size: int = 24,
    color: str = "inherit",
    font: str = "material",
    customStyle: dict = None,
):
    """
    Componente Icon.

    Args:
        icon: str. Nombre del ícono.
        size: int (opcional, por defecto es 24). Tamaño del ícono en píxeles.
        color: str (opcional, por defecto es "inherit"). Color del ícono.
        font: str (opcional, por defecto es "material"). Fuente del ícono ("material" o "font-awesome").
        customStyle: dict (opcional, por defecto es None). Estilos personalizados para el ícono.

    Returns:
        Retorna un componente Icon.

    """
    if font == "font-awesome":
        return html.span(
            {"style": customStyle},
            html.i(
                {
                    "class": f"fa {icon}",
                    "style": {"fontSize": f"{size}px", "color": color},
                }
            ),
        )

    styles = (
        {
            "display": "inline-flex",
            "align-items": "center",
            "justify-content": "center",
            "width": f"{size}px",
            "height": f"{size}px",
            "color": color,
            **customStyle,
        }
        if customStyle
        else {
            "display": "inline-flex",
            "align-items": "center",
            "justify-content": "center",
            "width": f"{size}px",
            "height": f"{size}px",
            "color": color,
        }
    )

    return html.i({"class": "material-icons", "style": styles}, icon)
