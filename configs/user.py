from configs.base import BaseConfig


class UserConfig(BaseConfig):
    CASH_AMOUNT = {'type': float, 'default': 0}
    BANK_AMOUNT = {'type': float, 'default': 0}
    MONTHLY_FOOD_LIMIT = {'type': float, 'default': 0}
    MONTHLY_THINGS_LIMIT = {'type': float, 'default': 0}
    CURRENCY = {'type': str, 'default': 'USD'}
