from aiogram.fsm.state import StatesGroup, State

class Refill(StatesGroup):
    money = State()