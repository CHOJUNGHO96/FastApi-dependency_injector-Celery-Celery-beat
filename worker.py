from celery import Celery
from dependencies import Container


def create_celery_app() -> Celery:
    container: Container = Container()
    container.config.celery.broker_url.from_env("CELERY_BROKER_URL", "redis://:redis!123@127.0.0.1:6379/0")
    _celery_app = container.celery_app()
    return _celery_app


celery_app = create_celery_app()


@celery_app.task
def test_task():
    print("테스트")


# Celery Beat 설정
celery_app.conf.beat_schedule = {
    "test-task-every-10-seconds": {"task": "worker.test_task", "schedule": 10.0},
}
