import requests

def binance_error_dict(no):
    if no == "429":
        print("İstek zamanı geçti")
        print("HTTP 429 return code is used when breaking a request rate limit.")
    elif no == "418":
        print("Çok sayıda istek gönderildiğinden ip geçici olarak banlanmıştır")
        print("HTTP 418 return code is used when an IP has been auto-banned for continuing to send requests after receiving 429 codes.")
    elif no == "504":
        print("İstek başarıyla gönderildi fakat cevap alınamadı")
        print('''HTTP 504 return code is used when the API successfully sent the message but not get a response within the timeout period.
        \nIt is important to NOT treat this as a failure; the execution status is UNKNOWN and could have been a success.''')
    elif no[0] == "4":
        print("Api kullanımında hata")
        print("HTTP 4XX return codes are used for for malformed requests; the issue is on the sender's side.")
    elif no[0] == "4":
        print("Binance server hatası")
        print("HTTP 5XX return codes are used for internal errors; the issue is on Binance's side.")

def get_depth(symbol,limit="10"):#ORDER BOOK
    r = requests.get('https://api.binance.com/api/v1/depth', "symbol={0}&limit={1}".format(symbol,limit))
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_ping():
    r = requests.get('https://api.binance.com/api/v1/ping')
    if r.status_code == 200:
        return r.text
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_server_time():
    r = requests.get('https://api.binance.com/api/v1/time')
    if r.status_code == 200:
        return r.text()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_exchange_info():
    r = requests.get('https://api.binance.com/api/v1/exchangeInfo')
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_recent_trades(symbol,limit=100):#öntanımlı olarak 500 yerine 100 yaptım.
    r = requests.get('https://api.binance.com/api/v1/trades', "symbol={0}&limit={1}".format(symbol, limit))
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_klines(symbol,interval="1m",limit=5,time=None):
    if time is None:
        r = requests.get('https://api.binance.com/api/v1/depth', "symbol={0}&interval={1}&limit={2}".format(symbol,interval,limit))
        if r.status_code == 200:
            return r.json()
        else:
            binance_error_dict(r.status_code)
            return "Bir hata oluştu"
    else:
        r = requests.get('https://api.binance.com/api/v1/depth', "symbol={0}&interval={1}&limit={2}&startTime={3}&endTime={4}".format(symbol, interval, limit,time[0],time[1]))
        if r.status_code == 200:
            return r.json()
        else:
            binance_error_dict(r.status_code)
            return "Bir hata oluştu"

def get_ticker_price_for24hour_withsymbol(symbol):
    r = requests.get('https://api.binance.com/api/v1/ticker/24hr', "symbol={0}".format(symbol))
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_ticker_price_for24hour_withoutsymbol():
    r = requests.get('https://api.binance.com/api/v1/ticker/24hr')
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_symbol_price_withsymbol(symbol):
    r = requests.get('https://api.binance.com/api/v1/ticker/price', "symbol={0}".format(symbol))
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_symbol_price_withoutsymbol():
    r = requests.get('https://api.binance.com/api/v1/ticker/price')
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"

def get_symbol_orderbook_ticker_withsymbol(symbol):
    r = requests.get('https://api.binance.com/api/v1/ticker/bookTicker', "symbol={0}".format(symbol))
    if r.status_code == 200:
        return r.json()
    else:
        binance_error_dict(r.status_code)
        return "Bir hata oluştu"
