### --------------------- This is main file -------------------------- ###
# telebot telegram api
# install it with pip3 install pyTelegramBotAPI
# you can call in in python file with import telebot

import telebot

# for more scurety
with open(r"/home/bny1485/source_code/Bny1485_Bot/token_file.txt", "r") as txt_file:
    bot_token = txt_file.readline()

bot = telebot.TeleBot(bot_token)
print(bot_token)


## ------ this function tell abot programmmer of this bot -------##
@bot.message_handler(commands=['start', 'Auther', 'Bot'])
def About(user):
    usr_id = user.from_user.id
    main_text = user.text
    if "/Auther" == main_text:
        bot.send_message(usr_id, 'I am Benyamin my email address is benyaminmahmoudyan@gmail.com and this is my phone number +98-910-966-7550 you can contact me in telegram by @bny1485 instagram with this id @bny1485')
    if "/start" in main_text:
        bot_command = '/start\n/Auther\n/Bot'
        bot.send_message(usr_id, bot_command)
    if "/Bot" in main_text:
        bot.send_message(
            usr_id, 'my name is seventh robot I am from Seventh Regiment')


bot.polling()
