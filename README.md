# FastAPI + Dependency Injector + Celery 프로젝트

이 프로젝트는 FastAPI, Dependency Injector, Celery를 사용하여 구현하는데 참고할수있는 프로젝트입니다.

## 설치 및 실행 방법
1. Docker 및 Docker Compose가 설치되어 있는지 확인하세요.
2. 이 리포지토리를 클론하세요: `git clone [GitHub 리포지토리 URL]`
3. 다음 명령으로 서비스를 실행하세요: `docker-compose up --build`
4. 브라우저에서 `localhost:8000`으로 애플리케이션에 접속하세요.

## 환경 변수
- `CELERY_BROKER_URL`: Celery의 브로커 URL (예: `redis://redis:6379/0`)

## 실행TEST
### celery_app.conf.beat_schedule 에 설정된 스케쥴(10초로 설정)마다 worker-beat 가 실행
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-Celery-Celery-beat/assets/61762674/4d8a7768-d08a-472c-ab9c-a6ab81726f78)

### WEB에서 celery 작업 api요청시 celery worker가 실행
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-Celery-Celery-beat/assets/61762674/0da94425-e1ce-48d9-8b90-5f6c4bea25dd)
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-Celery-Celery-beat/assets/61762674/9c8bb460-7cfa-458b-8ae0-d9d1fc51ff95)

