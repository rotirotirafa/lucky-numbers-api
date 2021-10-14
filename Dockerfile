
FROM python:3.9


WORKDIR /src


COPY ./requirements.txt /src/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt


COPY . .

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]
