from aiogram.fsm.state import State, StatesGroup



class AccountStates(StatesGroup):
    count = State()


class VideoStates(StatesGroup):
    name = State()
    link = State()


class PackStates(StatesGroup):
    name = State()
    role = State()