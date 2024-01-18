from fastapi import FastAPI
from dependencies import Container
from worker import create_celery_app

app = FastAPI()
container = Container()
container.wire(modules=[__name__])
celery_app = create_celery_app()


@app.get("/")
async def read_root():
    celery_app.send_task("worker.test_task")
    return {"message": "Task dispatched"}
