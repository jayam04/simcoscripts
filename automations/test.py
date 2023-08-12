import time

from common import user
from common.chat import Chat
from helpers.dev_tools import *

from private import simcobot

start_dev_mode()
bot = user.User(simcobot.username, simcobot.password)

bot.generate_cookies()
# print(1)
# time.sleep(5)
print(bot.authenticate().status_code)
bot.get_companies()
bot.get_userid_and_current_company()
# print(2)
# time.sleep(5)
# bot.get_user_id_and_companies()
# print(3)
time.sleep(10)
chat = Chat(bot, 1911682)
chat.send_message("Hello World")
