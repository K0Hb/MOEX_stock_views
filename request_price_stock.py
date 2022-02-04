import yfinance as yf
import requests

def yahoo_get_api(ticker):
    url = f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price'
    headers = 'Mozilla/5.0 '
    session = requests.session()
    response = session.get(url, headers={'User-Agent': headers})
    result = dict(response.json())
    return result

def genearate_view(data_dict):
    data = data_dict['quoteSummary']['result'][0]['price']
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
    print(float(procent[0:3]))
    if float(procent[0:6]) < 0:
        trend = '📉'
    result_dict = {
        'Название' : name,
        'Тикер' : ticker_,
        'Цена в' : valute,
        'Цена' : f'{price} {trend} {procent}',
        'Дневной диапозон' : f'{low_day} - {hi_day}',
        'Открытие' : open_price,
        'Пред. закр' : close_price,
    }
    return result_dict

def get_stock_info(stock_ticker):
    all_rus_stocks = ['SBER', 'GAZP', 'LKOH', 'YANDX', 'GMKN', 'MTSS', 'ALRS', 'NLMK',
                        'MAGN', 'VTBR', 'OZON', 'POLY', 'TCSG', 'SBERP', 'VKCO', 'MOEX', 'CHMF', 'ROSN', 
                        'AFLT', 'NVTK', 'TATN', 'PLZL', 'DSKY', 'FIVE', 'AFKS', 'RUAL', 'MTLP', 'MVID', 'PHOR', 
                        'IRAO', 'SHGSP', 'PIKK', 'SIBM', 'SNGS', 'FEES', 'AGRO', 'RASP', 'SGZH', 'HYDR', 'RSTI',
                        'TATNP', 'GLTR', 'FIXP', 'POGR', 'BANEP', 'RTKM', 'AKRN', 'MTLRP', 'SNGSP']

    blue_stoks = ['SBER', 'GAZP', 'LKOH', 'YANDX', 'GMKN', 'NVTK', 'TATNP', 'MOEX', 'VTBR', 'SNGS', 'ALRS']
    yahoo_info = yahoo_get_api(stock_ticker + '.ME')
    result = genearate_view(yahoo_info)
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view

def get_commodites(product_ticker):
    yahoo_info = yahoo_get_api(product_ticker)
    result = genearate_view(yahoo_info)
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view

def get_index(index_ticker):
    yahoo_info = yahoo_get_api(index_ticker)
    result = genearate_view(yahoo_info)
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view

def general_sentiment():
    sentiment = {
        'РТС' : 'RTSI.ME',
        'Индекс Мосбиржи' : 'IMOEX.ME',
        'USD/RUB' : 'RUB=X',
        'EUR/RUB' : 'EURRUB=X',
        'Нефть brent' : 'BZ=F',
        'Золото' : 'GC=F',
        'SP500' : '^GSPC',
        'BTC/USD' : 'BTC-USD',
    }
    result = 'Рыночный сентимент:\n'
    for name, ticker in sentiment.items():
        yaho_dict = yahoo_get_api(ticker)['quoteSummary']['result'][0]['price']
        price = yaho_dict['regularMarketPrice']['fmt']
        procent = yaho_dict['regularMarketChangePercent']['fmt']
        trend = '📈'
        if float(procent[0:6]) < 0:
            trend = '📉'
        result += f'{name} : {procent} {trend}\n'
    return result
