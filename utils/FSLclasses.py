from aiogram.fsm.state import StatesGroup, State

class Data(StatesGroup):
    ozon_url:str = State()
    