import robin_stocks.robinhood as robin
import pyotp

def login():
    lines = open("E:/Robinhood_Trading/account.txt").read().splitlines()

    KEY = lines[0]
    EMAIL = lines[1]
    PASSWD = lines[2]
    CODE = lines[3]

    totp = pyotp.TOTP(KEY).now()
    login = robin.login(EMAIL, PASSWD, mfa_code=totp)
