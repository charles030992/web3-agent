from services.agent_services import run_agent


if __name__ == "__main__":

    question = "How much is 2.35 ETH in USD?"

    result = run_agent(question)

    print("Agent response:")
    print(result)