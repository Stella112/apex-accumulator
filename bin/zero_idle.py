#!/usr/bin/env python3
import time, hmac, hashlib, urllib.parse, json
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# Configuration
API_KEY_PATH = 'secrets/binance_main.key'

# Load API Keys
with open(API_KEY_PATH) as f:
    api_key = f.readline().strip()
    secret = f.readline().strip()

# Binance Earn parameters
EARN_URL = 'https://api.binance.com/sapi/v1/simple-earn/flexible/list'

ASSETS_TO_MONITOR = {
    'USDT': {'price_symbol': None},
    'BNB': {'price_symbol': 'BNBUSDT'},
}

# Function to get spot balances
def get_spot_balances():
    params = {
        'timestamp': int(time.time() * 1000),
        'recvWindow': 5000,
    }
    query_string = urllib.parse.urlencode(params)
    signature = hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    url = f'https://api.binance.com/api/v3/account?{query_string}&signature={signature}'
    req = Request(url)
    req.add_header('X-MBX-APIKEY', api_key)
    return json.loads(urlopen(req).read().decode())

# Function to get flexible earn products
def get_flexible_earn_products():
    params = {
        'page': 1,
        'size': 20,
        'type': 'FLEXIBLE',
        'recvWindow': 5000,
        'timestamp': int(time.time() * 1000),
    }
    query_string = urllib.parse.urlencode(params)
    signature = hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    url = f'{EARN_URL}?{query_string}&signature={signature}'
    req = Request(url)
    req.add_header('X-MBX-APIKEY', api_key)
    return json.loads(urlopen(req).read().decode())


def get_symbol_price(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    req = Request(url)
    data = json.loads(urlopen(req).read().decode())
    return float(data['price'])


def find_best_apr(products, asset):
    for row in products.get('rows', []):
        if row.get('asset') != asset:
            continue
        rates = []
        latest_rate = row.get('latestAnnualPercentageRate')
        if latest_rate is not None:
            rates.append(float(latest_rate))
        tier_rates = row.get('tierAnnualPercentageRate') or {}
        for value in tier_rates.values():
            rates.append(float(value))
        if rates:
            return max(rates)
    return None


# Main execution logic
if __name__ == '__main__':
    try:
        balances = get_spot_balances()['balances']
        balance_map = {b['asset']: float(b['free']) for b in balances}
        earn_products = get_flexible_earn_products()

        alerts = []
        for asset, config in ASSETS_TO_MONITOR.items():
            idle_amount = balance_map.get(asset, 0.0)
            if idle_amount <= 0:
                continue

            usd_value = idle_amount
            price_symbol = config.get('price_symbol')
            if price_symbol:
                usd_value = idle_amount * get_symbol_price(price_symbol)

            best_rate = find_best_apr(earn_products, asset)
            if best_rate is None:
                continue

            alerts.append(
                f"You have ${usd_value:.2f} in idle {asset}. I found a {best_rate * 100:.2f}% APR Flexible Earn for it."
            )

        if alerts:
            for alert in alerts:
                print(alert)
        else:
            print('No idle USDT/BNB balances or matching Flexible Earn offers found.')
    except HTTPError as e:
        print(f'Error fetching data: {e}')
