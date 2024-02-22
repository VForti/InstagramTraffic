import os
from io import BytesIO

from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.types import (
    Message,
    InputFile
)

from bot.core.keyboards.user import start, exits, pack_role, video_func, video_update
from aiogram.filters import CommandStart, CommandObject, StateFilter
from aiogram.fsm.context import FSMContext

from app.database import Database
from bot.core.fsm import VideoStates

from bot.core.keyboards.factories import MainFactory

from app.configuration.configuration import Configuration


router = Router()



@router.callback_query(MainFactory.filter(F.action=='video_func'))
async def callback_query(
        callback: CallbackQuery,
        callback_data: MainFactory,
        bot: Bot,
        state: FSMContext,
        database: Database,
):
    if callback_data.value == 'update':
        await callback.message.edit_text(
            'Ви хоче редагувати що?:',
            reply_markup=video_update
        )
    if callback_data.value == 'del':
        data = await state.get_data()
        await callback.message.edit_text(
            'Видалили✅',
        )
        await database.delete_video(int(data.get("video_id")))

    if callback_data.value == 'add_video':
        await state.set_state(VideoStates.name)
        await callback.message.edit_text(
            'Введіть назву відео:',
        )




@router.message(StateFilter(VideoStates.name))
async def process_message(
        message: Message,
        bot: Bot,
        database: Database,
        state: FSMContext,
):
    await state.set_state(VideoStates.link)
    await message.answer(
        'Скиньте відео сюда:',
    )
    await state.update_data(name=message.text)

@router.message(StateFilter(VideoStates.link))
async def process_message(
        message: Message,
        bot: Bot,
        database: Database,
        state: FSMContext,
):
    data = await state.get_data()
    link = message.video.file_id


    # Отримання об'єкту файлу
    file = await bot.get_file(link)

    # Створення каталогу "video", якщо його не існує
    video_dir = "video"
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)

    # Створення шляху до файлу з унікальним ідентифікатором користувача та унікальним ідентифікатором файлу
    path = f"{video_dir}/{message.from_user.id}_{file.file_unique_id}.mp4"

    # Завантаження файлу
    await bot.download_file(file.file_path, path)

    # Створення запису в базі даних
    video = await database.create_video(
        name=data.get("name"),
        pack=int(data.get("pack_id")),
        link=path
    )

    await bot.send_video(
        chat_id=message.chat.id,
        video=FSInputFile(video.link),
        caption=f'{video.name}\n'
    )