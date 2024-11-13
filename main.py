import telebot

import sqlite3

import config

bot = telebot.TeleBot(config.token)


def open_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    return [conn, cur]
def close_db(base):
    base[1].close()    
    base[0].commit()
    base[0].close()    

def typemsg(message, typemsg):
    base = open_db()
    base[1].execute(f"SELECT typemsg FROM users WHERE id={message.from_user.id}")
    result = base[0].fetchone()
    if result != []:
        base[1].execute(f"UPDATE users SET typemsg={typemsg} WHERE id={message.from_user.id}")
    else:
        base[1].execute(f"INSERT INTO users (id, first_name, last_name, username, typemsg) VALUES ({message.from_user.id}, '{message.from_user.first_name}', '{message.from_user.last_name}', '{message.from_user.username}', {typemsg})")
    close_db(base)

def user(message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    base = open_db()
    base[1].execute(f"SELECT * FROM users WHERE id={id}")
    result = base[1].fetchone()
    if result != []:
        if result[4]!=None:
            close_db(base)
            return result
        else:
            bot.send_message(message.cht.id, "Введите свои полное имя и фамилию через пробел.\n Пример 'Иван Иванов'.")
            typemsg(message, "set_real_name")


@bot.message_handler(commands=['start'])
def start_command(message):
    pass


@bot.message_handler()
def msg_handler(message):
    base = open_db()
    base[1].execute(f"SELECT typemsg FROM users WHERE id={message.from_user.id}")
    result = base[0].fetchone()
    if result!= []:
        typemsg = result[0]
    else:
        user(message)

bot.polling(none_stop=True)