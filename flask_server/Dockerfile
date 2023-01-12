# temp stage
FROM python:3-alpine as builder

# Sets directory
WORKDIR /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Updates all Alpine packages
RUN apk update && \
    apk upgrade

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Creates Python environment
RUN python3 -m venv /app/myenv
ENV PATH="/app/myenv/bin:$PATH"

# Install pip requirements from the file via bash command "pip freeze > requirements.txt"
RUN pip install --upgrade pip


# final stage
FROM python:3-alpine

# Sets directory
WORKDIR /app

# Creates multistage build
COPY --from=builder /app/myenv /app/myenv

# Sets Python environment
ENV PATH="/app/myenv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt --use-pep517

# Sets container's process
COPY . .

EXPOSE 5000

ENTRYPOINT ["python3", "flask_server.py"]