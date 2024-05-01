from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status":"Success","message":"Server Running Successfully"}

