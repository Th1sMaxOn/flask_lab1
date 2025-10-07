FROM python:3.11.9-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . /app

ENV PORT=8080
CMD ["sh","-c","flask --app app run -h 0.0.0.0 -p ${PORT}"]
