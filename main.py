### --------------------- This is main file -------------------------- ###
# telebot telegram api
# install it with pip3 install pyTelegramBotAPI
# you can call in in python file with import telebot

import telebot

bot_token = "1211332991:AAFEJylXhEOfLanJavEkJVorQ0umHNmoK2w"
bot = telebot.TeleBot(bot_token)

msg = ['I am Benyamin my email address is benyaminmahmoudyan@gmail.com \
    and this is my phone number +98-910-966-7550 you can contact me in in t \
    elegram by @bny1485 instagram with this id @bny1485', 'my name is seventh robot I am from Seventh Regiment']


## ------ this function tell abot programmmer of this bot -------##
@bot.message_handler(command=['Auther'])
def Hi(user):
    usr_id = user.from_user.id
    bot.send_message(usr_id, "Yes, dear 😉🌹")
    global msg
    bot.send_message(usr_id, msg[0])


## ------- help and command massege ------- ##
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global msg
    if message == "start":
        bot.reply_to(message, 'Hi. welcome to my bot 👋')
    elif message == "help":
        bot.reply_to(message, msg[1])


bot.polling()
