def analyze_trace(trace):
    steps = trace["steps"]
    issues = []

    for i in range(len(steps) - 2):
        s1, s2, s3 = steps[i], steps[i+1], steps[i+2]

        if (
            s1["action"] == s2["action"] == s3["action"] and
            s1["input"] == s2["input"] == s3["input"] and
            s1["output"] == s2["output"] == s3["output"]
        ):
            issues.append({
                "type": "loop",
                "message": f"Repeated action '{s1['action']}' with identical input/output",
                "root_cause": "Agent is retrying without updating state or strategy",
                "recommendation": "Modify input/query after failure or introduce fallback logic"
            })
            break

    empty_outputs = [s for s in steps if s["output"] == ""]
    if len(empty_outputs) >= 2:
        issues.append({
            "type": "no_progress",
            "message": "Multiple steps produced empty outputs",
            "root_cause": "Agent is not generating meaningful intermediate results",
            "recommendation": "Improve tool responses or enforce validation after each step"
        })

    for step in steps:
        if step["action"] == "search_flights" and "weather" in step["input"].lower():
            issues.append({
                "type": "tool_misuse",
                "message": "Irrelevant tool used for given task",
                "root_cause": "Agent failed to select appropriate tool",
                "recommendation": "Improve tool selection logic or add tool constraints"
            })
            
    if len(steps) >= 3:
        retry_like = sum(
            1 for i in range(1, len(steps))
            if steps[i]["action"] == steps[i-1]["action"]
        )
        if retry_like >= 2:
            issues.append({
                "type": "user_frustration_signal",
                "message": "Agent repeatedly retries similar actions",
                "root_cause": "Agent stuck without alternative strategy",
                "recommendation": "Introduce retry limits or alternative execution paths"
            })

    if not issues:
        status = "success"
        insight = "Agent executed successfully with stable behavior"
    else:
        status = "failed"
        insight = " | ".join([issue["root_cause"] for issue in issues])

    return {
        "trace_id": trace["trace_id"],
        "task": trace["task"],
        "step_count": len(steps),
        "status": status,
        "issues": issues,
        "insight": insight,
        "steps": steps
    }