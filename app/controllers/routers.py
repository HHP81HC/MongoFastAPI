"""Create router for API"""
# Standard Library
import sys
import inspect

from fastapi import APIRouter

from .student_repository.router import get_student_router


router = APIRouter(prefix="/api")
all_routers = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
for _, value in all_routers:
    if str(inspect.signature(value) == "()"):
        router.include_router(value())
