import asyncio

from src.core.app_context import app_context
from src.core.app_logger import logger


async def main() -> None:
    logger.info(msg="Запуск приложения...")
    await app_context.setup()
    await app_context.dp.start_polling(app_context.bot)
    logger.info(msg="Polling завершён — бот остановлен")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception(f"Ошибка при запуске: {e}")
