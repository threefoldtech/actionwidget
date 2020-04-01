FROM python:slim
RUN mkdir /opt/backend
WORKDIR /opt/backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app"]