FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/estudiantes/data/v1

EXPOSE 5000

CMD ["python", "run.py"]