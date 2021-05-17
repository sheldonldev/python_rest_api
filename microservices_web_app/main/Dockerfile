FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.text /app/requirements.text
RUN pip install -r requirements.txt
COPY . /app
CMD python main.py
