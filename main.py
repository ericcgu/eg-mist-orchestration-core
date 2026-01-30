from fastapi import FastAPI

app = FastAPI(
    title="Juniper Mist Mega Lab Deployment API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/status")
async def status():
    return {"status": "ok"}