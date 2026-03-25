from aiogram import Router

from src.handlers.cancel import router as cancel_router
from src.handlers.start import router as start_router

all_routers = Router(name="all_routers")


all_routers.include_routers(
    start_router,
    cancel_router,
)
