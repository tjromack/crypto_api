def transform_data(data):
    prices = {}
    market_caps = {}
    changes = {}

    for coin in data:
        prices[coin] = data[coin]['usd']
        market_caps[coin] = data[coin]['usd_market_cap']
        changes[coin] = data[coin]['usd_24h_change']

    return prices, market_caps, changes
