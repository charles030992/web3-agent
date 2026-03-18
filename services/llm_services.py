import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:7b-instruct"
SYSTEM_PROMPT = """
You are an AI agent that can use tools.

Rules:
- Think step by step.
- Use tools whenever real-time data is needed.
- Use tools whenever a calculation is needed.
- Do NOT perform calculations mentally if a calculation tool is available.
- If the task requires multiple steps, call multiple tools in sequence.
- Do NOT call the same tool again unless it is strictly necessary.
- After receiving a tool result, continue solving the ORIGINAL user question.
- Only give the final answer when no more tools are needed.
- When using tools, return tool call structure (tool_calls) and avoid final answer text until done.
- If you return a final answer, do not include tool_calls.
- Be concise and accurate.
"""


def ask_llm(messages, tools=None):
    full_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *messages
        ]   
    payload = {
        "model": MODEL,
        "messages": full_messages,
        "stream": False
    }

    if tools:
        payload["tools"] = tools

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()