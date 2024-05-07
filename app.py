# My Stuff
from fastapi import FastAPI

from src.controllers.routers import router

app = FastAPI(
    title="Mongo Tesing API",
    summary="A sample application showing how to use FastAPI to add a ReST API to a MongoDB collection.",
)

app.include_router(router)
