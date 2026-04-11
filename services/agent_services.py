import re

from services.state import AgentState
from services.llm_services import ask_llm
from services.tool_schema import tools

from services.agent_steps import (
    extract_amount_step,
    get_price_step,
    calculate_step,
    generate_response_step
)



def run_agent(query):
    state = AgentState(query)

    print("\n--- START ---")

    # Nodo 1
    state = extract_amount_step(state)
    print(f"Amount extracted: {state.amount}")

    if state.amount is None:
        return "Could not extract ETH amount from query."

    # Nodo 2
    state = get_price_step(state)
    print(f"ETH price: {state.eth_price}")

    # Nodo 3
    state = calculate_step(state)
    print(f"Result: {state.result}")

    # Nodo 4 (LLM solo para lenguaje)
    response = generate_response_step(state, ask_llm, tools)

    return response