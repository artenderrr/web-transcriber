FROM ubuntu:24.04
WORKDIR /app

RUN apt update && apt install -y curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY . .

EXPOSE 8000