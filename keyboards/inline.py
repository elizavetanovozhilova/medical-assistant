from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="Да", callback_data="auth")],
        [InlineKeyboardButton(text="Нет", callback_data="register")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_main_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="📝 Запись к врачу", callback_data="appointment")],
        [InlineKeyboardButton(text="💊 Мои лекарства", callback_data="medicines")],
        [InlineKeyboardButton(text="🩺 Мед карта", callback_data="medical_card")],
        [InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_doctors_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="Терапевт", callback_data="doctor_therapist")],
        [InlineKeyboardButton(text="Кардиолог", callback_data="doctor_cardio")],
        [InlineKeyboardButton(text="Невролог", callback_data="doctor_neuro")],
        [InlineKeyboardButton(text="Назад", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)