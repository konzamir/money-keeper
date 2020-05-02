from celery.schedules import crontab

from configs.db import DBConfig as db_config


class CeleryConfig:
    IMPORTS = ("tasks",)
    ACCEPT_CONTENT = ['application/json']
    RESULT_SERIALIZER = 'json'
    TASK_SERIALIZER = 'json'
    TIMEZONE = 'Europe/Kiev'
    MONGODB_SCHEDULER_DB = "celery"
    MONGODB_SCHEDULER_COLLECTION = "schedules"
    BROKER_URL = f'mongodb://{db_config.DB_USER}:{db_config.DB_PASS}@{db_config.DB_HOST}:{db_config.DB_PORT}'
    TASK_ROUTES = {
        "get_updates": {
            'queue': 'task_get_updates',
        }
    }
    BEAT_SCHEDULE = {
        'get_updates': {
            'task': 'get_updates',
            'schedule': 3
        }
    }
