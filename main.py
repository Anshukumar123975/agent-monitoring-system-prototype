from fastapi import FastAPI
from agent import run_agent
from analyzer import analyze_trace

app = FastAPI()

@app.post("/run-agent")
def run(task: dict):
    trace = run_agent(task["task"])
    result = analyze_trace(trace)
    return result