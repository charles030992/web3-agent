from tools.market_tools import get_eth_price_usd
from tools.math_tools import multiply_numbers
from services.parsers import extract_eth_amount


def extract_amount_step(state):
    state.amount = extract_eth_amount(state.user_query)
    return state


def get_price_step(state):
    if state.eth_price is None:
        state.eth_price = get_eth_price_usd()
    return state


def calculate_step(state):
    if state.result is None and state.amount is not None and state.eth_price is not None:
        state.result = multiply_numbers(state.amount, state.eth_price)
    return state


def generate_response_step(state, ask_llm, tools):
    final_prompt = (
        f"The user asked: {state.user_query}. "
        f"The result is: {state.amount} ETH = ${state.result:.2f} USD. "
        f"Respond clearly."
    )

    messages = [{"role": "user", "content": final_prompt}]
    response = ask_llm(messages, tools)

    return response["message"].get(
        "content",
        f"{state.amount} ETH = ${state.result:.2f} USD"
    )