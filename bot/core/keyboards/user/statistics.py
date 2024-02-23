from bot.core.keyboards.factories import MainFactory
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

static = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Крипта📊',
                callback_data=MainFactory(action='static',value='crypto').pack(),
            ),
            InlineKeyboardButton(
                text='Казино💸',
                callback_data=MainFactory(action='static',value='casino').pack(),
            )
        ],
        [

            InlineKeyboardButton(
                text='Нутра💄',
                callback_data=MainFactory(action='static',value='nutra').pack(),
            ),
            InlineKeyboardButton(
                text='Дейтинг👧',
                callback_data=MainFactory(action='static',value='deting').pack(),
            )
        ],
        [
            InlineKeyboardButton(
                text='Бейтинг⚽️',
                callback_data=MainFactory(action='static',value='betting').pack(),
            ),
            InlineKeyboardButton(
                text='Меню📛️',
                callback_data='menu'
            ),
        ],
    ])
# -


static_func = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Меню📛',
                callback_data='menu',
            ),
            InlineKeyboardButton(
                text='Зупинити📛',
                callback_data='stop_bay',
            )
        ],
    ])
# -
