from aiogram.dispatcher.filters.state import StatesGroup, State


class CheckoutState(StatesGroup):
    check_cart = State()
    name = State()
    contacts = State()
    address = State()
    confirm = State()
