import requests

def get_exchange_rate(from_currency, to_currency):
    """
    Fetches real-time currency exchange rates using the open.er-api.com service.
    """
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rate. Check your internet connection.")

    data = response.json()
    if data.get("result") != "success":
        raise Exception("Invalid currency or API issue.")

    rates = data.get("rates", {})
    if to_currency not in rates:
        raise Exception(f"Currency '{to_currency}' not found in exchange rates.")

    return rates[to_currency]
