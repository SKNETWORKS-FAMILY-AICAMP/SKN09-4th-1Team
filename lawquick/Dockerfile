# 1. Python 베이스 이미지 선택
FROM python:3.12

# 2. 파이썬 캐시 및 버퍼링 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. 작업 디렉토리 생성
WORKDIR /app

# 4. requirements 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 전체 프로젝트 복사
COPY . .

# 6. static 파일 수집
RUN python manage.py collectstatic --noinput

# 7. Gunicorn 서버로 실행
CMD ["gunicorn", "lawquick.wsgi:application", "--config", "gunicorn.conf.py"]
