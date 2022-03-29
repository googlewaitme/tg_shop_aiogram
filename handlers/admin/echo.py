from loader import dp

from aiogram import types

from filters import IsUser, IsAdmin
from handlers.user.menu import admin_menu, user_menu


@dp.message_handler(IsUser())
async def send_user_echo(message: types.Message):
    await user_menu(message)


@dp.message_handler(IsAdmin())
async def send_admin_echo(message: types.Message):
    await admin_menu(message)
