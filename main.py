# This is main file

# telebot telegram api 
# install it with pip3 install pyTelegramBotAPI 
# you can call in in python file with import telebot

import telebot

class main_bot():
    
    Auther = 'Benyamin'
    Email = 'benyaminmahmoudyan@gmail.com'
    phone = '+98-910-966-7550'
    tele_user_name = '@bny1485'

    def __init__(self, token, your_msg):
        self.token = token
        self.your_msg = your_msg

    def about_me(self, Auther, Email, phone):
        msg = f'I am {Auther} my email address is {Email} and this is my phone number {phone}'
        return msg

    def it_is_work(self, your_mas, tele_user_name):
        return f'I am Bny1485 Bot you can contact my owner with his telegram user name {tele_user_name} your token is {token} and your massge to me is {your_msg}'


token = input('Welcome to Bny1485_Bot\nplase give me your bot token: ')
user_msg = input('what is your massge for Auther : ')

