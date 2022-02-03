from bot_v2 import bot, dp
from aiogram.types import Message
from config import TG_TOKEN, ADMIN_ID
from request_price_stock import get_stock_info, get_commodites
from keyboard import start_keyboard, product_keyboard, stocks_keyboard


@dp.message_handler(commands=['start'])
async def start(message):
    text = 'Приветствую. Выберите эшелон акций'
    await message.answer(text=text, reply_markup=start_keyboard())

@dp.message_handler(commands=['акции'])
async def commodites(message):
    text = 'Выберите акцию или напишете ее тикер'
    await message.answer(text=text, reply_markup=stocks_keyboard())

@dp.message_handler(commands=['товары'])
async def commodites(message):
    text = 'Выберите товар'
    await message.answer(text=text, reply_markup=product_keyboard())

@dp.message_handler(commands=['нефть brent', 'нефть WTI', 'натуральный газ', 'серебро', 'золото', 'палладий'])
async def view_product(message):
    ['GC=F', 'BZ=F', 'MCL=F', 'SI=F', 'NG=F', 'PA=F']
    commodites = {
        '/золото' : 'GC=F',
        '/нефть brent' : 'BZ=F',
        '/нефть WTI' : 'MCL=F',
        '/серебро' : 'SI=F',
        '/натуральный газ' : 'NG=F',
        '/палладий' : 'PA=F',
    }
    text = get_commodites(commodites[message.text])
    await message.answer(text=text, reply_markup=product_keyboard())

# @dp.message_handler(commands=['нефть brent', 'нефть WTI', 'натуральный газ', 'серебро', 'золото', 'палладий'])
# async def view_product(message):
#     blue_stoks = ['SBER', 'GAZP', 'LKOH', 'YANDX', 'GMKN', 'NVTK', 'TATNP', 'MOEX', 'VTBR', 'SNGS', 'ALRS']
#     commodites = {
#         '/золото' : 'GC=F',
#         '/нефть brent' : 'BZ=F',
#         '/нефть WTI' : 'MCL=F',
#         '/серебро' : 'SI=F',
#         '/натуральный газ' : 'NG=F',
#         '/палладий' : 'PA=F',
#     }
#     text = get_commodites(commodites[message.text])
#     await message.answer(text=text, reply_markup=product_keyboard())