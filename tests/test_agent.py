import unittest

from services.agent_steps import calculate_step, generate_response_step, get_price_step
from services.parsers import extract_eth_amount
from services.state import AgentState
from tools.registry import ToolNotFoundError, list_tools, run_tool


class ExtractEthAmountTests(unittest.TestCase):
    def test_integer_and_decimal_amounts(self):
        self.assertEqual(extract_eth_amount("How much is 2 ETH in USD?"), 2.0)
        self.assertEqual(extract_eth_amount("How much is 2.35 ETH in USD?"), 2.35)

    def test_case_insensitive_unit(self):
        self.assertEqual(extract_eth_amount("convert 0.5 eth"), 0.5)

    def test_no_amount(self):
        self.assertIsNone(extract_eth_amount("What is the weather?"))
        self.assertIsNone(extract_eth_amount("ETH is up today"))


class StepsTests(unittest.TestCase):
    def test_get_price_step_keeps_an_existing_price(self):
        state = AgentState("x")
        state.eth_price = 2000.0
        # Must not hit the network when the price is already known.
        self.assertEqual(get_price_step(state).eth_price, 2000.0)

    def test_calculate_step_multiplies_amount_by_price(self):
        state = AgentState("x")
        state.amount, state.eth_price = 2.0, 2500.0
        self.assertEqual(calculate_step(state).result, 5000.0)


class GenerateResponseTests(unittest.TestCase):
    def make_state(self):
        state = AgentState("How much is 2 ETH in USD?")
        state.amount, state.eth_price, state.result = 2.0, 2500.0, 5000.0
        return state

    def test_returns_the_llm_text(self):
        def fake_llm(messages, tools=None):
            return {"message": {"content": "  2 ETH is about $5000.  "}}

        self.assertEqual(
            generate_response_step(self.make_state(), fake_llm), "2 ETH is about $5000."
        )

    def test_does_not_offer_tools_to_the_llm(self):
        calls = []

        def fake_llm(messages, tools=None):
            calls.append(tools)
            return {"message": {"content": "ok"}}

        generate_response_step(self.make_state(), fake_llm)
        self.assertEqual(calls, [None])

    def test_falls_back_when_the_llm_returns_empty_content(self):
        # Regression: with tools offered, the model answered with tool_calls and "".
        def fake_llm(messages, tools=None):
            return {"message": {"content": "", "tool_calls": [{"function": {"name": "x"}}]}}

        self.assertEqual(
            generate_response_step(self.make_state(), fake_llm), "2.0 ETH = $5000.00 USD"
        )

    def test_falls_back_when_the_llm_is_unreachable(self):
        def fake_llm(messages, tools=None):
            raise ConnectionError("ollama is down")

        self.assertEqual(
            generate_response_step(self.make_state(), fake_llm), "2.0 ETH = $5000.00 USD"
        )


class RegistryTests(unittest.TestCase):
    def test_list_tools_exposes_the_catalog(self):
        self.assertIn("multiply_numbers", list_tools())

    def test_run_tool_executes_a_known_tool(self):
        self.assertEqual(run_tool("multiply_numbers", {"a": 3, "b": 4}), 12)

    def test_run_tool_rejects_an_unknown_tool(self):
        with self.assertRaises(ToolNotFoundError):
            run_tool("does_not_exist", {})


class ApiImportTests(unittest.TestCase):
    def test_api_module_imports(self):
        # Regression: api.app imported names that did not exist, so the API never started.
        import api.app

        paths = {route.path for route in api.app.app.routes}
        self.assertTrue({"/health", "/tools", "/tools/run"} <= paths)


if __name__ == "__main__":
    unittest.main()
