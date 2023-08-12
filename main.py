import uvicorn
from fastapi import FastAPI, HTTPException, status
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

FastAPIInstrumentor.instrument_app(app)

@app.get("/health")
def root():
    raise HTTPException(
        status_code = status.HTTP_200_OK,
        detail = "Service OK"
    )

def main():
    uvicorn.run(app, host = "0.0.0.0", port = 8000)

if __name__ == "__main__":
    main()
