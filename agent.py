import uuid

def run_agent(task: str):
    trace_id = str(uuid.uuid4())

    # Example traces just for simulation
    if "flight" in task:
        steps = [
            {
                "step": 1,
                "action": "search_flights",
                "input": "NY to SF",
                "output": "No results",
                "status": "success",
                "thought": "No results found, retrying search"
            },
            {
                "step": 2,
                "action": "search_flights",
                "input": "NY to SF",
                "output": "No results",
                "status": "success",
                "thought": "Still no results, retrying again"
            },
            {
                "step": 3,
                "action": "search_flights",
                "input": "NY to SF",
                "output": "No results",
                "status": "success",
                "thought": "Retrying again without changing input"
            }
        ]

    elif "weather" in task:
        steps = [
            {
                "step": 1,
                "action": "get_weather",
                "input": "Delhi",
                "output": "25°C Sunny",
                "status": "success",
                "thought": "Fetched weather data"
            }
        ]
        
    elif "confused" in task:
        steps = [
            {
                "step": 1,
                "action": "search_flights",
                "input": "weather in Delhi",
                "output": "irrelevant result",
                "status": "success",
                "thought": "Trying to use flight search for weather"
            }
        ]
        
    else:
        steps = [
            {
                "step": 1,
                "action": "start_process",
                "input": task,
                "output": "",
                "status": "success",
                "thought": "Starting process"
            },
            {
                "step": 2,
                "action": "process_data",
                "input": task,
                "output": "",
                "status": "success",
                "thought": "Processing data but no progress"
            },
            {
                "step": 3,
                "action": "process_data",
                "input": task,
                "output": "",
                "status": "success",
                "thought": "Still no progress"
            }
        ]

    trace = {
        "trace_id": trace_id,
        "task": task,
        "steps": steps,
        "status": "completed"
    }

    return trace