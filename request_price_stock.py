import yfinance as yf


def get_stock_info(stock_ticker):
    all_rus_stocks = ['SBER', 'GAZP', 'LKOH', 'YANDX', 'GMKN', 'MTSS', 'ALRS', 'NLMK',
                        'MAGN', 'VTBR', 'OZON', 'POLY', 'TCSG', 'SBERP', 'VKCO', 'MOEX', 'CHMF', 'ROSN', 
                        'AFLT', 'NVTK', 'TATN', 'PLZL', 'DSKY', 'FIVE', 'AFKS', 'RUAL', 'MTLP', 'MVID', 'PHOR', 
                        'IRAO', 'SHGSP', 'PIKK', 'SIBM', 'SNGS', 'FEES', 'AGRO', 'RASP', 'SGZH', 'HYDR', 'RSTI',
                        'TATNP', 'GLTR', 'FIXP', 'POGR', 'BANEP', 'RTKM', 'AKRN', 'MTLRP', 'SNGSP']

    blue_stoks = ['SBER', 'GAZP', 'LKOH', 'YANDX', 'GMKN', 'NVTK', 'TATNP', 'MOEX', 'VTBR', 'SNGS', 'ALRS']

    stock = yf.Ticker(stock_ticker + '.ME')
    sector = stock.info['sector']
    price = stock.info['regularMarketPrice']
    last_divident = stock.info['lastDividendValue']
    day_50 = stock.info['fiftyDayAverage']
    open_price = stock.info['open']
    marketCap = stock.info['marketCap']
    daylow = stock.info['dayLow']
    dayhigh = stock.info['dayHigh']
    hi_52 = stock.info['fiftyTwoWeekHigh']
    middle_52 = stock.info['fiftyDayAverage']
    low_52 = stock.info['fiftyTwoWeekLow']
    divident = stock.info['dividendRate']
    last_price_close = stock.info['previousClose']
    procent = round((price - last_price_close)/ price * 100, 2)
    result = {
        'тикер' : stock_ticker,
        'сектор' : sector,
        'капитализация' : marketCap,
        'цена' : price,
        'процент изменения' : procent,
        'цена последнего закрытия' : last_price_close,
        'цена открытия денвной сессии' : open_price,
        'дневной максимум' : dayhigh,
        'дневной минимум' : daylow,
        '50 дневная средняя' : day_50,
        '52 дневный максимум' : hi_52,
        '52 дневная средняя' : middle_52,
        '52 дневный минимум' : low_52,
        'Размер последнего дивиденда на одну акцию' : last_divident,
        'Размер дивиденда на одну акцию' : divident,
        }
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view

def get_commodites(product_ticker):
    products = ['GC=F', 'BZ=F', 'MCL=F', 'SI=F', 'NG=F', 'PA=F']
    product = yf.Ticker(product_ticker)
    daylow = product.info['dayLow']
    dayhigh = product.info['dayHigh']
    open_price = product.info['regularMarketOpen']
    price = product.info['regularMarketPrice']
    procent = round((price - open_price)/ price * 100, 2)
    name = product.info['shortName']
    result = {
        'название' : name,
        'цена' : price,
        'процент изменения' : procent,
        'цена открытия денвной сессии' : open_price,
        'дневной максимум' : dayhigh,
        'дневной минимум' : daylow,
        }
    string_view = ''
    for key in result:
        string_view += f'{key} : {result[key]}\n' 
    return string_view



print(get_commodites('NG=F'))