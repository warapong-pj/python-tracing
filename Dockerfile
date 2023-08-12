FROM python:3.8.17-bullseye

EXPOSE 8000
WORKDIR /app

COPY . /app
RUN pip install pipenv && \
        pipenv requirements > requirements.txt && \
        pip install -r requirements.txt

CMD [ "python", "main.py" ]
