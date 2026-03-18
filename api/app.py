from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict
from services.agent_services import list_tools, run_tool, ToolNotFoundError
from fastapi import HTTPException
from services.wallet_services import analyze_wallet
from services.wallet_summary_services import wallet_summary


app = FastAPI(title="Web3 Agent API", version="0.1")


class WalletRequest(BaseModel):
    address: str
    simulate: bool = True


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze_wallet")
def analyze_wallet_endpoint(payload: WalletRequest):
    result = analyze_wallet(payload.address, simulate=payload.simulate)
    return {"result": result}

class ToolRunRequest(BaseModel):
    tool_name: str
    args: Dict[str, Any] = {}


@app.get("/tools")
def tools_endpoint():
    return list_tools()


@app.post("/tools/run")
def tools_run_endpoint(payload: ToolRunRequest):
    try:
        result = run_tool(payload.tool_name, payload.args)
        return {"tool_name": payload.tool_name, "result": result}
    except ToolNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except TypeError as e:
        # Suele ser: argumentos incorrectos (faltan o sobran)
        raise HTTPException(status_code=422, detail=f"Args inválidos: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error ejecutando tool: {e}")
    
@app.post("/wallet/summary")
def wallet_summary_endpoint(payload: WalletRequest):
    return wallet_summary(payload.address, simulate=payload.simulate)