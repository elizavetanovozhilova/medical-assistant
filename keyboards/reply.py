from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Каталог")],
        [KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="ℹ️ О нас")],
        [KeyboardButton(text="📞 Контакты"), KeyboardButton(text="⚙️ Настройки")]
    ],
    resize_keyboard=True
)

# Кнопка отправки номера телефона
phone_request = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Отправить номер", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Кнопка отправки местоположения
location_request = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Отправить местоположение", request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)