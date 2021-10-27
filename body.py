import vk_api, config
from sql import SQL
from vk_api.longpoll import *
from vk_api.bot_longpoll import *

sql =SQL()
class Bot:
    def __init__(self):
        self.vk = vk_api.VkApi(token=config.token)
        self.longpoll = VkBotLongPoll(self.vk, config.idbot)
        self.vk._auth_token()
        self.vk = self.vk.get_api()
    def work(self):
        pass