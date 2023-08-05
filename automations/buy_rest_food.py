from common import user
from common.session import Session

bot = user.User("itinerarydismiss395@simplelogin.com", "R%KM&6VP3giUcS9%")
current_session = Session(bot)

print(bot, current_session)