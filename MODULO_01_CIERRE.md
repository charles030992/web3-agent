# MODULO 01 - CIERRE

## Qué se hizo

Se reformuló el posicionamiento del proyecto `web3-agent` para que deje de comunicarse como un experimento educativo centrado en Web3 y pase a presentarse como una base técnica para automatización empresarial con agentes LLM.

El nuevo enfoque comunica:

- Automatización de procesos empresariales mediante Python y LLMs.
- Arquitectura modular basada en estado explícito (`AgentState`).
- Separación entre API, servicios, herramientas y lógica de orquestación.
- Evolución desde un agente LLM-driven hacia un sistema state-driven más controlable.
- Aplicabilidad a casos de uso enterprise como flota, renting, facturación, validación de datos y generación de respuestas operativas.
- Stack alineado con empleabilidad técnica: Python, FastAPI, LLM orchestration, workflow automation, agentes IA y automatización empresarial.

---

# README generado

```markdown
# web3-agent

Python-based LLM workflow automation agent with modular architecture, explicit state management and enterprise-oriented use cases.

This project started as a local Web3 agent experiment and has evolved into a backend-oriented automation system for business workflows. The goal is to demonstrate how LLMs can be integrated into deterministic Python applications to classify requests, route workflows, call tools and generate structured operational responses.

## What problem does this project solve?

Many business processes still depend on manual interpretation of emails, spreadsheets, tickets or internal requests. Examples include fleet management, renting documentation, invoice checks, cost allocation, vehicle assignment or operational queries.

This repository explores how to automate those workflows using:

- Python backend logic
- LLM orchestration
- State-driven agent architecture
- Tool-based execution
- FastAPI endpoints
- Modular business rules
- Controlled fallback and clarification flows

The main idea is simple:

> Use the LLM for language understanding and response generation, but keep the workflow control, business rules and tool execution inside deterministic backend code.

This makes the system easier to test, debug and extend than a fully LLM-driven agent.

## Key features

- Modular Python architecture
- State-driven workflow orchestration
- Explicit `AgentState` object to track execution context
- Dynamic routing between workflow steps
- Tool layer for external actions and calculations
- FastAPI-ready backend structure
- Local LLM integration through Ollama
- Business workflow automation patterns
- Clarification and fallback handling
- Separation between model reasoning, backend logic and tools

## Enterprise automation use cases

The project is designed to be extended toward real business automation scenarios such as:

### Fleet management automation

Examples:

- Identify vehicle registration plates in user requests
- Retrieve assigned vehicle cost or operational data
- Route the request depending on missing fields
- Generate a structured business response

### Renting and vehicle documentation workflows

Examples:

- Detect renting provider references
- Prepare operational responses for ITV, fleet or documentation tasks
- Handle missing information through clarification logic

### Invoice and cost allocation support

Examples:

- Classify invoice-related queries
- Extract relevant entities such as dates, vehicles, providers or cost centers
- Trigger calculation or lookup tools
- Generate standardized business outputs

### Generic workflow automation

Examples:

- Classify intent
- Extract structured data from natural language
- Validate completeness
- Execute tools
- Return a final answer adapted to business context

## Architecture

The repository follows a modular backend architecture:

```text
web3-agent/
│
├── api/                  # FastAPI / HTTP layer
├── services/             # Agent orchestration and workflow logic
├── tools/                # Executable tools used by the agent
├── main.py               # Local execution entry point
└── README.md             # Project documentation
```

## Agent design

The project evolved from an LLM-driven agent to a state-driven agent.

### Previous approach: LLM-driven

In the first version, the LLM was responsible for deciding:

- which tool to call
- when to call it
- how to continue the workflow
- when to finish

This approach is flexible, but it creates problems in enterprise workflows:

- inconsistent behavior
- difficult debugging
- weak control over multi-step execution
- excessive dependency on the LLM
- harder testing

### Current approach: State-driven orchestration

The current design introduces explicit backend control.

The workflow is controlled by Python code and an explicit state object. The LLM is used only where it adds value: language interpretation and final response generation.

Typical execution flow:

```text
User request
   ↓
Intent classification
   ↓
Entity extraction
   ↓
State validation
   ↓
Tool execution
   ↓
Business logic / routing
   ↓
Final response generation
```

## Why this architecture matters

Enterprise automation should not rely on a black-box LLM deciding everything.

This architecture keeps the critical parts deterministic:

- workflow control
- validation
- business rules
- tool execution
- routing
- error handling

The LLM is integrated as one component inside a controlled backend system, not as the whole system.

## Tech stack

- Python
- FastAPI
- LangGraph-ready architecture
- LLM orchestration
- Ollama
- Qwen2.5 7B Instruct
- Modular tool calling
- State-driven agent workflows
- GitHub version control

## Keywords

Python, FastAPI, LLM orchestration, workflow automation, AI agents, agentes IA, automatización empresarial, enterprise automation, tool calling, backend automation, LangGraph, AgentState, business process automation.

## Example: local execution

The project can be executed locally from `main.py`.

Example request:

```python
question = "How much is 2.35 ETH in USD?"
result = run_agent(question)
print(result)
```

Although the initial example uses ETH price calculation, the same architecture can be extended to enterprise workflows such as fleet, renting, invoices and internal operational requests.

## How to run

### 1. Clone the repository

```bash
git clone https://github.com/charles030992/web3-agent.git
cd web3-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Ollama

Make sure Ollama is running locally and that the required model is available.

Example:

```bash
ollama run qwen2.5:7b-instruct
```

### 6. Run the agent locally

```bash
python main.py
```

### 7. Run the API

If the FastAPI layer is enabled:

```bash
uvicorn api.main:app --reload
```

## Project status

This repository is an active technical portfolio project.

Current focus:

- consolidating the state-driven architecture
- improving business workflow routing
- adding enterprise automation examples
- preparing the codebase for LangGraph-based orchestration
- documenting practical use cases for employability in AI automation roles

## Roadmap

Planned improvements:

- Add dedicated business workflow examples
- Add fleet management use case
- Add invoice classification and validation flow
- Add structured JSON outputs
- Add LangGraph implementation
- Add tests for routing and state transitions
- Add FastAPI endpoints for external integrations
- Add n8n/webhook integration examples
- Add persistence layer with PostgreSQL or MySQL

## Professional positioning

This project demonstrates practical skills relevant to AI automation and enterprise backend roles:

- building Python services around LLMs
- designing modular agent architectures
- controlling workflows with explicit state
- integrating tools into agent systems
- separating business logic from model output
- preparing LLM systems for real operational use cases

The objective is not to build a chatbot. The objective is to build a controlled automation layer where LLMs help interpret business requests and Python executes the workflow reliably.
```

---

## Cómo venderlo en LinkedIn

- Reposicioné mi proyecto `web3-agent`: de agente local experimental a arquitectura modular en Python para automatización empresarial con LLMs, usando control state-driven, tool calling, FastAPI y flujos preparados para casos reales como flota, renting y facturación.

**Keywords:** Python, FastAPI, LLM orchestration, workflow automation, agentes IA, automatización empresarial, AgentState, LangGraph-ready, backend automation, tool calling.

---

## Estado

Listo para subir a GitHub.
