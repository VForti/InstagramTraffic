from bot.core.keyboards.factories import MainFactory
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

video_func = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Видалити📛',
                callback_data=MainFactory(action='video_func',value='del').pack(),
            ),
            InlineKeyboardButton(
                text='Меню📛️',
                callback_data='menu'
            ),
        ],
    ])
# -


video_update = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Назва😎️',
                callback_data=MainFactory(action='video_update',value='name').pack(),
            ),
            InlineKeyboardButton(
                text='Відео🎥',
                callback_data=MainFactory(action='video_update',value='video').pack(),
            )
        ],
        [
            InlineKeyboardButton(
                text='Меню📛️',
                callback_data='menu'
            ),
        ],
    ])
# -