FROM python:3.10.4

RUN apt-get update && apt-get -y install nano

ADD ./requirements.txt /home/software/

ENV DEBUG=False

WORKDIR /home/software

RUN pip install -r /home/software/requirements.txt

ADD . /home/software

RUN chmod +x ./docker-entrypoint.sh


CMD ["./docker-entrypoint.sh"]
