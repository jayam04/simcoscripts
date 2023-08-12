from common import user
from helpers.dev_tools import *

from private import simcobot

import time

bot = user.User(simcobot.username, simcobot.password)
# current_session = Session(bot)

# print(bot, current_session)

# print("authenticating")
# current_session.generate_cookies()
# r = current_session.authenticate()
# print(r, r.ok, r.json())
# print("done")

start_dev_mode()
bot.generate_cookies()
# print(1)
# time.sleep(5)
print(bot.authenticate().status_code)
# print(2)
# time.sleep(5)
# bot.get_user_id_and_companies()
# print(3)