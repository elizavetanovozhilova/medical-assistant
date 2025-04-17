from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config import TOKEN
from handlers import common, admin
#from filters.is_admin import IsAdmin


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Регистрируем обработчики с фильтрами
    dp.message.register(common.start_command, Command("start"))
    #dp.message.register(admin.admin_panel, Command("admin"), IsAdmin())

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())