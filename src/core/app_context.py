from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config import settings
from src.core.app_logger import logger
from src.handlers.callbacks import callbacks_router
from src.handlers.commands import commands_router


async def on_startup() -> None:
    logger.info(msg="Бот запущен")


class AppContext:
    def __init__(self) -> None:
        self.bot: Bot = Bot(
            token=settings.bot.TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )
        self.dp: Dispatcher = Dispatcher()
        self.dp.startup.register(callback=on_startup)

    async def setup(self) -> None:
        # Инициализация основного роутера который включает в себя все роутеры
        logger.info(msg="Инициализация роутеров...")
        self.dp.include_routers(
            commands_router,
            callbacks_router,
        )
        logger.info(msg="Роутеры инициализарованны.")

        # Запуск телеграм бота
        logger.info(msg="Запуск бота (start polling)...")
        await self.dp.start_polling(self.bot)
        logger.info(msg="Бот остановлен (polling stop).")


app_context = AppContext()
