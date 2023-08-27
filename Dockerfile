# Базовый образ Python
FROM python:3.9
# Переменная окружения для отключения вывода буферизации Python
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
