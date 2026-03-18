import requests


def get_eth_price_usd() -> float:
    """
    Precio de ETH en USD usando CoinGecko (sin API key).
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "ethereum", "vs_currencies": "usd"}

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        return float(data["ethereum"]["usd"])
    except Exception as e:
        # En producción haríamos logging estructurado; por ahora simple.
        raise RuntimeError(f"Error obteniendo precio ETH: {e}")