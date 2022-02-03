from binascii import b2a_base64
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start_buttons = ['/индексы', '/акции', '/иностранные_акции', '/товары']
commodites_buttons = ['/нефть_brent', '/нефть_WTI', '/натуральный_газ', '/серебро', '/палладий', '/золото']
stocks_buttons = ['/сбер', '/газпром', '/лукойл', '/яндекс', '/норильский_никель', '/новатэк', '/татнефть', '/мосбиржа', '/втб', '/сургутнефтегаз', '/алроса']

dict_list_but = {
    'старт' : start_buttons,
    'товары' : commodites_buttons,
    'акции' : stocks_buttons,
}
dict_list_stocks = {
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

def generate_keyboard(buttons_name=None):
    buttons_list = dict_list_but[buttons_name]
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    if len(buttons_list) < 5:
        for but in buttons_list:
            kb.add(KeyboardButton(but))
    else:
        count = 0
        for but in buttons_list:
            count += 1
            print(count)
            if count == 1:
                kb.add(KeyboardButton(but))
            elif count < 4:
                kb.insert(KeyboardButton(but))
            else:
                count = 1
                kb.add(KeyboardButton(but))
    return kb
