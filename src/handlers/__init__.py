from aiogram import Router

from src.handlers.callbacks import callbacks_router
from src.handlers.commands import commands_router

main_router = Router()

main_router.include_routers(
    commands_router,
    callbacks_router,
)
