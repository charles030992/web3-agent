from services.llm_services import ask_llm
from services.tool_schema import tools
from tools.market_tools import get_eth_price_usd
from tools.wallet_tools import get_wallet_balance
import re
from tools.math_tools import multiply_numbers
from services.state import AgentState


def extract_eth_amount(text):
    m = re.search(r"([0-9]+(?:\.[0-9]+)?)\s*ETH", text, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def run_agent(query):
    state = AgentState(query)
    state.amount = extract_eth_amount(query)

    # Validación inicial
    if state.amount is None:
        return "Could not extract ETH amount from query."

    # LOOP controlado por backend
    while not state.reached_limit():
        state.increment_step()

        print(f"\n--- STEP {state.step_count} ---")
        print(f"STATE: amount={state.amount}, price={state.eth_price}, result={state.result}")

        # 1. Obtener precio si falta
        if state.eth_price is None:
            print("→ Getting ETH price...")
            price = get_eth_price_usd()
            state.eth_price = price
            continue

        # 2. Calcular resultado si falta
        if state.result is None:
            print("→ Calculating result...")
            result = multiply_numbers(state.amount, state.eth_price)
            state.result = result
            continue

        # 3. Si todo está listo → salir del loop
        break

    # Generar respuesta final con LLM
    final_prompt = (
        f"The user asked: {state.user_query}. "
        f"The result is: {state.amount} ETH = ${state.result:.2f} USD. "
        f"Respond clearly."
    )

    messages = [{"role": "user", "content": final_prompt}]
    response = ask_llm(messages, tools)

    return response["message"].get("content", f"{state.amount} ETH = ${state.result:.2f} USD")