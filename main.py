import logging
from configs import token, questions, code
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from answers import Answers
import pandas as pd


logging.basicConfig(level=logging.INFO)
bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
excel_dreval = {
    'ФИО': [],
    'Группа': [],
    'Синтетический стиль': [],
    'Идеалистический стиль': [],
    'Прагматический стиль': [],
    'Аналитичесеий стиль': [],
    'Реалистический стиль': []
}


class User(StatesGroup):
    fio = State()
    group = State()
    test1 = State()
    test2 = State()
    test3 = State()
    test4 = State()
    test5 = State()
    test6 = State()
    test7 = State()
    test8 = State()
    test9 = State()
    test10 = State()
    test11 = State()
    test12 = State()
    test13 = State()
    test14 = State()
    test15 = State()
    test16 = State()
    test17 = State()
    test18 = State()


@dp.message_handler(commands=code)
async def cmd_excel_print(message: types.Message):
    pd.DataFrame(excel_dreval).to_excel('./dreval.xlsx', index=False)
    await bot.send_document(
        message.chat.id,
        open('dreval.xlsx', 'rb')
    )


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    """
    Начало теста
    """
    # Set state
    await User.fio.set()

    await bot.send_message(message.chat.id, "ФИО")


# You can use state '*' if you need to handle all states
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
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=User.fio)
async def process_surname(message: types.Message, state: FSMContext):
    # Update state and data
    async with state.proxy() as data:
        data['fio'] = message.text
    await User.next()

    await bot.send_message(message.chat.id, "Группа")


@dp.message_handler(state=User.group)
async def process_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )
    await bot.send_message(
        message.chat.id,
        "Задание А" + questions['А']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test1
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test1)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test1'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Б" + questions['Б']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test2
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test2)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test2'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание В" + questions['В']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test3
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test3)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test3'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Г" + questions['Г']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test4
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test4)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test4'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Д" + questions['Д']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test5
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test5)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test5'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Е" + questions['Е']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test6
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test6)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test6'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Ж" + questions['Ж']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test7
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test7)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test7'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание З" + questions['З']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test8
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test8)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test8'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание И" + questions['И']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test9
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test9)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test9'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание К" + questions['К']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test10
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test10)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test10'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Л" + questions['Л']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test11
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test11)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test11'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание М" + questions['М']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test12
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test12)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test12'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Н" + questions['Н']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test13
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test13)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test13'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание О" + questions['О']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test14
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test14)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test14'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание П" + questions['П']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test15
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test15)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test15'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Р" + questions['Р']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test16
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test16)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test16'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание С" + questions['С']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test17
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test17)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test17'] = list(message.text.split(" "))
    await User.next()

    await bot.send_message(
        message.chat.id,
        "Задание Т" + questions['Т']
    )


@dp.message_handler(
    lambda message: sorted(list(message.text.split(" "))) != ["1", "2", "3", "4", "5"],
    state=User.test18
)
async def process_gender_invalid(message: types.Message):
    return await message.reply(
        "Расставляй цифры через пробел, в порядке приоритета, что ты считаешь более важным, пример:\n3 2 5 1 4"
    )


@dp.message_handler(state=User.test18)
async def process_test1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['test18'] = list(message.text.split(" "))

        excel_dreval['ФИО'].append(data['fio'])
        excel_dreval['Группа'].append(data['group'])
        k = 0
        lst = [
            "Синтетический стиль",
            "Идеалистический стиль",
            "Прагматический стиль",
            "Аналитичесеий стиль",
            "Реалистический стиль"
        ]
        for res in Answers(
            {
                'А': list(map(int, ' '.join(list(data['test1'])).split(' '))),
                'Б': list(map(int, ' '.join(list(data['test2'])).split(' '))),
                'В': list(map(int, ' '.join(list(data['test3'])).split(' '))),
                'Г': list(map(int, ' '.join(list(data['test4'])).split(' '))),
                'Д': list(map(int, ' '.join(list(data['test5'])).split(' '))),
                'Е': list(map(int, ' '.join(list(data['test6'])).split(' '))),
                'Ж': list(map(int, ' '.join(list(data['test7'])).split(' '))),
                'З': list(map(int, ' '.join(list(data['test8'])).split(' '))),
                'И': list(map(int, ' '.join(list(data['test9'])).split(' '))),
                'К': list(map(int, ' '.join(list(data['test10'])).split(' '))),
                'Л': list(map(int, ' '.join(list(data['test11'])).split(' '))),
                'М': list(map(int, ' '.join(list(data['test12'])).split(' '))),
                'Н': list(map(int, ' '.join(list(data['test13'])).split(' '))),
                'О': list(map(int, ' '.join(list(data['test14'])).split(' '))),
                'П': list(map(int, ' '.join(list(data['test15'])).split(' '))),
                'Р': list(map(int, ' '.join(list(data['test16'])).split(' '))),
                'С': list(map(int, ' '.join(list(data['test17'])).split(' '))),
                'Т': list(map(int, ' '.join(list(data['test18'])).split(' '))),
            }
        ).sorted().split('\n'):
            excel_dreval[lst[k]].append(res.replace(lst[k] + ": ", ""))
            k += 1

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text(
                    Answers(
                        {
                            'А': list(map(int, ' '.join(list(data['test1'])).split(' '))),
                            'Б': list(map(int, ' '.join(list(data['test2'])).split(' '))),
                            'В': list(map(int, ' '.join(list(data['test3'])).split(' '))),
                            'Г': list(map(int, ' '.join(list(data['test4'])).split(' '))),
                            'Д': list(map(int, ' '.join(list(data['test5'])).split(' '))),
                            'Е': list(map(int, ' '.join(list(data['test6'])).split(' '))),
                            'Ж': list(map(int, ' '.join(list(data['test7'])).split(' '))),
                            'З': list(map(int, ' '.join(list(data['test8'])).split(' '))),
                            'И': list(map(int, ' '.join(list(data['test9'])).split(' '))),
                            'К': list(map(int, ' '.join(list(data['test10'])).split(' '))),
                            'Л': list(map(int, ' '.join(list(data['test11'])).split(' '))),
                            'М': list(map(int, ' '.join(list(data['test12'])).split(' '))),
                            'Н': list(map(int, ' '.join(list(data['test13'])).split(' '))),
                            'О': list(map(int, ' '.join(list(data['test14'])).split(' '))),
                            'П': list(map(int, ' '.join(list(data['test15'])).split(' '))),
                            'Р': list(map(int, ' '.join(list(data['test16'])).split(' '))),
                            'С': list(map(int, ' '.join(list(data['test17'])).split(' '))),
                            'Т': list(map(int, ' '.join(list(data['test18'])).split(' '))),
                        }
                    ).sorted()
                ),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN,
        )

        await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
