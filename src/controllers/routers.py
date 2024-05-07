"""Create router for API"""
# Standard Library
import sys
import inspect

# My Stuff
from src.controllers import *  # noqa

from fastapi import APIRouter


router = APIRouter(prefix="/api")
all_routers = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
for _, value in all_routers:
    if str(inspect.signature(value) == "()"):
        router.include_router(value())
