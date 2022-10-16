import logging
from configs import token
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token)
dp = Dispatcher(bot)


otvet = {
    "А" : [],
    "Б" : [],
    "В" : [],
    }


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Расставляй в порядке приоритета")


@dp.message_handler()
async def xd(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)