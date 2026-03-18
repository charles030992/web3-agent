from tools.wallet_tools import get_wallet_balance
from tools.market_tools import get_eth_price_usd


def wallet_summary(address: str, simulate: bool = True) -> dict:
    balance = get_wallet_balance(address, simulate=simulate)
    price = get_eth_price_usd()

    return {
        "address": address,
        "balance": balance,
        "eth_price_usd": price,
        "note": "Resumen básico. Próximo paso: transacciones reales y PnL.",
    }