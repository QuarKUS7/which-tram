FROM python:3.6-alpine
WORKDIR /app

RUN apk --update add --no-cache g++ chromium chromium-chromedriver

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
