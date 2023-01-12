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

RUN apk add --update openssl && \
    rm -rf /var/cache/apk/*

# Sets Python environment
ENV PATH="/app/myenv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt --use-pep517

# Generating fresh TLS certificates
COPY TLS_certificate_generator_bot.sh .
RUN chmod +x TLS_certificate_generator_bot.sh
RUN ./TLS_certificate_generator_bot.sh

# Sets container's process
COPY . .

EXPOSE 443

ENTRYPOINT ["python3", "judicial_bot.py"]