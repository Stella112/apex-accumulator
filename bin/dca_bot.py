#!/usr/bin/env python3
import json
import urllib.parse
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API_KEYS_PATH = 'secrets/binance_main.key'
ASSET_SYMBOL = 'BTCUSDT'
ASSET_NAME = 'BTC'
RSI_PERIOD = 14
DIP_THRESHOLD_PERCENT = 3.0

with open(API_KEYS_PATH) as f:
    api_key = f.readline().strip()
    secret = f.readline().strip()  # Unused for public endpoints but kept for parity/logging


def get_klines(symbol, interval='1h', limit=200):
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit,
    }
    query_string = urllib.parse.urlencode(params)
    url = f'https://api.binance.com/api/v3/klines?{query_string}'
    req = Request(url)
    req.add_header('X-MBX-APIKEY', api_key)
    return json.loads(urlopen(req).read().decode())


def calculate_rsi(closes, period=RSI_PERIOD):
    if len(closes) < period + 1:
        raise ValueError('Not enough data to compute RSI')

    gains = []
    losses = []
    for i in range(-period, 0):
        delta = closes[i] - closes[i - 1]
        if delta >= 0:
            gains.append(delta)
        else:
            losses.append(abs(delta))

    average_gain = sum(gains) / period if gains else 0
    average_loss = sum(losses) / period if losses else 0

    if average_loss == 0:
        return 100.0

    rs = average_gain / average_loss
    return 100 - (100 / (1 + rs))


def get_dip_percentage(closes):
    if len(closes) < 2:
        raise ValueError('Need at least two closes to compute dip percentage')
    previous_close = closes[-2]
    last_close = closes[-1]
    dip_pct = ((previous_close - last_close) / previous_close) * 100
    return dip_pct


if __name__ == '__main__':
    try:
        klines = get_klines(ASSET_SYMBOL)
        closes = [float(entry[4]) for entry in klines]
        rsi_value = calculate_rsi(closes)
        dip_pct = get_dip_percentage(closes)

        if dip_pct >= DIP_THRESHOLD_PERCENT:
            print(
                f"{ASSET_NAME} dipped {dip_pct:.2f}% (RSI: {rsi_value:.2f}). Executing your weekly $100 DCA paper-trade now for a better entry."
            )
        else:
            print(
                f"No 3% dip yet for {ASSET_NAME} (latest move: {dip_pct:.2f}%, RSI: {rsi_value:.2f}). Holding fire on the weekly $100 DCA trigger."
            )
    except HTTPError as e:
        print(f'Error fetching klines: {e}')
    except ValueError as ve:
        print(f'Calculation error: {ve}')
