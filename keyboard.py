from binascii import b2a_base64
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def start_keyboard():
    b1 = KeyboardButton('/индексы')
    b2 = KeyboardButton('/акции')
    b3 = KeyboardButton('/иностранные акции')
    b4 = KeyboardButton('/товары')

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(b1).add(b2).add(b3).add(b4)
    return kb

def product_keyboard():
    b1 = KeyboardButton('/нефть brent')
    b2 = KeyboardButton('/нефть WTI')
    b3 = KeyboardButton('/натуральный газ')
    b4 = KeyboardButton('/серебро')
    b5 = KeyboardButton('/палладий')
    b6 = KeyboardButton('/золото')
    buttons = [b1, b2, b3, b4, b5, b6]
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for but in buttons:
        kb.add(but)
    return kb

def stocks_keyboard():
    buttons = ['/сбер', '/газпром', '/лукойл', '/яндекс', '/норильский никель', '/новатэк', '/татнефть', '/мосбиржа', '/втб', '/сургутнефтегаз', '/алроса']
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for but in buttons:
        kb.add(KeyboardButton(but))
    return kb