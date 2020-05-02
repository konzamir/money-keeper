from configs.commands import CommandsConfig
from configs.states import StatesConfig
from configs.db import DBConfig
from configs.telegram import TelegramConfig


class AppConfig(
        CommandsConfig, StatesConfig,
        DBConfig, TelegramConfig):
    pass
