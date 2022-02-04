from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_buttons = ['/индексы', '/акции', '/валютные_пары', '/товары']
commodites_buttons = ['/нефть_brent', '/нефть_WTI', '/натуральный_газ',
                      '/серебро', '/палладий', '/золото']
stocks_buttons = ['/сбер', '/газпром', '/лукойл', '/яндекс',
                  '/норильский_никель', '/новатэк', '/татнефть',
                  '/мосбиржа', '/втб', '/сургутнефтегаз', '/алроса']
indexs_buttons = ['/РТС', '/Мосбиржа_индекс', '/SP500', '/NASDAQ', '/DJI',
                  '/DAX', '/IBOVESPA', '/KOSPI', '/Nikkei']
currencies_buttons = ['/USD/RUB', '/EUR/RUB', '/RUB/CNY', '/EUR/USD',
                      '/USD/JPY', '/USD/CNY', '/BTC/USD']

dict_list_but = {
    'старт': start_buttons,
    'товары': commodites_buttons,
    'акции': stocks_buttons,
    'индексы': indexs_buttons,
    'валютные_пары': currencies_buttons,
}


def generate_keyboard(buttons_name=None, back=False):  # noqa
    buttons_list = dict_list_but[buttons_name]
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    if back:
        kb.add(KeyboardButton('/вернуться'))
    if len(buttons_list) < 5:
        for but in buttons_list:
            kb.add(KeyboardButton(but))
    else:
        count = 0
        for but in buttons_list:
            count += 1
            if count == 1:
                kb.add(KeyboardButton(but))
            elif count < 4:
                kb.insert(KeyboardButton(but))
            else:
                count = 1
                kb.add(KeyboardButton(but))
    return kb
