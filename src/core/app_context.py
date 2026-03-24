from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config import settings
from src.handlers import main_router


class AppContext:
    def __init__(self) -> None:
        self.bot: Bot = Bot(
            token=settings.bot.TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )
        self.dp: Dispatcher = Dispatcher()

    async def setup(self) -> None:
        # Инициализация основного роутера который включает в себя все роутеры
        self.dp.include_router(router=main_router)


app_context = AppContext()
