from typing import Any, Callable, Dict
from tools.wallet_tools import get_wallet_balance
from tools.market_tools import get_eth_price_usd
from tools.math_tools import multiply_numbers

# Catálogo de herramientas (nombre -> función)
TOOLS: Dict[str, Callable[..., Any]] = {
    "get_wallet_balance": get_wallet_balance,
    "get_eth_price_usd": get_eth_price_usd,
    "multiply_numbers": multiply_numbers,

}

# (Opcional, pero útil) Descripción para humanos/LLM
TOOL_DESCRIPTIONS = {
    "get_wallet_balance": {
        "description": "Devuelve el balance (simulado por ahora) de una wallet.",
        "args": {"address": "str", "simulate": "bool"},
        "returns": "str",
    },
    "get_eth_price_usd": {
        "description": "Devuelve el precio actual de ETH en USD (CoinGecko).",
        "args": {},
        "returns": "float",
    },
    "multiply_numbers": {
    "description": "Multiply two numbers and return the result.",
    "args": {"a": "float", "b": "float"},
    "returns": "float",
    },
}