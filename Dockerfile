FROM python:3.12.5

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "run.py"]
