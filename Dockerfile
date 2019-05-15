FROM python:2.7.16-alpine3.9

WORKDIR /usr/src/app

ADD requirement.txt /usr/src/app

RUN pip install -r requirement.txt

ADD demo.py /usr/src/app

CMD tail -f /dev/null &
