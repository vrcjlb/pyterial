from reactpy import component, html
from src.app.components.icon.component import IconComponent
from src.app.components.body.component import BodyComponent
from src.app.components.row.component import RowComponent
from src.app.components.column.component import ColumnComponent
from src.app.components.button.component import ButtonComponent
from src.app.components.card.component import CardComponent
from src.app.components.navbar.component import NavbarComponent


@component
def HomeComponent():
    brand = ButtonComponent(
        type="link",
        content="PyTerial",
        iconText="menu",
        customStyle={
            "margin": "0",
            "color": "#fff",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "gap": "5px",
        },
    )

    nav_links = [
        {"type": "primary", "content": "Components"},
    ]

    buttons = [
        {"type": "primary", "content": "primary"},
        {"type": "secondary", "content": "secondary"},
        {"type": "success", "content": "success"},
        {"type": "danger", "content": "danger"},
        {"type": "warning", "content": "warning"},
        {"type": "info", "content": "info"},
        {"type": "light", "content": "light"},
        {"type": "dark", "content": "dark"},
        {"type": "link", "content": "link", "linkTo": "/faq"},
    ]

    outlined_buttons = [
        {"type": "primary-outlined", "content": "primary"},
        {"type": "secondary-outlined", "content": "secondary"},
        {"type": "success-outlined", "content": "success"},
        {"type": "danger-outlined", "content": "danger"},
        {"type": "warning-outlined", "content": "warning"},
        {"type": "info-outlined", "content": "info"},
        {"type": "light-outlined", "content": "light"},
        {"type": "dark-outlined", "content": "dark"},
    ]

    cards = [
        {
            "title": "Card title",
            "body": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "footer": [ButtonComponent("primary", "Go somewhere")],
        }
    ] * 4

    nav_links_row = ColumnComponent(
        content=[ButtonComponent(**nav_link) for nav_link in nav_links],
        size=10,
        customStyle={"text-align": "right"},
    )

    nav_brand_row = ColumnComponent(
        content=brand,
        size=2,
        customStyle={"text-align": "left", "display": "flex", "align-items": "center"},
    )

    nav_content = RowComponent(
        content=[nav_brand_row, nav_links_row],
    )

    navbar = NavbarComponent(
        content=nav_content,
        customStyle={
            "background-color": "#e91e63",
        },
    )

    buttons_row = RowComponent(
        content=[
            ButtonComponent(**button, customStyle={"margin-top": "10px"})
            for button in buttons
        ],
        customStyle={"margin-bottom": "10px"},
    )

    outlined_buttons_row = RowComponent(
        content=[
            ButtonComponent(**button, customStyle={"margin-top": "10px"})
            for button in outlined_buttons
        ],
        customStyle={"margin-bottom": "10px"},
    )

    cards_columns = [
        ColumnComponent(
            content=[CardComponent(**card, customStyle={"margin-top": "10px"})],
            size=3,
            id="",
        )
        for card in cards
    ]

    cards_row = RowComponent(
        content=cards_columns,
        customStyle={"margin-bottom": "10px"},
    )

    return BodyComponent(
        content=(
            navbar,
            html.h2("Buttons 🎛️"),
            buttons_row,
            html.h2("Outline buttons 🎛️"),
            outlined_buttons_row,
            html.h2("Cards 🎛️"),
            cards_row,
            html.h2("Icons 🎛️"),
            RowComponent(
                content=[
                    ColumnComponent(
                        content=[
                            IconComponent(
                                icon="menu",
                                customStyle={"margin-top": "10px"},
                            )
                        ],
                    )
                ]
            ),
        ),
        customStyle={"globalCss": "body { background-color: #303030; }"},
    )
