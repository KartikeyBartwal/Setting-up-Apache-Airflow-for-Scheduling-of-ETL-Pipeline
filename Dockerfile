FROM apache/airflow:2.0.1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
