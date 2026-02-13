from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/profile")
def get_profile():
    # Simulate random failure
    if random.random() < 0.5:
        raise Exception("Backend crashed!")

    return {
        "name": "User1",
        "points": 120,
        "status": "Active User"
    }