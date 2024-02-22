from aiogram import Dispatcher
from .user import router as user_router


def setup_routers(dispatcher: Dispatcher) -> None:
    # include routers
    dispatcher.include_routers(
        user_router,
    )


__all__ = [
    'setup_routers'
]
