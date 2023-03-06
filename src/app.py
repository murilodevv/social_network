from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def hello():
    return {"Hello!!"}