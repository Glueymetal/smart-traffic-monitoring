FROM python:3.11-slim

WORKDIR /cloud

COPY sensor_readings.py .

CMD ["python","-u","sensor_readings.py"]

