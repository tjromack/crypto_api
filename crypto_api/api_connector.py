import requests

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    parameters = {
        "ids": "bitcoin,ethereum,binancecoin,cardano,ripple",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_change": "true"
    }

    response = requests.get(url, params=parameters)
    
    if response.status_code != 200:
        raise Exception(f"Error: Unable to fetch data from CoinGecko. HTTP Status Code: {response.status_code}")

    return response.json()

# You can add other functions or logic as needed

