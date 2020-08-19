# This is main file

# telebot telegram api 
# install it with pip3 install pyTelegramBotAPI 
# you can call in in python file with import telebot

import telebot

class main_bot():

    def __init__(self, token, your_msg):
        self.Auther = 'Benyamin'
        self.Email = 'benyaminmahmoudyan@gmail.com'
        self.phone = '+98-910-966-7550'
        self.tele_user_name = '@bny1485'
        self.token = token
        self.your_msg = user_msg

    def about_me(self):
        msg = f'I am {self.Auther} my email address is {self.Email} and this is my phone number {self.phone}'
        return msg

    def it_is_work(self):
        return f'I am Bny1485 Bot you can contact my owner with his telegram user name {self.tele_user_name} your token is {self.token} and your massge to me is {self.your_msg}'

token = input('Welcome to Bny1485_Bot\nplase give me your bot token: ')
user_msg = input('what is your massge for Auther : ')

call_bot = main_bot(token, user_msg)
print(call_bot.about_me())
print(call_bot.it_is_work())