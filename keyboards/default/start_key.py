from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_markup():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('✅Заполнить анкету✅'))
    return keyboard
