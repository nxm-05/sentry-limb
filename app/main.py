from fastapi import FastAPI
import requests
import time
import redis

app = FastAPI()

BACKEND_URL = "http://127.0.0.1:8001/profile"

# Redis connection
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

FAIL_LIMIT = 3
COOLDOWN_TIME = 30  # seconds

@app.get("/profile")
def get_profile():
    current_time = time.time()

    fail_count = int(r.get("fail_count") or 0)
    state = r.get("state") or "CLOSED"
    last_failure_time = float(r.get("last_failure_time") or 0)

    # If circuit is OPEN
    if state == "OPEN":
        if current_time - last_failure_time > COOLDOWN_TIME:
            r.set("state", "HALF_OPEN")
        else:
            return {
                "mode": "CIRCUIT_OPEN",
                "message": "Backend temporarily blocked (Redis)"
            }

    try:
        response = requests.get(BACKEND_URL, timeout=2)

        if response.status_code != 200:
            raise Exception("Backend error")

        # Success → reset breaker
        r.set("fail_count", 0)
        r.set("state", "CLOSED")

        return response.json()

    except:
        fail_count += 1
        r.set("fail_count", fail_count)
        r.set("last_failure_time", current_time)

        if fail_count >= FAIL_LIMIT:
            r.set("state", "OPEN")

        return {
            "mode": "FALLBACK",
            "fail_count": fail_count,
            "state": r.get("state")
        }