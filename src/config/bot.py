from .base import BaseConfig


class BotConfig(BaseConfig):
    TOKEN: str = "TOKEN"


    class Config:
        env_prefix = "BOT_"
