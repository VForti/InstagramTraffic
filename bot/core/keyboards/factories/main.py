from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MainFactory(CallbackData, prefix="m"):
    action: str
    value: str

    def __bool__(self):
        if self.value in {"True", "true"}:
            return True
        if self.value in {"False", "false"}:
            return False
        return bool(self.value)

    @staticmethod
    async def video_pack_button(line_list: list):
        builder = InlineKeyboardBuilder()

        for line in line_list:
            join = line.split(': ')
            pack = join[0]
            pack_id = join[1]


            builder.button(text=f'{pack}', callback_data=MainFactory(action='pack', value=f'{pack_id}'))
        builder.adjust(2)
        builder.button(text=f'Назад📛', callback_data=MainFactory(action='menu', value=f'0'))
        return builder.as_markup()

    @staticmethod
    async def video_button(line_list: list):
        builder = InlineKeyboardBuilder()

        for line in line_list:
            join = line.split(': ')
            video = join[0]
            video_id = join[1]

            builder.button(text=f'{video}', callback_data=MainFactory(action='video', value=f'{video_id}'))
        builder.button(text=f'Добавити✅', callback_data=MainFactory(action='video_func', value=f'add_video'))
        builder.button(text=f'Меню📛', callback_data=MainFactory(action='menu', value=f'0'))

        builder.adjust(2)
        return builder.as_markup()

