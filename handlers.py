from bot_v2 import bot, dp
from aiogram.types import Message
from request_price_stock import get_commodites, get_stock_info
from keyboard import generate_keyboard

stocks = {
        '/сбер' : 'SBER',
        '/газпром' : 'GAZP',
        '/лукойл' : 'LKOH',
        '/яндекс' : 'YANDX',
        '/норильский_никель' : 'GMKN',
        '/новатэк' : 'NVTK',
        '/татнефть' : 'TATNP',
        '/мосбиржа' : 'MOEX',
        '/втб' : 'VTBR',
        '/сургутнефтегаз' : 'SNGS',
        '/алроса' : 'ALRS',
        }
commodites = {
        '/золото' : 'GC=F',
        '/нефть_brent' : 'BZ=F',
        '/нефть_WTI' : 'MCL=F',
        '/серебро' : 'SI=F',
        '/натуральный_газ' : 'NG=F',
        '/палладий' : 'PA=F',
        }

@dp.message_handler(commands=['старт'])
async def start(message):
    text = 'Приветствую. Выберите эшелон акций'
    await message.answer(text=text, reply_markup=generate_keyboard('старт'))

@dp.message_handler(commands=['акции'])
async def commodites(message):
    text = 'Выберите акцию или напишете ее тикер'
    await message.answer(text=text, reply_markup=generate_keyboard('акции'))

@dp.message_handler(commands=['товары'])
async def commodites(message):
    text = 'Выберите товар'
    await message.answer(text=text, reply_markup=generate_keyboard('товары'))

@dp.message_handler(commands=['нефть_brent', 'нефть_WTI', 'натуральный_газ', 'серебро', 'золото', 'палладий'])
async def view_product(message):
    text = get_commodites(commodites[message.text])
    await message.answer(text=text, reply_markup=generate_keyboard('товары'))

@dp.message_handler(commands=['сбер', 'газпром', 'лукойл', 'яндекс', 'норильский_никель', 'новатэк', 'татнефть', 'мосбиржа', 'втб', 'сургутнефтегаз', 'алроса'])
async def view_product(message):
    text = get_stock_info(stocks[message.text])
    await message.answer(text=text)