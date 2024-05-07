# My Stuff
from src.mongo_api.controllers.routers import router

from fastapi import FastAPI


app = FastAPI(
    title="Mongo Tesing API",
    summary="A sample application showing how to use FastAPI to add a ReST API to a MongoDB collection.",
)

app.include_router(router)
