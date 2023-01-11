from aiogram import types, Dispatcher
from modules.bot_base import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from modules.buttons import keys, keys2
from modules.buttons import keyboard_generator
from modules.judicial_writer_1 import data_print
class InputUserData(StatesGroup):
    user_data1 = State()
    user_data2 = State()
    user_data3 = State()
    user_data4 = State()
    user_data5 = State()
    user_data6 = State()
    user_data7 = State()
    user_data8 = State()
    user_data9 = State()
    user_data10 = State()
    user_data11 = State()
    user_data12 = State()
    user_data13 = State()
    user_data14 = State()

async def start_command(message: types.Message):
    # await bot.delete_message(chat_id = message.from_user.id, message_id=message.message_id)
    await bot.send_message(chat_id = message.from_user.id, text='Привет, нажми "создать", а затем введи требуемые данные, чтобы сформировать документ', reply_markup=keys)

async def add_data(message: types.Message):
    await InputUserData.user_data1.set()
    await message.reply('Инстанция для обращения:', reply_markup=keys2)

async def cancel_handlers_pick_data(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вы можете начать заново с нажатия кнопки "создать"', reply_markup=keys)

async def pick_data1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data1'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Адрес инстанции для обращения:')

async def pick_data2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data2'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='ФИО истца:')

async def pick_data3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data3'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Адрес истца:')

async def pick_data4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data4'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Адрес истца для корреспонденции при необходимости:')

async def pick_data5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data5'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Представитель истца:')

async def pick_data6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data6'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Контактные данные представителя истца:')

async def pick_data7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data7'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Ответчик:')

async def pick_data8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data8'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Адрес ответчика:')

async def pick_data9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data9'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Номер дела:')

async def pick_data10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data10'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Дата подачи обращения:')

async def pick_data11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data11'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Текст обращения:')

async def pick_data12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data12'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Процессуальный статус обращающегося:')

async def pick_data13(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data13'] = message.text
    await InputUserData.next()
    await bot.send_message(chat_id = message.from_user.id, text='Инициалы обращающегося:')

async def pick_data14(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_data14'] = message.text
    await data_print(state)
    await bot.send_message(chat_id = message.from_user.id, text='Данные записаны, нажмите "получить", чтобы выгрузить готовый документ', reply_markup=keys)
    await state.finish()

async def get_file(message: types.Message):
    await message.reply_document(open('/home/lines14/projects/judicial_telegram_bot/documents/judicial_writer_1.docx', 'rb'))

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(add_data, commands=['создать'], state=None)
    dp.register_message_handler(cancel_handlers_pick_data, state='*', commands=['отмена'])
    dp.register_message_handler(pick_data1, state=InputUserData.user_data1)
    dp.register_message_handler(pick_data2, state=InputUserData.user_data2)
    dp.register_message_handler(pick_data3, state=InputUserData.user_data3)
    dp.register_message_handler(pick_data4, state=InputUserData.user_data4)
    dp.register_message_handler(pick_data5, state=InputUserData.user_data5)
    dp.register_message_handler(pick_data6, state=InputUserData.user_data6)
    dp.register_message_handler(pick_data7, state=InputUserData.user_data7)
    dp.register_message_handler(pick_data8, state=InputUserData.user_data8)
    dp.register_message_handler(pick_data9, state=InputUserData.user_data9)
    dp.register_message_handler(pick_data10, state=InputUserData.user_data10)
    dp.register_message_handler(pick_data11, state=InputUserData.user_data11)
    dp.register_message_handler(pick_data12, state=InputUserData.user_data12)
    dp.register_message_handler(pick_data13, state=InputUserData.user_data13)
    dp.register_message_handler(pick_data14, state=InputUserData.user_data14)
    dp.register_message_handler(get_file, commands=['получить'])