
from flask import Flask, render_template, request, jsonify, redirect, url_for
from algorithms import knapsack, greedy_knapsack, job_sequencing, priority_score, health_score
import random, time

app = Flask(__name__)
app.secret_key = "optiverse-2026"

PROJECTS = [
 {"id":"P01","name":"AI Automation","resource":18,"profit":95,"risk":2,"strategic":5},
 {"id":"P02","name":"Cloud Upgrade","resource":12,"profit":70,"risk":3,"strategic":4},
 {"id":"P03","name":"Green Energy","resource":20,"profit":100,"risk":2,"strategic":5},
 {"id":"P04","name":"Office Renovation","resource":10,"profit":35,"risk":4,"strategic":2},
 {"id":"P05","name":"Cybersecurity","resource":15,"profit":85,"risk":2,"strategic":5},
]
JOBS = [
 {"id":"J01","name":"Data Backup","deadline":2,"profit":40},
 {"id":"J02","name":"Security Patch","deadline":1,"profit":70},
 {"id":"J03","name":"Server Migration","deadline":2,"profit":55},
 {"id":"J04","name":"Report Generation","deadline":3,"profit":30},
 {"id":"J05","name":"System Audit","deadline":1,"profit":25},
]
HISTORY=[]

def dashboard_data():
    capacity=50
    k=knapsack(PROJECTS,capacity)
    j=job_sequencing(JOBS)
    return k,j,capacity

@app.route("/")
def home():
    k,j,c=dashboard_data()
    return render_template("index.html", projects=PROJECTS, jobs=JOBS, k=k, j=j, capacity=c)

@app.route("/dashboard")
def dashboard():
    k,j,c=dashboard_data()
    scores=[priority_score(p) for p in PROJECTS]
    return render_template("dashboard.html", k=k,j=j,capacity=c,scores=scores)

@app.route("/projects", methods=["GET","POST"])
def projects():
    result=None
    capacity=50
    if request.method=="POST":
        capacity=int(request.form.get("capacity",50))
        result=knapsack(PROJECTS,capacity)
        HISTORY.append({"type":"Knapsack","profit":result["max_profit"],"score":round(result["used"]/max(capacity,1)*100,1)})
    enriched=[dict(p, priority=priority_score(p)) for p in PROJECTS]
    return render_template("projects.html", projects=enriched, result=result, capacity=capacity)

@app.route("/jobs", methods=["GET","POST"])
def jobs():
    result=None
    if request.method=="POST":
        result=job_sequencing(JOBS)
        HISTORY.append({"type":"Scheduler","profit":result["total_profit"],"score":100})
    return render_template("jobs.html", jobs=JOBS, result=result)

@app.route("/battle")
def battle():
    capacity=50
    dp=knapsack(PROJECTS,capacity)
    gr=greedy_knapsack(PROJECTS,capacity)
    return render_template("battle.html", dp=dp, gr=gr, capacity=capacity)

@app.route("/simulator")
def simulator():
    return render_template("simulator.html")

@app.route("/performance")
def performance():
    sizes=[5,10,15,20,25]
    # deterministic synthetic performance illustration for visual comparison
    dp_times=[round((n*n)*0.018 + 0.05,3) for n in sizes]
    greedy_times=[round(n*0.012 + 0.03,3) for n in sizes]
    return render_template("performance.html", sizes=sizes, dp_times=dp_times, greedy_times=greedy_times)

@app.route("/advisor")
def advisor():
    return render_template("advisor.html")

@app.route("/sdg")
def sdg():
    return render_template("sdg.html")

@app.route("/leaderboard")
def leaderboard():
    board=HISTORY[-10:] or [
      {"type":"Hospital Scenario","profit":520,"score":94},
      {"type":"Manufacturing","profit":480,"score":91},
      {"type":"Cloud Infrastructure","profit":450,"score":88}]
    return render_template("leaderboard.html", board=board)

@app.route("/api/simulate", methods=["POST"])
def simulate():
    d=request.get_json()
    capacity=int(d.get("capacity",50))
    profit_factor=float(d.get("profit_factor",1))
    count=int(d.get("count",5))
    base=PROJECTS[:]
    while len(base)<count:
        i=len(base)+1
        base.append({"id":f"R{i:02}","name":f"Generated Project {i}","resource":random.randint(5,25),
                     "profit":random.randint(30,130),"risk":random.randint(1,5),"strategic":random.randint(1,5)})
    base=base[:count]
    sim=[dict(p, profit=round(int(p["profit"])*profit_factor)) for p in base]
    r=knapsack(sim,capacity)
    h=health_score(r["used"],capacity,r["max_profit"],sum(int(x["profit"]) for x in sim))
    return jsonify({"result":r,"health":h,"projects":sim})

@app.route("/api/advice", methods=["POST"])
def advice():
    d=request.get_json()
    optimal=d.get("optimal",True); speed=d.get("speed","medium"); capacity=d.get("capacity","limited")
    if optimal:
        rec="Dynamic Programming – 0/1 Knapsack"
        reason="Your scenario prioritizes guaranteed optimal profit under limited resources."
    elif speed=="high":
        rec="Greedy Strategy"
        reason="Fast decisions and lower memory usage are your highest priorities."
    else:
        rec="Hybrid Decision Workflow"
        reason="Use Greedy for quick filtering, then Dynamic Programming for the final high-value decision."
    return jsonify({"recommendation":rec,"reason":reason})

if __name__=="__main__":
    app.run(debug=True, port=5000)
