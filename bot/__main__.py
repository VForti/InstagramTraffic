import asyncio
import signal

from aiogram import Bot, Dispatcher

from app.configuration import Configuration
from app.database import Base
from bot.core.middlewares import setup_middlewares
from bot.routers import setup_routers
import logging

logging.basicConfig(level=logging.INFO)


async def main():
    config = Configuration()
    # setup dispatcher and bot
    dispatcher = Dispatcher()

    setup_middlewares(dispatcher=dispatcher, config=config)

    # setup routers
    setup_routers(dispatcher=dispatcher)

    # # якщо не получається через alembic зробити міграції вот автоматичне створення бд
    # async with config.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)

    bot = Bot(config.bot_token, parse_mode="html")

    # start polling
    await dispatcher.start_polling(
        bot,
        session_pool=config.session_pool,
        config=config,
    )


if __name__ == "__main__":
    asyncio.run(main())


