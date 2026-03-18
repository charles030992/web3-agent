from tools.wallet_tools import get_wallet_balance
from tools.market_tools import get_eth_price_usd


def analyze_wallet(address: str, *, simulate: bool = True) -> dict:
    balance_str = get_wallet_balance(address, simulate=simulate)
    eth_price = get_eth_price_usd()

    return {
        "address": address,
        "balance": balance_str,
        "eth_price_usd": eth_price,
        "mode": "SIMULATED" if simulate else "REAL",
    }