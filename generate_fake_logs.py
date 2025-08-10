
import json, random, time
from datetime import datetime, timedelta
from pathlib import Path

LOG_PATH = Path("logs/synthetic_inventory_logs.json")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

OUTCOMES = ["success", "retry", "fail"]
start_time = datetime.now() - timedelta(days=1)

def generate_log_line(ts):
    return {
        "timestamp": ts.isoformat(),
        "batch_id": f"BATCH{random.randint(1000,9999)}",
        "duration_sec": round(random.uniform(0.05, 0.5), 3),
        "outcome": random.choices(OUTCOMES, weights=[0.85, 0.10, 0.05])[0],
        "records_processed": random.randint(50, 500)
    }

with open(LOG_PATH, "w") as f:
    for i in range(10000):
        timestamp = start_time + timedelta(seconds=i * random.randint(10, 30))
        json.dump(generate_log_line(timestamp), f)
        f.write("\n")

print(f"Generated 10,000 logs at {LOG_PATH}")
