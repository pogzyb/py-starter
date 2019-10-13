# src/app/routes.py
from aiohttp.web import Application
from app.handler import AppHandler


def init_routes(app: Application, handler: AppHandler) -> None:
    app.router.add_route('GET', '/', handler.index, name='index')
    return
