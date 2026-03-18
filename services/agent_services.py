from services.llm_services import ask_llm
from services.tool_schema import tools
from tools.market_tools import get_eth_price_usd
from tools.wallet_tools import get_wallet_balance
import re
from tools.math_tools import multiply_numbers


def extract_eth_amount(text):
    m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*ETH", text, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def run_agent(query):
    messages = [
        {"role": "user", "content": query}
    ]

    max_steps = 5
    step = 0
    last_tool_name = None
    eth_amount = extract_eth_amount(query)
    last_price = None
    used_multiply = False

    while step < max_steps:
        step += 1

        response = ask_llm(messages, tools)
        message = response["message"]

        if "tool_calls" in message:
            print("\n--- NEW LOOP ---")
            print("Model message:", message)

            tool_call = message["tool_calls"][0]
            name = tool_call["function"]["name"]
            args = tool_call["function"]["arguments"]

            if name == last_tool_name:
                return f"Agent stopped: repeated tool call detected ({name})"

            if name == "get_eth_price":
                result = get_eth_price_usd()
                last_price = result
            elif name == "get_wallet_balance":
                result = get_wallet_balance(args.get("address"))
            elif name == "multiply_numbers":
                result = multiply_numbers(args.get("a"), args.get("b"))
                used_multiply = True
            else:
                result = "Unknown tool"

            print(f"Tool selected: {name}")
            print(f"Arguments: {args}")
            print(f"Tool result: {result}")

            last_tool_name = name

            messages.append(message)
            messages.append({
                "role": "function",
                "name": name,
                "content": f"{result}"
            })
            if name == "get_eth_price" and eth_amount is not None:
                messages.append({
                    "role": "user",
                    "content": (
                        f"The question is: {query}. You got ETH price {result}. "
                        f"Now calculate {eth_amount} ETH in USD using multiply_numbers(a={eth_amount}, b={result})."
                    )
                })
            else:
                messages.append({
                    "role": "user",
                    "content": "Continue solving the original question. If a calculation is needed, use the multiply_numbers tool."
                })

        else:
            # Fallback: si el modelo no hace segunda tool call, hacemos el cálculo final
            if (
                last_tool_name == "get_eth_price"
                and eth_amount is not None
                and last_price is not None
                and not used_multiply
            ):
                final_value = multiply_numbers(eth_amount, last_price)
                return f"{eth_amount} ETH is ${final_value:.2f} USD (calculated with multiply_numbers)."
            return message.get("content", "") or "Agent finished without content."

    return "Agent stopped: max steps reached."