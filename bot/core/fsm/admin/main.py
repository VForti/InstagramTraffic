from aiogram.fsm.state import State, StatesGroup



class SendMessageEveryone(StatesGroup):
    enter_message = State()
    enter_bttn = State()
    enter_button_url = State()
    enter_delay_delete = State()
    confirm_send_album = State()