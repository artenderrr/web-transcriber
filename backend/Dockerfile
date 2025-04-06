FROM ubuntu:24.04
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive TZ=Europe/Moscow

RUN apt update && apt install -y curl ffmpeg
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

RUN apt install -y python3 python3-pip
RUN pip3 install openai-whisper --break-system-packages
RUN python3 -c "import whisper ; whisper.load_model('small')"

COPY pyproject.toml ./
RUN /root/.local/bin/uv venv
RUN /root/.local/bin/uv pip install -r pyproject.toml

COPY . .

EXPOSE 8000