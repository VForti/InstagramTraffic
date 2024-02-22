from bot.core.keyboards.factories import MainFactory
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Залив✅',
                callback_data='bay'
            ),
            InlineKeyboardButton(
                text='Паки🔥',
                callback_data='list_pack'
            )
        ],
    ])
# -




exits = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Меню📛',
                callback_data='menu'
            ),

        ],
    ])
# -





bay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Крипта📊',
                callback_data='crypto'
            ),
            InlineKeyboardButton(
                text='Казино💸',
                callback_data='casino'
            )
        ],
        [

            InlineKeyboardButton(
                text='Нутра💄',
                callback_data='nutra'
            ),
            InlineKeyboardButton(
                text='Дейтинг👧',
                callback_data='deting'
            )
        ],
        [
            InlineKeyboardButton(
                text='Бейтинг⚽️',
                callback_data='betting'
            )
        ],


    ])
# -



