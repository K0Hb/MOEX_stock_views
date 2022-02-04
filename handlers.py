from bot_v2 import bot, dp
from aiogram.types import Message
from request_price_stock import get_commodites, get_stock_info, get_index, general_sentiment
from keyboard import generate_keyboard

stocks = {
        '/сбер' : 'SBER',
        '/газпром' : 'GAZP',
        '/лукойл' : 'LKOH',
        '/яндекс' : 'YNDX',
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
indexs = {
    '/РТС' : 'RTSI.ME',
    '/Мосбиржа_индекс' : 'IMOEX.ME',
    '/SP500' : '^GSPC',
    '/NASDAQ' : '^IXIC',
    '/DJI' : '^DJI',
    '/DAX' : '^GDAXI',
    '/IBOVESPA' : 'IBV=F',
    '/KOSPI' : '^KS11',
    '/Nikkei' : '^N225',
}
currencies = {
    '/USD/RUB' : 'RUB=X',
    '/EUR/RUB' : 'EURRUB=X',
    '/RUB/CNY' : 'RUBCNY=X',
    '/EUR/USD' : 'EURUSD=X',
    '/USD/JPY' : 'JPY=X',
    '/USD/CNY' : 'CNY=X',
    '/BTC/USD' : 'BTC-USD'
}


@dp.message_handler(commands=['старт', 'вернуться'])
async def start(message):
    text = general_sentiment()
    await message.answer(text=text, reply_markup=generate_keyboard('старт'))

@dp.message_handler(commands=['акции'])
async def stocks_view(message):
    text = 'Выберите акцию или напишете ее тикер'
    await message.answer(text=text, reply_markup=generate_keyboard('акции',True))

@dp.message_handler(commands=['товары'])
async def commodites_view(message):
    text = 'Выберите товар'
    await message.answer(text=text, reply_markup=generate_keyboard('товары',True))

@dp.message_handler(commands=['индексы'])
async def indexes_view(message):
    text = 'Выберите индекс'
    await message.answer(text=text, reply_markup=generate_keyboard('индексы',True))

@dp.message_handler(commands=['валютные_пары'])
async def currencies_view(message):
    text = 'Выберите валютную пару'
    await message.answer(text=text, reply_markup=generate_keyboard('валютные_пары',True))

@dp.message_handler(commands=['нефть_brent', 'нефть_WTI', 'натуральный_газ', 'серебро', 'золото', 'палладий'])
async def view_product(message):
    text = get_commodites(commodites[message.text])
    await message.answer(text=text)

@dp.message_handler(commands=['сбер', 'газпром', 'лукойл', 'яндекс', 'норильский_никель', 'новатэк', 'татнефть', 'мосбиржа', 'втб', 'сургутнефтегаз', 'алроса'])
async def view_stock(message):
    text = get_stock_info(stocks[message.text])
    await message.answer(text=text)

@dp.message_handler(commands=['РТС', 'Мосбиржа_индекс', 'SP500', 'NASDAQ', 'DJI', 'DAX', 'IBOVESPA', 'KOSPI', 'Nikkei'])
async def view_index(message):
    text = get_index(indexs[message.text])
    await message.answer(text=text)

@dp.message_handler(commands=['USD/RUB', 'EUR/RUB', 'RUB/CNY', 'EUR/USD', 'USD/JPY', 'USD/CNY', 'BTC/USD'])
async def view_currency(message):
    text = get_index(currencies[message.text])
    await message.answer(text=text)