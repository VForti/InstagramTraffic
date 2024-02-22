from bot.core.keyboards.factories import MainFactory
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

pack_role = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Крипта📊',
                callback_data=MainFactory(action='pack_role',value='crypto').pack(),
            ),
            InlineKeyboardButton(
                text='Казино💸',
                callback_data=MainFactory(action='pack_role',value='casino').pack(),
            )
        ],
        [

            InlineKeyboardButton(
                text='Нутра💄',
                callback_data=MainFactory(action='pack_role',value='nutra').pack(),
            ),
            InlineKeyboardButton(
                text='Дейтинг👧',
                callback_data=MainFactory(action='pack_role',value='deting').pack(),
            )
        ],
        [
            InlineKeyboardButton(
                text='Бейтинг⚽️',
                callback_data=MainFactory(action='pack_role',value='betting').pack(),
            ),
            InlineKeyboardButton(
                text='Меню📛️',
                callback_data='menu'
            ),
        ],
    ])
# -


new_pack = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Крипта📊',
                callback_data=MainFactory(action='new_pack',value='crypto').pack(),
            ),
            InlineKeyboardButton(
                text='Казино💸',
                callback_data=MainFactory(action='new_pack',value='casino').pack(),
            )
        ],
        [

            InlineKeyboardButton(
                text='Нутра💄',
                callback_data=MainFactory(action='new_pack',value='nutra').pack(),
            ),
            InlineKeyboardButton(
                text='Дейтинг👧',
                callback_data=MainFactory(action='new_pack',value='deting').pack(),
            )
        ],
        [
            InlineKeyboardButton(
                text='Бейтинг⚽️',
                callback_data=MainFactory(action='new_pack',value='betting').pack(),
            ),
            InlineKeyboardButton(
                text='Меню📛️',
                callback_data='menu'
            ),
        ],
    ])
# -
