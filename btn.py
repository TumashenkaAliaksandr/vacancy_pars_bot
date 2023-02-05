from telebot import types


#русское меню
russian_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
russian_menu.row('Проверить 🔄', 'О нас 🤖')

russian_menu_check = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
russian_menu_check.row('Проверить 🔄')

#МЕНЮ кнопки Настройки ЯЗЫК
about_rus = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton(text='📲 аккаунт разработчика в телеграмм', url='https://t.me/ultravioletpartyeyes')
btn2 = types.InlineKeyboardButton('👄 Изменить язык', callback_data='👄 Изменить язык')
about_rus.add(btn1, btn2)
# -----------------------------------------------

# Английское меню
english_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
english_menu.row('Check 🔄', 'About us 🤖')

eng_about = types.InlineKeyboardMarkup()
btn3 = types.InlineKeyboardButton(text='📲 Develop Telegram account', url='https://t.me/ultravioletpartyeyes')
btn4 = types.InlineKeyboardButton('👄 Choose language', callback_data='👄 Choose language')
eng_about.add(btn3, btn4)
# -------------------------------------------------------------------------------------
