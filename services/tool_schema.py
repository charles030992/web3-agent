tools = [
    {
        "type": "function",
        "function": {
            "name": "get_eth_price",
            "description": "Get current Ethereum price in USD",
            "parameters": {
                "type": "object",
                "properties": {},
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_wallet_balance",
            "description": "Get Ethereum balance of a wallet address",
            "parameters": {
                "type": "object",
                "properties": {
                    "address": {
                        "type": "string"
                    }
                },
                "required": ["address"]
            }
        }
    }
]