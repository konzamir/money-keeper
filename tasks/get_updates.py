from celery import Task


class GetUpdatesTask(Task):
    name = 'get_updates'

    def run():
        return 'test'
