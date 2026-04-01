# Agent Monitoring and Failure Detection System

A prototype system for monitoring, diagnosing, and debugging AI agent behavior in production-like scenarios.

## Problem

AI agents in production often:
- get stuck in loops
- produce incorrect or irrelevant outputs
- misuse tools
- fail silently without clear debugging signals

Most systems only log outputs but lack structured understanding of agent behavior.

## Solution

This project captures agent execution traces and analyzes them to:
- detect failure patterns
- identify root causes
- generate actionable recommendations

## Features

Execution Trace Logging
- step-by-step tracking of agent actions
- includes input, output, status, and reasoning (thought)

Failure Pattern Detection
- loop detection: repeated actions with identical inputs and outputs
- no progress detection: steps producing empty or unchanged outputs
- tool misuse: incorrect tool selection for a given task
- user frustration signals: repeated retries without strategy change

Root Cause Analysis
- each issue includes explanation and underlying cause

Fix Recommendations
- suggests improvements such as fallback strategies, better tool usage, or retry handling

## Example Outputs

Loop Detection
```json
{
  "task": "book flight",
  "status": "failed",
  "issues": [
    {
      "type": "loop",
      "message": "Repeated action 'search_flights'",
      "root_cause": "Agent is retrying without updating state",
      "recommendation": "Modify query or introduce fallback strategy"
    }
  ]
}
```

Tool Misuse
```json
{
  "task": "confused agent",
  "issues": [
    {
      "type": "tool_misuse",
      "message": "Irrelevant tool used",
      "root_cause": "Incorrect tool selection",
      "recommendation": "Improve tool routing logic"
    }
  ]
}
```

Successful Execution
```json
{
  "task": "weather in delhi",
  "status": "success",
  "issues": []
}
```

## Architecture

User Request -> Agent Simulation -> Trace Logger -> Analyzer -> Debug Insights

## How to Run

1. Install dependencies
pip install fastapi uvicorn

2. Start server
uvicorn main:app --reload

3. Test API
Open in browser:
http://127.0.0.1:8000/docs

Use POST /run-agent

Example input:
{
  "task": "book flight"
}

## Proposed Direction

This prototype explores how agent monitoring systems can go beyond logging into behavior understanding and automated debugging.

Possible improvements:
- real-time trace streaming
- hallucination detection
- multi-run pattern learning
- integration with LLM-based evaluators
- automated feedback loops for agent improvement