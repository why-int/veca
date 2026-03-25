from aiogram import Router

from src.handlers.commands.cancel_command import router as cancel_command_router
from src.handlers.commands.start_command import router as start_command_router

commands_router = Router(name="commands_router")


commands_router.include_routers(
    start_command_router,
    cancel_command_router,
)
