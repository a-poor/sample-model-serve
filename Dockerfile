FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN python make-model.py

EXPOSE 8000

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "serve-model:app" ]
