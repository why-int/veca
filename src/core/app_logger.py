import logging
import logging.handlers
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Основной лог-файл
LOG_FILE: Path = LOG_DIR / "app.log"


def setup_logger(
    name: str = "veca", log_file: Path = LOG_FILE, level: int = logging.DEBUG
) -> logging.Logger:
    logger = logging.getLogger(name=name)
    logger.setLevel(level)

    # Формат сообщений в логе
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Консольный обработчик (StreamHandler)
    ch = logging.StreamHandler()
    ch.setLevel(level=logging.INFO)  # в консоль выводим INFO и выше
    ch.setFormatter(fmt=formatter)

    # Файловый обработчик с ротацией по размеру (RotatingFileHandler)
    fh = logging.handlers.RotatingFileHandler(
        filename=log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    fh.setLevel(level=level)  # в файл пишем с уровнем level (обычно DEBUG)
    fh.setFormatter(fmt=formatter)

    # Добавляем обработчики, если они ещё не добавлены (чтобы избежать дублей)
    if not logger.hasHandlers():
        logger.addHandler(hdlr=ch)
        logger.addHandler(hdlr=fh)

    # Отключаем распространение логов вверх по иерархии (чтобы не дублировались)
    logger.propagate = False

    return logger


# Инициализация логгера при импорте
logger: logging.Logger = setup_logger()
