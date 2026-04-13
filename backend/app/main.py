from fastapi import FastAPI

app = FastAPI(title="Pulse API")

@app.get("/")
def root():
    return {"message": "Pulse API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}