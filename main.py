from translate import translate
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6121874631:AAE84ypIZglf6Mph3ZUya3D8pxYhwax2p2E'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"<b>👋 Assalomu alaykum {message.from_user.first_name}</b>"
                         f"\n\n♻️ Bu bot uz-en-uz tarjima qila oladi!"
                         f"\n\n<b>⚠️ Ya'ni o'zbekchadan inglizchaga inglizchadan o'zbekchaga tarjima qila oladi.</b>"
                         f"\n\n<i>Botdan foydalanishiz uchun iltimos tarjima qilish kerak bo'lgan matnni yuboring</i>")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(translate(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)