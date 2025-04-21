# 베이스 이미지
FROM python:3.10

# 작업 디렉토리 생성
WORKDIR /app

# 필요 파일 복사
COPY . /app

# 의존성 설치
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# 마이그레이션 후 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]