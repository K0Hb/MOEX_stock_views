import yfinance as yf
import requests

def yahoo_get_api(ticker):
    url = f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price'
    headers = 'Mozilla/5.0 '
    session = requests.session()
    response = session.get(url, headers={'User-Agent': headers})
    result = dict(response.json())
    data = result['quoteSummary']['result'][0]['price']
    procent = data['regularMarketChangePercent']['fmt']
    price = data['regularMarketPrice']['fmt']
    open_price = data['regularMarketOpen']['fmt']
    hi_day = data['regularMarketDayHigh']['fmt']
    low_day = data['regularMarketDayLow']['fmt']
    close_price = data['regularMarketPreviousClose']['fmt']
    ticker_ = data['symbol']
    name = data['shortName']
    valute = data['currency']
    trend = '📈'
    if float(procent[0:3]) < 0:
        trend = '📉'
    data_dict = {
        'Название' : name,
        'Тикер' : ticker_,
        'Цена в' : valute,
        'Цена' : f'{price} {trend} {procent}',
        'Дневной диапозон' : f'{low_day} - {hi_day}',
        'Открытие' : open_price,
        'Пред. закр' : close_price,
    }
    return data_dict

def get_stock_info(stock_ticker):
    all_rus_stocks = ['SBER', 'GAZP', 'LKOH', 'YANDX', 'GMKN', 'MTSS', 'ALRS', 'NLMK',
                        'MAGN', 'VTBR', 'OZON', 'POLY', 'TCSG', 'SBERP', 'VKCO', 'MOEX', 'CHMF', 'ROSN', 
                        'AFLT', 'NVTK', 'TATN', 'PLZL', 'DSKY', 'FIVE', 'AFKS', 'RUAL', 'MTLP', 'MVID', 'PHOR', 
                        'IRAO', 'SHGSP', 'PIKK', 'SIBM', 'SNGS', 'FEES', 'AGRO', 'RASP', 'SGZH', 'HYDR', 'RSTI',
                        'TATNP', 'GLTR', 'FIXP', 'POGR', 'BANEP', 'RTKM', 'AKRN', 'MTLRP', 'SNGSP']

    blue_stoks = ['SBER', 'GAZP', 'LKOH', 'YANDX', 'GMKN', 'NVTK', 'TATNP', 'MOEX', 'VTBR', 'SNGS', 'ALRS']
    result = yahoo_get_api(stock_ticker + '.ME')
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view

def get_commodites(product_ticker):
    result = yahoo_get_api(product_ticker)
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view

def get_index(index_ticker):
    result = yahoo_get_api(index_ticker)
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view
