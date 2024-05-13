FROM python:3.12.2-alpine3.19

ADD main.py .

RUN pip install rethinkdb

CMD ["python", "./main.py"] 
