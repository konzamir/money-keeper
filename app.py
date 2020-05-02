from celery import Celery

from configs import celery_config
from tasks import GetUpdatesTask


def check_imports():
    try:
        from configs.db import DBConfig
        from configs.telegram import TelegramConfig
    except ImportError as err:
        raise Exception(
            'Rename `configs/*.py-example` to '
            '`configs/*.py` and set necessary '
            'configs there!') from err


if __name__ == "__main__":
    check_imports()
    print(celery_config.get('BROKER_URL'))
    # app = Celery('money_keeper')
    # app.config_from_object(CeleryConfig())
    #
    # app.register_task(GetUpdatesTask())
