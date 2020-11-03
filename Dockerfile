FROM python:3.8-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx libgtk2.0-dev

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

ENV DISPLAY host.docker.internal:0

CMD ["python", "/app/main.py"]