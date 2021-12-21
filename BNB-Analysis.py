import pandas
import yfinance as yf
import ccxt
import pandas as pd
import pandas_ta as ta

exchange = ccxt.binance()
#Pulls in Etherum data from binance
crypto = exchange.fetch_ohlcv(symbol='BNBUSDT',timeframe='5m',limit=500)
#Sorts it into a nicer format before we use pandas-ta
df = pandas.DataFrame(crypto, columns=['Time','Open','High','Low','Close','Volume'])
#adx = ta.adx(df['High'],df['Low'],df['Close'])
adx = df.ta.adx()
macd = df.ta.macd()
rsi = df.ta.rsi()

df = pd.concat([df, adx, macd, rsi], axis=1)


last_row = df.iloc[-1]
print(last_row)
if last_row['ADX_14'] >= 25:
    message = f"STRONG TREND: ADX_14 is trending - ADX Value: {last_row['ADX_14']:.2f}"
    print(message)
if last_row['ADX_14'] < 25:
    message2 = f"NO Trend: ADX value is : {last_row['ADX_14']:.2f}"
    print(message2)


if last_row['DMP_14'] > last_row['DMN_14']:
    print(f"UP-TREND - Potenitial Buy Signal")
if last_row['DMP_14'] < last_row['DMN_14']:
    print(f"DOWN--TREND")