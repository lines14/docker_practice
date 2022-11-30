FROM python

WORKDIR /app

COPY . .

CMD ["python", "docker_test.py"]