import telebot
import constants
import random

bot = telebot.TeleBot(constants.token)
"""
print(bot.get_me())
"""


def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("сообщение от {0} {1}. (id = {2}) \nСообщение:  {3}".format(message.from_user.first_name,
                                                                      message.from_user.last_name,
                                                                      str(message.from_user.id),
                                                                      message.text))
    print(answer)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Какой я сегодня?', 'Очистить историю')
    bot.send_message(message.from_user.id, 'прив', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'пок', reply_markup=hide_markup)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, """Я ПОКА НИХЕРА НЕ УМЕЮ, НО СКОРО ПОРАБОЩУ ВСЕХ ЛЮДИШЕК""")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "ясно"
    name = str(message.from_user.first_name + " " + message.from_user.last_name)
######сохранение сообщений в списки#######
    if message.text == answer:
        for constants.deleted_messages_bot in constants.messages_bot:
            constants.messages_bot = str(message.from_user.id)
        for constants.deleted_messages_my in constants.messages_my:
            constants.messages_my = str(message.text)
######сохранение сообщений в списки#######
    if message.from_user.last_name is None:
        message.from_user.last_name = ""

    if str(message.from_user.id) == "399878105":
        name = "Димас"
    if str(message.from_user.id) == "443688665":
        name = "Некит"
    if str(message.from_user.id) == "472355950":
        name = "Саня"

    if message.text.lower() == "привет":
        answer = "привет ты чо охуел"
        log(message, answer)
        bot.send_message(message.chat.id, "привет ты чо охуел")
    elif message.text.lower() == "какой я сегодня?":
        random_word_1 = random.choice(constants.first_word)
        random_word_2 = random.choice(constants.second_word)
        random_word_3 = random.choice(constants.third_word)
        random_word_4 = random.choice(constants.fourth_word)
        random_word_5 = random.choice(constants.fifth_word)
        epic_phrase = str("Ну что ж, " + name + ". "
                          + random_word_1 + ", "
                          + random_word_2 + " "
                          + random_word_3 + ", "
                          + random_word_4 + " "
                          + random_word_5)
        log(message, epic_phrase)
        bot.send_message(message.chat.id, epic_phrase)
    elif message.text.lower() == "очистить историю":
        answer = "сообщения удалены. (нет)"
        for constants.deleted_messages_bot in constants.messages_bot:
            bot.delete_message(472355950, str(message.text))
        log(message, answer)
        bot.send_message(message.chat.id, "сообщения удалены. (нет)")
    elif message.text.lower() == "ясно":
        answer = "понятно"
        log(message, answer)
        bot.send_message(message.chat.id, "понятно")
    elif message.text.lower() == "пока":
        answer = "ты пидор"
        log(message, answer)
        bot.send_message(message.chat.id, "ты пидор")
    elif message.text.lower() == "ты":
        answer = "пидор"
        log(message, answer)
        bot.send_message(message.chat.id, "пидор")
    elif message.text.lower() == "нет ты":
        answer = "а может быть ты пидор? мммм?!"
        log(message, answer)
        bot.send_message(message.chat.id, "а может быть ты пидор? мммм?!")
    elif message.text.lower() == "саня лох":
        answer = "а может быть ты лох? ММММ?!"
        log(message, answer)
        bot.send_message(message.chat.id, "а может быть ты лох? ММММ?!")
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)


bot.polling(none_stop=True, interval=0)


