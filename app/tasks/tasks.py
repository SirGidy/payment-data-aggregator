from app import celery


@celery.task(name="import_from_third_parties")
# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
def import_data():
    logger.info(f"successfully imported data")
