### python tracing

# package requirement
- pipenv install fastapi
- pipenv install 'uvicorn[standard]'
- pipenv install opentelemetry-distro opentelemetry-exporter-otlp opentelemetry-instrumentation-fastapi

# run application
- opentelemetry-instrument --metrics_exporter none --traces_exporter console,otlp --exporter_otlp_traces_insecure true --exporter_otlp_endpoint localhost:4317 --service_name test python main.py

# run with docker
1. docker build -t test:dev --no-cache .
2. docker compose up -d
3. docker run -it -p 8000:8000 --network tracing_default --name test --rm test:dev opentelemetry-instrument --metrics_exporter none --traces_exporter console,otlp --exporter_otlp_traces_insecure true --exporter_otlp_endpoint tempo:4317 --service_name test python main.py
