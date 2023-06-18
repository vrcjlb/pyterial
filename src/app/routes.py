from reactpy import component
from reactpy_router import route, simple

from src.app.views.home.component import HomeComponent
from src.app.views.faq.component import FaqComponent


@component
def RouteModule():
    return simple.router(
        route("/", HomeComponent()),
        route("/faq", FaqComponent()),
    )
