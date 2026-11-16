FROM python:3.16.0a2-alpine3.23
WORKDIR /usr/src/app
COPY . .
ENV PYTHONUNBUFFERED=1
RUN pip install Flask && pip install requests
CMD ["python", "app.py"]