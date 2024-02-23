import os
from io import BytesIO

from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.types import (
    Message,
    InputFile
)

from bot.core.fsm.user.main import AccountStates
from bot.core.keyboards.user import start, exits, pack_role, video_func, video_update, bay_category
from aiogram.filters import CommandStart, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext

from app.database import Database
from bot.core.fsm import VideoStates

from bot.core.keyboards.factories import MainFactory

from app.configuration.configuration import Configuration


router = Router()



@router.callback_query(F.data == 'bay')
async def callback_query(
        callback: CallbackQuery,
        bot: Bot,
        state: FSMContext,
        database: Database,
):
    await state.set_state(AccountStates.count)
    await callback.message.edit_text(
        'Введіть кількість акаунтів для заливу:',
    )



@router.message(StateFilter(AccountStates.count))
async def process_message(
        message: Message,
        bot: Bot,
        database: Database,
        state: FSMContext,
):
    await state.update_data(count=message.text)
    await message.answer(
        'Виберіть тепер категорію для заливу:',
        reply_markup=bay_category
    )



@router.callback_query(MainFactory.filter(F.action=='bay_category'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        bot: Bot,
        state: FSMContext,
        database: Database,
):
    data = await state.get_data()
    count = data.get("count")

    await callback.message.answer(
        'Залив почався✅'
    )

