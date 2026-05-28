FROM python:3.12-slim
WORKDIR /app
RUN pip install fastapi uvicorn
COPY . .
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]