
from time import perf_counter

def knapsack(projects, capacity):
    """0/1 Knapsack using Dynamic Programming."""
    start = perf_counter()
    n = len(projects)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        r = int(projects[i-1]["resource"])
        p = int(projects[i-1]["profit"])
        for c in range(capacity+1):
            if r <= c:
                dp[i][c] = max(p + dp[i-1][c-r], dp[i-1][c])
            else:
                dp[i][c] = dp[i-1][c]

    selected = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            selected.append(projects[i-1])
            c -= int(projects[i-1]["resource"])
    selected.reverse()
    used = sum(int(x["resource"]) for x in selected)
    elapsed = (perf_counter()-start)*1000
    return {
        "selected": selected, "max_profit": dp[n][capacity],
        "used": used, "unused": capacity-used, "dp": dp,
        "execution_ms": round(elapsed, 4),
        "complexity": {"time": f"O(n × C) = O({n} × {capacity})",
                       "space": f"O(n × C) = O({n} × {capacity})"}
    }

def greedy_knapsack(projects, capacity):
    """Greedy ratio heuristic, intentionally included for counterexample comparison."""
    start = perf_counter()
    ordered = sorted(projects, key=lambda x: int(x["profit"])/max(1,int(x["resource"])), reverse=True)
    chosen, used, profit = [], 0, 0
    for x in ordered:
        r = int(x["resource"])
        if used+r <= capacity:
            chosen.append(x); used += r; profit += int(x["profit"])
    return {"selected": chosen, "max_profit": profit, "used": used,
            "unused": capacity-used, "execution_ms": round((perf_counter()-start)*1000,4)}

def job_sequencing(jobs, slots=None):
    """Greedy Job Sequencing with Deadlines."""
    start = perf_counter()
    if not jobs:
        return {"selected": [], "schedule": [], "total_profit": 0, "execution_ms": 0}
    max_deadline = max(int(j["deadline"]) for j in jobs)
    slots = min(slots or max_deadline, max_deadline)
    schedule = [None]*slots
    for job in sorted(jobs, key=lambda x:int(x["profit"]), reverse=True):
        d = min(int(job["deadline"]), slots)-1
        while d >= 0 and schedule[d] is not None:
            d -= 1
        if d >= 0:
            schedule[d] = job
    selected = [x for x in schedule if x]
    return {"selected": selected, "schedule": schedule,
            "total_profit": sum(int(x["profit"]) for x in selected),
            "execution_ms": round((perf_counter()-start)*1000,4),
            "complexity": {"time": "O(n log n + n × d)", "space": "O(d)"}}

def priority_score(project):
    resource = int(project.get("resource",1))
    profit = int(project.get("profit",0))
    risk = int(project.get("risk",3))
    strategic = int(project.get("strategic",3))
    efficiency = min(100, (profit/max(resource,1))*5)
    return round(min(100, efficiency*.55 + strategic*10*.30 + (6-risk)*10*.15),1)

def health_score(used, capacity, profit, potential=1, deadline_success=100):
    utilization = min(100, used/max(capacity,1)*100)
    profit_eff = min(100, profit/max(potential,1)*100) if potential else 100
    overall = round(utilization*.4 + profit_eff*.35 + deadline_success*.25,1)
    return {"utilization": round(utilization,1), "profit_efficiency": round(profit_eff,1),
            "deadline_success": round(deadline_success,1), "overall": overall}
