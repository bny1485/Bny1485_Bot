### --------------------- This is main file -------------------------- ###

# telebot telegram api 
# install it with pip3 install pyTelegramBotAPI 
# you can call in in python file with import telebot

import telebot


## -------- in this two line get token form "@botfather" and define bot  ------- ##
token =  "1354592892:AAHdnEWxWPCPe39LCB1yRjxi1fojVzpQQ3s"
bot = telebot.TeleBot(token)
print('I AM start ...')

## ------ this function tell abot programmmer of this bot -------##
@bot.message_handler(commands=['Auther'])
def Hi(user):    
    usr_id = user.from_user.id
    bot.send_message(usr_id, "Yes, dear 😉🌹")

    msg = 'I am Benyamin my email address is benyaminmahmoudyan@gmail.com \
    and this is my phone number +98-910-966-7550 you can contact me in in t \
    elegram by @bny1485 instagram with this id @bny1485'
    
    bot.send_message(usr_id, msg)

## ------- help and command massege ------- ##
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Hi. welcome to my bot 👋')



# this bilt in function to keep bot runing
bot.polling()