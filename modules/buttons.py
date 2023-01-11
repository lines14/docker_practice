from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/создать')
b2 = KeyboardButton('/получить')
b3 = KeyboardButton('/отмена')

keys = ReplyKeyboardMarkup(resize_keyboard=True) # one_time_keyboard=True
keys.add(b1).insert(b2)

keys2 = ReplyKeyboardMarkup(resize_keyboard=True)
keys2.add(b3)

# keyboard: Optional[List[List[KeyboardButton]]] = None
async def keyboard_generator(key_list):
    # key_list = ['1', '2', '3']
    tmp_buttons = []
    for i in key_list:
        tmp_buttons.append([KeyboardButton(i)])
    tmp_buttons.append([KeyboardButton('/cancel')])
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=tmp_buttons)
    return keyboard