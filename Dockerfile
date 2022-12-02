# temp stage
FROM python:3-slim as builder

# Sets directory
WORKDIR /app

# Removes Debian warning
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NOWARNINGS="yes"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Updates all Debian packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Creates Python environment
RUN python3 -m venv /home/appuser/projects/myenv
ENV PATH="/home/appuser/projects/myenv/bin:$PATH"

# Install pip requirements from the file via "pip freeze > requirements.txt"
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# final stage
FROM python:3-slim

# Creates multistage build
COPY --from=builder /home/appuser/projects/myenv /home/appuser/projects/myenv

# Sets directory
WORKDIR /app

# Sets Python environment
ENV PATH="/home/appuser/projects/myenv/bin:$PATH"

# Sets container's process
COPY . /app

CMD ["python3", "docker_test.py"]