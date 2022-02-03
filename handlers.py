from bot_v2 import bot, dp
from aiogram.types import Message
from config import TG_TOKEN, ADMIN_ID
from request_price_stock import get_stock_info

async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')

@dp.message_handler()
async def asnwer(message):
    text = str(get_stock_info('SBER.ME'))
    await message.answer(text=text)
