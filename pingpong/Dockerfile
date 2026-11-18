FROM python:3.16.0a2-slim
WORKDIR /usr/src/app
COPY . .
ENV PYTHONUNBUFFERED=1
RUN pip install Flask
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install psycopg2
CMD ["python", "pingpong.py"]