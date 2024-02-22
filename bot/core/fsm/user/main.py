from aiogram.fsm.state import State, StatesGroup



class VideoStates(StatesGroup):
    name = State()
    link = State()


class PackStates(StatesGroup):
    name = State()
    role = State()