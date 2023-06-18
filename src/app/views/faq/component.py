from reactpy import component, html
from reactpy_router import link


@component
def FaqComponent():
    return html.div(
        html.h1("Home Page 🏠"),
        link("Messages", to="/"),
    )
