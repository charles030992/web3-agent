# WEB3_AGENT

Estado: proyecto educativo en desarrollo

Agente local en Python con arquitectura modular y un LLM local (Ollama). Dada una pregunta como *"How much is 2.35 ETH in USD?"*, el **backend** extrae la cantidad, consulta el precio real de ETH y calcula el resultado; el LLM solo redacta la respuesta final.

## Qué hace

- Extrae la cantidad de ETH de la pregunta.
- Consulta el precio de ETH en USD (CoinGecko, sin API key).
- Calcula el valor en dólares.
- Pide a un modelo local (Qwen2.5 7B Instruct vía Ollama) que redacte la respuesta. Si el modelo no responde o devuelve texto vacío, se responde con el resultado calculado.
- Expone una API HTTP (FastAPI) con las herramientas y un análisis básico de wallet.

## Arquitectura

- `services/agent_services.py` → flujo del agente (`run_agent`), controlado desde el backend
- `services/state.py` → estado explícito del agente (`AgentState`)
- `services/agent_steps.py` → pasos: extraer cantidad, obtener precio, calcular, redactar respuesta
- `services/llm_services.py` → cliente de Ollama
- `tools/` → herramientas (precio de ETH, balance de wallet, multiplicación) y su registro (`registry.py`)
- `api/app.py` → API FastAPI
- `main.py` → punto de entrada para probar el agente
- `tests/` → tests unitarios (`unittest`, sin dependencias extra)

## Cómo ejecutarlo

Requisitos: Python 3.11+ y [Ollama](https://ollama.com).

```bash
ollama pull qwen2.5:7b-instruct

python -m venv .venv
.venv\Scripts\activate            # en Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Con Ollama en marcha:

```bash
python main.py                    # pregunta de ejemplo definida en main.py
uvicorn api.app:app --reload      # API en http://127.0.0.1:8000/docs
python -m unittest discover -s tests -t .
```

Endpoints de la API: `GET /health`, `GET /tools`, `POST /tools/run`, `POST /analyze_wallet`, `POST /wallet/summary`.

## Limitaciones actuales

- El balance de wallet es **simulado** (siempre devuelve `2.35 ETH`); el modo real no está implementado.
- El agente solo entiende preguntas con una cantidad en ETH (por ejemplo `2.35 ETH`); cualquier otra pregunta recibe un mensaje indicándolo.
- La API no expone todavía el agente; solo las herramientas y el análisis de wallet.
- `services/tool_schema.py` es un resto de la primera versión (controlada por el LLM) y ahora no se usa.

## Objetivo

Entender cómo funciona un agente desde cero:

- tool calling
- orquestación
- uso de LLM local
- separación entre modelo, backend y herramientas

## Evolución del agente

La primera versión estaba completamente controlada por el modelo (LLM-driven): el LLM decidía qué herramientas usar y cuándo terminar.

Durante el desarrollo se identificaron limitaciones en ese enfoque:

- dificultad en tareas multi-step
- comportamiento inconsistente del modelo
- dependencia excesiva del LLM para el flujo

La versión actual es **state-driven**:

- uso de un estado explícito (`AgentState`)
- control del flujo desde backend
- ejecución determinista de herramientas
- el LLM se utiliza únicamente para generar la respuesta final

Un detalle aprendido por el camino: al ofrecer herramientas al modelo en el paso final, intentaba llamar a una en vez de responder y devolvía texto vacío. Como el resultado ya está calculado, ese paso se hace sin herramientas.
