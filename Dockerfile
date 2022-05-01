FROM python:3.9.1
ADD . /
WORKDIR /
RUN pip install -r requirements.txt
CMD python app.py