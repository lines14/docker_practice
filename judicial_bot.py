from aiogram.utils.executor import start_webhook
from modules.config import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT
from modules.bot_base import bot
from modules.bot_base import dp

async def on_startup(_):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    print('Бот успешно запущен!')

async def on_shutdown(_):
    await bot.delete_webhook()

from modules import handlers

handlers.register_handler_client(dp)

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )