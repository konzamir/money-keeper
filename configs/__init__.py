from .commands import CommandsConfig
from .states import StatesConfig
from .user import UserConfig

try:
    from .db import DBConfig
    from .telegram import TelegramConfig
except ImportError as err:
    raise Exception(
        'Rename `configs/*.py-example` to '
        '`configs/*.py` and set necessary '
        'configs there!') from err


__all__ = [
    'CommandsConfig', 'StatesConfig', 'UserConfig',
    'DBConfig', 'TelegramConfig'
]
