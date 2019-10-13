# src/app/__init__.py
from aiohttp.web import Application
from app.handler import AppHandler
from app.routes import init_routes
import aiohttp_jinja2
import jinja2
import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))
logger = logging.basicConfig()


def init_jinja2(app: Application) -> None:
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(os.path.join(basedir, 'app/templates'))
    )


async def create_app() -> Application:
    app = Application()
    handler = AppHandler()
    init_routes(app, handler)
    init_jinja2(app)
    return app
