from fastapi import FastAPI

app = FastAPI()


@app.get("/images/")
async def images(q: str, exclude: list = []):
    return {"message": q, "exclude": exclude}