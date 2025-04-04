FROM ubuntu:24.04
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive TZ=Europe/Moscow

RUN apt update && apt install -y curl ffmpeg
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY . .

EXPOSE 8000