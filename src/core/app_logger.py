import logging
import logging.handlers
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Основной лог-файл
LOG_FILE = LOG_DIR / "app.log"

def setup_logger(name: str = "velora", log_file: str = LOG_FILE, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Формат сообщений в логе
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Консольный обработчик (StreamHandler)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)  # в консоль выводим INFO и выше
    ch.setFormatter(formatter)

    # Файловый обработчик с ротацией по размеру (RotatingFileHandler)
    fh = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5, encoding='utf-8'
    )
    fh.setLevel(level)  # в файл пишем с уровнем level (обычно DEBUG)
    fh.setFormatter(formatter)

    # Добавляем обработчики, если они ещё не добавлены (чтобы избежать дублей)
    if not logger.hasHandlers():
        logger.addHandler(ch)
        logger.addHandler(fh)

    # Отключаем распространение логов вверх по иерархии (чтобы не дублировались)
    logger.propagate = False

    return logger

# Инициализация логгера при импорте
logger = setup_logger()
