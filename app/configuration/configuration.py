import json
import os
from typing import List

from aiogram import Bot
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv

load_dotenv()

class Configuration:
    admins: list[int] = json.loads(os.getenv("ADMIN_ID"))
    database_url: str = "{engine}://{username}:{password}@{host}/{db}".format(
            engine=os.getenv('DATABASE_ENGINE'),
            username=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            host=os.getenv('DATABASE_HOST'),
            db=os.getenv('DATABASE_NAME'),
        )
    bot_token: str = os.getenv('BOT_TOKEN')

    engine = create_async_engine(database_url)
    session_pool = async_sessionmaker(engine, expire_on_commit=False)



