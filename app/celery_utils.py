def init_celery(celery, app):
    backend = app.config["CELERY_RESULT_BACKEND"]
    broker = app.config["CELERY_BROKER_URL"]
    beatschedule = app.config["CELERYBEAT_SCHEDULE"]
    # celery = Celery(app.import_name, backend=backend, broker=broker)
    celery.conf.broker_url = broker
    celery.conf.result_backend = backend
    celery.conf.beat_schedule = beatschedule
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
