from fastapi import FastAPI

from api.router import router


app = FastAPI()
app.router.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
