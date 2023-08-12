### python tracing

# package requirement
pipenv install fastapi
pipenv install 'uvicorn[standard]'
pipenv install opentelemetry-distro opentelemetry-exporter-otlp opentelemetry-instrumentation-fastapi

# run application
opentelemetry-instrument --metrics_exporter none --traces_exporter console,otlp --exporter_otlp_traces_insecure true --exporter_otlp_endpoint localhost:4317 --service_name test python main.py
