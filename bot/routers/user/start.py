from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from aiogram.types import (
    Message,
)

from bot.core.keyboards.user import start
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext

from app.database import Database


from bot.core.keyboards.factories import MainFactory

from app.configuration.configuration import Configuration


router = Router()

config = Configuration()

@router.message(CommandStart())
async def process_message(
        message: Message,
        config: Configuration


):
    if message.from_user.id in config.admins:
        await message.answer(
            f'Привіт <b>{message.from_user.first_name}</b>',
            reply_markup=start
        )
    else:
        await message.answer(
            f'...',
        )


@router.callback_query(F.data=='menu')
async def process_message(
        callback: CallbackQuery,
        config: Configuration


):
    await callback.message.edit_text(
        f'Привіт <b>{callback.from_user.first_name}</b>',
        reply_markup=start
    )
