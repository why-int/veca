__all__ = ["settings"]

from .bot import BotConfig


class Settings:
    bot = BotConfig()

settings = Settings()