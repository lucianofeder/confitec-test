FROM python:latest

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "./entrypoint.sh"]

EXPOSE 8000
