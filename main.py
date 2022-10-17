import logging
from configs import token, otvet, questions
# import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ParseMode
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class User(StatesGroup):
    name = State()
    surname = State()
    group = State()
    test = {}
    for num in otvet:
        test[num] = State()


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Начало теста
    """
    # Set state
    await User.name.set()

    await bot.send_message(message.chat.id, "Имя")


'''# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())'''


@dp.message_handler(state=User.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await User.next()
    await bot.send_message(message.chat.id, "Фамилия")


@dp.message_handler(lambda message: not message.text.isdigit(), state=User.surname)
async def process_surname(message: types.Message, state: FSMContext):
    # Update state and data
    await User.next()
    await state.update_data(surname=message.text)

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("8К23", "8К24")

    await bot.send_message(message.chat.id, "Группа", reply_markup=markup)


@dp.message_handler(lambda message: message.text not in ["8К23", "8К24"], state=User.group)
async def process_group_invalid(message: types.Message):
    return await bot.send_message(message.chat.id, "Группа")


@dp.message_handler(state=User.group)
async def process_group(message: types.Message, state: FSMContext):
    await User.next()
    await state.update_data(group=message.text)

    # Remove keyboard
    markup = types.ReplyKeyboardRemove()

    await bot.send_message(
        message.chat.id,
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4",
        reply_markup=markup
    )
    await bot.send_message(
        message.chat.id,
        "Задание " + list(questions.keys())[0] + questions[list(questions.keys())[0]]
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
