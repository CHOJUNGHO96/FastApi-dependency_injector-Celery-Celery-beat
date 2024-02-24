# FastAPI + Dependency Injector + Celery Project

This project serves as a reference implementation using FastAPI, Dependency Injector, and Celery.

## Installation and Execution
1. Ensure Docker and Docker Compose are installed.
2. Clone this repository: `git clone [GitHub Repository URL]`
3. Launch the services with the following command: `docker-compose up --build`
4. Access the application in your browser at `localhost:8000.`

## 환경 변수
- `CELERY_BROKER_URL`: The broker URL for Celery (e.g.,` redis://redis:6379/0`)

## Execution Test
### The worker-beat runs at scheduled intervals (set to every 10 seconds) as configured in celery_app.conf.beat_schedule
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-Celery-Celery-beat/assets/61762674/4d8a7768-d08a-472c-ab9c-a6ab81726f78)

### When a Celery task API request is made from the WEB, the Celery worker executes
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-Celery-Celery-beat/assets/61762674/0da94425-e1ce-48d9-8b90-5f6c4bea25dd)
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-Celery-Celery-beat/assets/61762674/9c8bb460-7cfa-458b-8ae0-d9d1fc51ff95)

