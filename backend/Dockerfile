FROM python:slim
RUN mkdir /opt/backend
WORKDIR /opt/backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn","-b","0.0.0.0", "-p", "8000", "app:app"]