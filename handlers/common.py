from aiogram import types
from keyboards.inline import start


async def start_command(message: types.Message):
    welcome_text = "👋 Добро пожаловать, я Разумед Бот — ваш медицинский помощник! У вас уже есть аккаунт?"

    await message.answer(
        text=welcome_text,
        reply_markup=start()
    )