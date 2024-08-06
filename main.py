import yfinance as yf
import json

ebnk = yf.Ticker("EQUITASBNK.NS")

info = ebnk.info

print(info)
