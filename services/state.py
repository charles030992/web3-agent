class AgentState:
    def __init__(self, user_query: str):
        self.user_query = user_query
        self.amount = None
        self.eth_price = None
        self.result = None
        self.last_tool_name = None
        self.used_multiply = False
        self.step_count = 0
        self.max_steps = 5

    def increment_step(self):
        self.step_count += 1

    def reached_limit(self) -> bool:
        return self.step_count >= self.max_steps