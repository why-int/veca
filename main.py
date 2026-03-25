import asyncio

from src.core.app_context import app_context
from src.core.app_logger import logger


async def main() -> None:
    logger.info(msg="Запуск приложения...")
    await app_context.setup()
    logger.info(msg="Приложение остановлено.")


if __name__ == "__main__":
    try:
        asyncio.run(main=main())
    except Exception as e:
        logger.exception(msg=f"Ошибка при запуске: {e}")
