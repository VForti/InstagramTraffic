import os
from io import BytesIO

from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.types import (
    Message,
    InputFile
)

from bot.core.keyboards.user import start, exits, pack_role, video_func, video_update, static, static_func
from aiogram.filters import CommandStart, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext

from app.database import Database
from bot.core.fsm import VideoStates

from bot.core.keyboards.factories import MainFactory

from app.configuration.configuration import Configuration


router = Router()


async def get_all_bay(statics) -> dict[str, int]:
    static_list = {}
    for static in statics:
        if  static.goal:
            static_list[f'{static.goal}'] = static.bay_id
    return static_list

@router.callback_query(F.data == 'static')
async def callback_query(
        callback: CallbackQuery,
        bot: Bot,
        state: FSMContext,
        database: Database,
):
    await callback.message.edit_text(
        'Виберіть категорію:',
        reply_markup=static
    )


@router.callback_query(MainFactory.filter(F.action=='static'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        state: FSMContext,
        database: Database,
):
    statics = await database.get_all_bay_by_role(callback_data.value)
    if statics == []:
        await callback.message.edit_text(
            f'У вас немає активних заливів!',
            reply_markup=exits
        )
        return

    pack_list = await get_all_bay(statics)
    joined = '\n'.join([f'{key}: {value}' for key, value in pack_list.items()])
    split_lines = joined.split('\n')

    line_list = []
    for line in split_lines:
        line_list.append(line)

    await callback.message.edit_text(
        f'{callback.from_user.full_name} ваші заливи у категорії - {callback_data.value}!',
        reply_markup=await MainFactory.bay_static_button(line_list=line_list)
    )

@router.callback_query(MainFactory.filter(F.action=='bay_static'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        state: FSMContext,
        database: Database,
):
    bay = await database.get_bay(int(callback_data.value))
    await callback.message.edit_text(
        f'Ціль: {bay.goal}\n'
        f'Залили: {bay.now_done}\n'
        f'Категорія: {bay.role}',
        reply_markup=static_func
    )

    await state.update_data(bay=bay.bay_id)


@router.callback_query(MainFactory.filter(F.action=='bay_static'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        state: FSMContext,
        database: Database,
):
    data = await state.get_data()

    await database.update_bay(int(data.get('bay')), {'done': True})
    await callback.message.answer(
        'Успішно завершили залив✅'
    )



