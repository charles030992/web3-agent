 # Enterprise LLM Workflow Agent

  State-driven agent architecture for business process automation using LLMs with explicit backend control.

  ## What this project demonstrates

  A production-oriented agent architecture where **LLMs handle language, not logic**.

  Routing, validation, and tool execution are controlled by the backend — not the model. This makes the system reliable, auditable, and scalable to enterprise environments.

  ## Architecture

  User input
    → Intent classification (LLM)
    → Data extraction
    → Validation        ← backend, deterministic
    → Routing           ← backend, explicit
    → Tool execution
    → Response generation (LLM)
    → Fallback / Clarify if data is missing

  ### Design principles

  | Component | Responsibility |
  |---|---|
  | LLM | Intent parsing and response generation |
  | Backend | Validation, routing, state management |
  | `AgentState` | Persistent context across workflow steps |
  | Tools | Atomic, composable business actions |
  | Fallback/Clarify | Safety and recovery layer |

  This separation means business rules live in code — not in prompts.

  ## Project structure

  web3-agent/
  ├── api/          → HTTP layer (FastAPI)
  ├── services/     → Agent logic and orchestration
  ├── tools/        → Action handlers (composable)
  └── main.py       → Entry point

  ## Stack

  - Python 3.11+
  - FastAPI
  - LangChain / LangGraph
  - Ollama (local LLM — Qwen2.5 7B Instruct)

  ## Why state-driven, not LLM-driven

  Early versions delegated all routing to the LLM:

  - Inconsistent behavior in multi-step workflows
  - No control over validation or error states
  - Business logic scattered in prompts

  The current architecture solves this:

  - State transitions are explicit and testable
  - LLM is a component, not the controller
  - The pattern applies directly to enterprise workflows: document processing, fleet management, invoice automation, internal tooling

  ## Applying this pattern to enterprise workflows

  The architecture is domain-agnostic. The same structure (AgentState → routing → tools → fallback) maps directly to:

  - **Document processing:** classify → extract → validate → route to action
  - **Fleet management:** query → validate vehicle status → trigger workflow
  - **Invoice automation:** parse PDF → extract fields → validate → generate output
  - **Internal tooling:** intent → backend lookup → structured response

  ## Running the project

  ```bash
  # 1. Activate virtual environment
  python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows

  # 2. Start local LLM
  ollama run qwen2.5:7b-instruct

  # 3. Run API
  uvicorn api.main:app --reload

  # 4. Or test directly
  python main.py

  Roadmap

  - [ ] Visual architecture diagram
  - [ ] End-to-end enterprise workflow example (document → action)
  - [ ] Input/output JSON examples
  - [ ] Unit tests for routing and state transitions
  - [ ] Docker deployment

  ---
