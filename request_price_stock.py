import yfinance as yf

all_rus_stocks = ['SBER.ME', 'GAZP.ME', 'LKOH.ME', 'YANDX.ME', 'GMKN.ME', 'MTSS.ME', 'ALRS.ME', 'NLMK.ME', 'MAGN.ME']

def get_stock_info(stock_ticker):
    stock = yf.Ticker(stock_ticker)
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
    return result
