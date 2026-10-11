from fastapi import FastAPI

app = FastAPI(
    title="DevOps Platform API",
    description="Учебное приложение для практики DevOps",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "devops-platform",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
