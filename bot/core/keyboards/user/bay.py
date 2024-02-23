from bot.core.keyboards.factories import MainFactory
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bay_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Крипта📊',
                callback_data=MainFactory(action='bay_category',value='crypto').pack(),
            ),
            InlineKeyboardButton(
                text='Казино💸',
                callback_data=MainFactory(action='bay_category',value='casino').pack(),
            )
        ],
        [

            InlineKeyboardButton(
                text='Нутра💄',
                callback_data=MainFactory(action='bay_category',value='nutra').pack(),
            ),
            InlineKeyboardButton(
                text='Дейтинг👧',
                callback_data=MainFactory(action='bay_category',value='deting').pack(),
            )
        ],
        [
            InlineKeyboardButton(
                text='Бейтинг⚽️',
                callback_data=MainFactory(action='bay_category',value='betting').pack(),
            ),
            InlineKeyboardButton(
                text='Меню📛️',
                callback_data='menu'
            ),
        ],
    ])
# -

