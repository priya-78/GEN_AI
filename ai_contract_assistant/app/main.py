
from fastapi import FastAPI
from pydantic import BaseModel
from app.contract_utils import extract_clauses
from app.negotiator import negotiate_clauses

app = FastAPI()

class ContractInput(BaseModel):
    text: str

@app.post("/optimize/")
def optimize_contract(contract: ContractInput):
    clauses = extract_clauses(contract.text)
    optimized = negotiate_clauses(clauses)
    return {"optimized_clauses": optimized}
