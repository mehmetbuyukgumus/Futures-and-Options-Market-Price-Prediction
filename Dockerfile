FROM python:3.12.5

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

# Uygulamanın çalıştırılma komutu
CMD ["python3", "run.py"]
