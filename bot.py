import telebot, time
import sqlite3
from book_stikers import *
from config import *
from book import *
from btn import *
from hh_parsing import parse_data
from handle_data import handel_vacancies


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('db1.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users_id(
        id INTEGER UNIQUE
    )""")
    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM users_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:

        user_id = [message.chat.id]
        cursor.execute("INSERT INTO users_id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, '👋 Nice to see you again!')
    bot.send_sticker(message.chat.id, sticker)  # выводим первый стикер
    bot.send_message(message.chat.id, message.from_user.first_name + hello)  # приветствие используя id
    bot.send_message(message.chat.id, lang, reply_markup=keyboard1)  # выводим клавиатуру для выбора языка


keyboard1 = types.ReplyKeyboardMarkup(True)  # клава выбора языка(используем book для переменных)
keyboard1.row(rus, eng)

@bot.message_handler(content_types=['text'])  # любое сообщение текст
def send_text(message):
    # англ ветка
    if message.text == '🇬🇧 English':
        bot.send_message(message.chat.id, lang_eng, reply_markup=english_menu)
        bot.send_sticker(message.chat.id, sticker_cool)

    elif message.text == 'About us 🤖':
        bot.send_sticker(message.chat.id, sticker_man)
        bot.send_message(message.from_user.id, about_me_eng_txt, reply_markup=eng_about)

    elif message.text == 'Check 🔄':  # запрос на вакансии
        bot.send_message(message.from_user.id, Loading_eng)
        bot.send_sticker(message.chat.id, sticker_dance)
        raw_data = parse_data()
        data = handel_vacancies(raw_data)
        if not data:
            bot.send_message(message.chat.id, 'There are no new vacancies yet..')
        else:
            for text in data:
                time.sleep(0.8)
                bot.send_message(message.chat.id, text, parse_mode='html')


    # русская ветка
    elif message.text == '🇷🇺 Русский':
        bot.send_message(message.chat.id, lang_rus, reply_markup=russian_menu)
        bot.send_sticker(message.chat.id, sticker_alkash)

    elif message.text == 'О нас 🤖':
        bot.send_sticker(message.chat.id, sticker_man)
        bot.send_message(message.from_user.id, about_me_txt, reply_markup=about_rus)

    elif message.text == 'Проверить 🔄':
        bot.send_message(message.from_user.id, Loading_rus)
        bot.send_sticker(message.chat.id, sticker_dance)
        raw_data = parse_data()
        data = handel_vacancies(raw_data)
        if not data:
            bot.send_message(message.chat.id, 'новых вакансий пока нет..')
        else:
            for text in data:
                time.sleep(0.8)
                bot.send_message(message.chat.id, text, parse_mode='html')


# менюшка инлайн клавиатуры (ответы)
@bot.callback_query_handler(func=lambda call: call.data == "👄 Изменить язык")
def callback_worker(call):
    if call.data == "👄 Изменить язык":
        bot.send_message(call.message.chat.id, lang, reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda call: call.data == "👄 Choose language")
def callback_worker(c):
    if c.data == "👄 Choose language":
        bot.send_message(c.message.chat.id, lang, reply_markup=keyboard1)

@bot.message_handler()
def another_answer(message):
    bot.send_message(message.chat.id, underst, reply_markup=russian_menu_check)


if __name__ == '__main__':
     bot.infinity_polling()