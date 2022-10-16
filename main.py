import logging
from configs import token, otvet, questions
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token)
dp = Dispatcher(bot)
users = {}
global questions
global users


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Введите свою фамилию")
    bot.

@dp.message_handler()
async def xd(message: types.Message):



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)