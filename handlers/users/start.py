from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data.config import messages
from keyboards.default import start_key


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = start_key.get_markup()
    await message.answer(messages['start_message'], reply_markup=keyboard)
