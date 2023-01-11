from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from modules.config import TG_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot, storage=storage)