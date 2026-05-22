from fastapi import FastAPI
from core.scanner import run_scan
from core.risk_engine import calculate_risk

app = FastAPI()

@app.get("/scan")
def scan():
    findings = run_scan()
    risk = calculate_risk(findings)

    return {
        "findings": findings,
        "risk": risk
    }