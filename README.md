# Real-Time Healthcare IoT Monitoring (Prometheus + Grafana)

This project is a software-only simulation of healthcare IoT monitoring. It uses:
- Prometheus to scrape and store metrics
- Grafana to visualize and alert
- A Python-based sensor simulator that exposes metrics on /metrics

## Files included
- docker-compose.yml
- prometheus.yml
- sensor_simulator.py
- requirements.txt
- sensor-simulator/Dockerfile
- grafana_dashboard.json

## Quick start (you have Docker 28.5.1)

1. Clone or download this project, then:
   ```
   cd healthcare_prometheus_grafana
   docker compose up -d --build
   ```

2. Open services:
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000 (admin/admin)
   - Sensor metrics: http://localhost:8000/metrics

3. In Grafana: Add Prometheus data source
   - URL: http://prometheus:9090
   - Save & Test

4. Import dashboard:
   - Grafana -> Dashboards -> Import -> Upload grafana_dashboard.json

## Generate PDF of this README (optional)
If you want a PDF copy of this README ("Real-Time Healthcare IoT Monitoring (Prometheus + Grafana Version)"), you can convert it locally:

Option A: Using pandoc (recommended)
- Install pandoc (https://pandoc.org/)
- Run:
  ```
  pandoc README.md -o Real-Time-Healthcare-IoT-Monitoring.pdf
  ```

Option B: Using Google Chrome / Browser
- Open README.md in VSCode or a browser extension that renders markdown.
- Print -> Save as PDF.

## Notes & Next steps
- To run multiple simulated patients: copy sensor_simulator.py and run multiple containers with different targets.
- To add alerts: create Grafana Alert Rules (e.g., temperature > 37.5°C).
- Need help? Reply and I can add email/Slack alerting, multiple patients, or containerized simulator auto-restart.
