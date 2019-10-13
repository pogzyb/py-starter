# src/app/handler.py
from aiohttp.web import Response, Request
from dataclasses import dataclass
from typing import Tuple, Dict
import aiohttp_jinja2
import asyncio


@dataclass
class ApiResponse:
    alert: Tuple[str, str]
    data: Dict[str, str]
    page: str


class AppHandler(object):

    def __init__(self):
        self._loop = asyncio.get_event_loop()

    @aiohttp_jinja2.template('index.html')
    async def index(self, request: Request) -> Dict[str, str]:
        return {}
