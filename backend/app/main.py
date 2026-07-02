from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SHL AI Assessment Recommender",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "SHL AI Assessment Recommender API",
        "docs": "/docs",
        "health": "/health"
    }


app.include_router(router)