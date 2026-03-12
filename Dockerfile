FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

WORKDIR /app

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    openjdk-17-jdk

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

# تشغيل السيرفر
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]