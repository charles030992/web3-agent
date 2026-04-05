# WEB3_AGENT

Agente local construido en Python con arquitectura modular y LLM local mediante Ollama.

## Qué hace

Este proyecto implementa un agente sencillo capaz de:

- consultar el precio de ETH
- consultar balances de wallet
- realizar cálculos simples
- usar un modelo local para decidir qué herramienta utilizar

## Arquitectura

- `api/` → capa HTTP / FastAPI
- `services/` → lógica del agente
- `tools/` → herramientas disponibles
- `main.py` → punto de entrada para pruebas

## Tecnologías

- Python
- Ollama
- Qwen2.5 7B Instruct
- FastAPI

## Objetivo

Entender cómo funciona un agente desde cero:

- tool calling
- orquestación
- uso de LLM local
- separación entre modelo, backend y herramientas

## Cómo ejecutarlo

1. Activar entorno virtual
2. Levantar Ollama con el modelo local
3. Ejecutar `main.py` o la API

## Estado del proyecto

Proyecto educativo en desarrollo.

## Evolución del agente

La primera versión del agente estaba completamente controlada por el modelo (LLM-driven),
donde el LLM decidía qué herramientas utilizar y cuándo finalizar el proceso.

Durante el desarrollo se identificaron limitaciones en este enfoque:

- dificultad en tareas multi-step
- comportamiento inconsistente del modelo
- dependencia excesiva del LLM para el flujo

La versión actual introduce un cambio clave:

### Nuevo enfoque: State-driven

- uso de un estado explícito (`AgentState`)
- control del flujo desde backend
- ejecución determinista de herramientas
- el LLM se utiliza únicamente para generar la respuesta final

Este cambio mejora la robustez, control y escalabilidad del sistema.