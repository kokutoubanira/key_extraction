FROM python:3.9

COPY ./src /src
WORKDIR /src
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/boudinfl/pke.git
EXPOSE 8051