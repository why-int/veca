import asyncio

from src2.core.app_context import app_context
from src2.core.app_logger import logger


async def main():
    logger.info("Запуск приложения...")
    await app_context.setup()
    await app_context.dp.start_polling(app_context.bot)
    logger.info("Polling завершён — бот остановлен")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception(f"Ошибка при запуске: {e}")
