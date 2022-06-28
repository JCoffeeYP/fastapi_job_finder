from api.v1 import route_general_pages, route_jobs, route_users
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(
    route_general_pages.general_pages_router,
    prefix="",
    tags=["general_pages"]
)
api_router.include_router(
    route_users.router,
    prefix="/users",
    tags=["users"]
)
api_router.include_router(
    route_jobs.router,
    prefix="/jobs",
    tags=["jobs"]
)
