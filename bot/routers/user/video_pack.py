from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.types import (
    Message,
)

from bot.core.fsm.user.main import PackStates
from bot.core.keyboards.user import start, exits, pack_role, video_func, new_pack
from aiogram.filters import CommandStart, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext

from app.database import Database


from bot.core.keyboards.factories import MainFactory

from app.configuration.configuration import Configuration


router = Router()

config = Configuration()

async def get_all_pack(packs) -> dict[str, int]:
    channel_list = {}
    for pack in packs:
        if pack.name:
            channel_list[f'{pack.name}'] = pack.pack_id
    return channel_list


async def get_all_video(videos) -> dict[str, int]:
    video_list = {}
    for video in videos:
        if video.link:
            video_list[f'{video.name}'] = video.video_id
    return video_list

@router.callback_query(F.data == 'list_pack')
async def callback_query(
        callback: CallbackQuery,
):
    await callback.message.edit_text(
        'Виберіть картегорію пакетів',
        reply_markup=pack_role
    )


@router.callback_query(MainFactory.filter(F.action=='pack_role'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        database: Database,
):
    packs = await database.get_all_pack_by_role(callback_data.value)
    if packs == []:
        await callback.message.edit_text(
            f'У вас ще немає паків!',
            reply_markup=exits
        )
        return

    pack_list = await get_all_pack(packs)
    joined = '\n'.join([f'{key}: {value}' for key, value in pack_list.items()])
    split_lines = joined.split('\n')

    line_list = []
    for line in split_lines:
        line_list.append(line)

    await callback.message.edit_text(
        f'{callback.from_user.full_name} ваші паки у категорії - {callback_data.value}!',
        reply_markup=await MainFactory.video_pack_button(line_list=line_list)
    )


@router.callback_query(MainFactory.filter(F.action=='pack'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        state: FSMContext,
        database: Database,
):

    if callback_data.value == 'add_pack':
        await state.set_state(PackStates.name)
        await callback.message.edit_text(
            f'Введіть назву паку:',
        )
        return

    videos = await database.get_all_by_pack_id(int(callback_data.value))
    pack = await database.get_pack(int(callback_data.value))
    if videos == []:
        await callback.message.edit_text(
            f'У цьому паці ще немає відео!',
            reply_markup=exits
        )
        return

    video_list = await get_all_video(videos)
    joined = '\n'.join([f'{key}: {value}' for key, value in video_list.items()])
    split_lines = joined.split('\n')

    line_list = []
    for line in split_lines:
        line_list.append(line)

    await callback.message.edit_text(
        f'<b>Відео в паку - {pack.name}</b>\n',
        reply_markup=await MainFactory.video_button(line_list=line_list)
    )
    await state.update_data(pack_id=pack.pack_id)


@router.callback_query(MainFactory.filter(F.action=='video'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        bot: Bot,
        state: FSMContext,
        database: Database,
):
    chat = callback.message.chat.id
    message_id = callback.message.message_id
    video = await database.get_video(int(callback_data.value))

    await bot.delete_message(chat, message_id)
    await bot.send_video(
        chat_id=callback.message.chat.id,
        video=FSInputFile(video.link),
        caption=f'{video.name}\n',
        reply_markup=video_func
    )

    await state.update_data(video_id=video.video_id)





@router.message(StateFilter(PackStates.name))
async def process_message(
        message: Message,
        bot: Bot,
        database: Database,
        state: FSMContext,
):
    await state.update_data(name=message.text)
    await message.answer(
        'Виберіть категорію:',
        reply_markup=new_pack
    )


@router.callback_query(MainFactory.filter(F.action=='new_pack'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        bot: Bot,
        state: FSMContext,
        database: Database,
):
    data = await state.get_data()
    new_pack = await database.create_pack(data.get("name"), callback_data.value)

    await callback.message.edit_text(
        'Успішно добавили новий пак✅'
    )