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