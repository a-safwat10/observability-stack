# Observability Stack with Prometheus & Grafana

A local observability platform built with Docker Compose, monitoring a Flask application with Prometheus metrics collection and Grafana dashboards.

## Stack

| Tool | Purpose |
|---|---|
| Flask | Sample application exposing custom metrics |
| Prometheus | Metrics collection and time-series database |
| Grafana | Metrics visualization and dashboards |
| Docker Compose | Container orchestration |

## Architecture

```
Flask App (/metrics endpoint)
      ↓ scrape every 15s
Prometheus (stores time-series data)
      ↓ query
Grafana (visualizes dashboards)
```

## Metrics Monitored

- **Total Requests** — cumulative request count per endpoint
- **Request Rate** — requests per second over time
- **Average Latency** — mean response time per endpoint

## How to Run

```bash
docker compose up -d
```

| Service | URL |
|---|---|
| Flask App | http://localhost:5000 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

Grafana credentials: `admin / admin`

## Project Structure

```
observability-stack/
├── docker-compose.yml
├── app/
│   ├── app.py
│   └── Dockerfile
├── prometheus/
│   └── prometheus.yml
└── grafana/
    └── provisioning/
        ├── datasources/
        │   └── datasource.yml
        └── dashboards/
            ├── dashboard.yml
            └── app-dashboard.json
```
