from config import token
import telebot
from random import choice

print(token)

bot = telebot.TeleBot(token)


text_messages = {
    'welcome':
        u'Please welcome {name}!\n\n'
        u'This chat is intended for questions about and discussion of the pyTelegramBotAPI.\n'
        u'To enable group members to answer your questions fast and accurately, please make sure to study the '
        u'project\'s documentation (https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md) and the '
        u'examples (https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) first.\n\n'
        u'I hope you enjoy your stay here!',

    'info':
        u'My name is TeleBot,\n'
        u'I am a bot that assists these wonderful bot-creating people of this bot library group chat.\n'
        u'Also, I am still under development. Please improve my functionality by making a pull request! '
        u'Suggestions are also welcome, just drop them in this group chat!',

    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['info', 'help'])
def on_info(message):
    if not is_api_group(message.chat.id):
        bot.reply_to(message, text_messages['wrong_chat'])
        return

    bot.reply_to(message, text_messages['info'])

class telebot.types.PhotoSize(file_id, file_unique_id, width, height, file_size=None, **kwargs)

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)
    
bot.infinity_polling()