from aiogram import Dispatcher

from .database import DatabaseMiddleware
from app.configuration import Configuration


def setup_middlewares(dispatcher: Dispatcher, config: Configuration) -> None:
    dispatcher.update.outer_middleware(DatabaseMiddleware())

__all__ = [
    'setup_middlewares'
]