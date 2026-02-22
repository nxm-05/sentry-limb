# Sentry-Limb – Distributed Circuit Breaker & Failure Isolation System

Sentry-Limb is a resilience-focused middleware service built using FastAPI and Redis that implements the Circuit Breaker pattern to protect unstable backend services. The system prevents cascading failures by isolating failing services, enforcing cooldown periods, and providing fallback responses during outages.

This project simulates a distributed system environment where a gateway service communicates with an unreliable backend. When repeated failures occur, the circuit transitions between CLOSED, OPEN, and HALF-OPEN states to maintain system stability and graceful degradation.

---

## 🏗 System Architecture

Client → Gateway (Circuit Breaker) → Backend Service  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Redis (Shared State)

Redis is used to maintain distributed breaker state including:
- Failure count
- Current circuit state
- Last failure timestamp

---

## 🚀 Key Features

- Implementation of Circuit Breaker pattern
- OPEN / HALF-OPEN / CLOSED state transitions
- Configurable failure threshold and cooldown window
- Distributed failure tracking using Redis
- Timeout-based backend protection
- Graceful fallback responses during backend outages
- Simulated unstable backend service for resilience testing

---

## ⚙️ Tech Stack

- Python
- FastAPI
- Redis
- Uvicorn

---

## ▶️ How to Run

1. Start Redis:
   redis-server

2. Run the backend service (simulated unstable service):
   uvicorn backend.main:app --port 8001

3. Run the gateway service (circuit breaker):
   uvicorn gateway.main:app --port 8000

4. Test the system:
   Open http://localhost:8000/profile

Repeated failures will trigger the circuit to OPEN state, temporarily blocking backend calls and returning fallback responses.

---

## 📚 Engineering Concepts Demonstrated

- Fault tolerance
- Resilience engineering
- Failure isolation
- Distributed state management
- Graceful degradation
- Microservice communication patterns

---

## 🎯 Project Goal

The goal of this project is to understand and implement production-level resilience patterns used in distributed systems to maintain service availability even when dependent services fail.
