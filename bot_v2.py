from aiogram import Bot, Dispatcher, executor
from config import TG_TOKEN
import asyncio


loop = asyncio.get_event_loop()
bot = Bot(TG_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)


if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)