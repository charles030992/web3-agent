# Enterprise LLM Workflow Agent
[![CI](https://github.com/charles030992/web3-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/charles030992/web3-agent/actions/workflows/ci.yml)

State-driven agent architecture for business process automation using LLMs with explicit backend control.

Status: educational project in progress. The architecture is demonstrated today on a small ETH → USD use case; enterprise workflows (fleet, invoicing) are the next step, see the [roadmap](#roadmap).

## What this project demonstrates

An agent architecture where **LLMs handle language, not logic**.

Data extraction, tool execution and the flow of the conversation are controlled by the backend — not the model. That makes the behaviour deterministic and easy to test: the same input follows the same path, and a misbehaving model cannot change the flow.

## How it works today

Given a question such as *"How much is 2.35 ETH in USD?"*:

```
User input
  → Data extraction      ← backend (parses the ETH amount)
  → Tool execution       ← backend (live ETH price from CoinGecko, then the calculation)
  → Response generation  ← LLM (phrases the computed result)
```

If the question has no ETH amount, the agent says so. If the model is unreachable or returns empty text, the computed result is returned directly. The LLM never decides what runs next.

## Target architecture

The pattern is meant to grow into a fuller workflow. Not implemented yet:

```
User input → Intent classification → Data extraction → Validation → Routing
          → Tool execution → Response generation → Fallback / Clarify if data is missing
```

### Design principles

| Component | Responsibility |
|---|---|
| LLM | Response generation (intent parsing is planned) |
| Backend | Extraction, tool execution, state management (validation and routing are planned) |
| `AgentState` | Context carried across workflow steps |
| Tools | Atomic, composable actions, listed in a registry |
| Fallback | Recovery when the model fails or data is missing |

This separation means business rules live in code, not in prompts.

## Project structure

```
web3-agent/
├── api/          → HTTP layer (FastAPI)
├── services/     → Agent flow, state, steps, Ollama client
├── tools/        → Actions (ETH price, wallet balance, multiplication) and their registry
├── tests/        → Unit tests (unittest, no extra dependencies)
└── main.py       → Entry point
```

## Stack

- Python 3.11+
- FastAPI
- Ollama (local LLM — Qwen2.5 7B Instruct)
- `requests`; tests with the standard library `unittest`

## Why state-driven, not LLM-driven

The first version delegated all routing to the LLM:

- Inconsistent behaviour in multi-step workflows
- No control over validation or error states
- Business logic scattered in prompts

The current architecture addresses this:

- State transitions are explicit and testable
- The LLM is a component, not the controller
- The same pattern can be applied to other workflows

One lesson from the way: offering tools to the model in the final step made it try to call one instead of answering, returning empty text. Since the result is already computed, that step runs without tools.

## Applying this pattern to enterprise workflows

The structure (`AgentState` → routing → tools → fallback) is domain-agnostic. Examples of where it would map (ideas, not implemented):

- **Document processing:** classify → extract → validate → route to action
- **Fleet management:** query → validate vehicle status → trigger workflow
- **Invoice automation:** parse PDF → extract fields → validate → generate output
- **Internal tooling:** intent → backend lookup → structured response

## Running the project

Requirements: Python 3.11+ and [Ollama](https://ollama.com).

```bash
ollama pull qwen2.5:7b-instruct

python -m venv .venv
.venv\Scripts\activate            # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

With Ollama running:

```bash
python main.py                              # runs the example question defined in main.py
uvicorn api.app:app --reload                # API at http://127.0.0.1:8000/docs
python -m unittest discover -s tests -t .   # tests
```

API endpoints: `GET /health`, `GET /tools`, `POST /tools/run`, `POST /analyze_wallet`, `POST /wallet/summary`.

## Known limitations

- The wallet balance is **simulated** (always `2.35 ETH`); real mode is not implemented.
- The agent only understands questions that contain an ETH amount (e.g. `2.35 ETH`); anything else gets a message saying so.
- The API does not expose the agent yet, only the tools and the wallet analysis.
- `services/tool_schema.py` is left over from the first (LLM-driven) version and is currently unused.

## Roadmap

- [x] Unit tests for the steps, the LLM fallbacks and the tool registry
- [ ] Unit tests for routing and state transitions
- [ ] Intent classification, validation and clarify/fallback routing
- [ ] End-to-end enterprise workflow example (document → action)
- [ ] Input/output JSON examples
- [ ] Visual architecture diagram
- [ ] Docker deployment
