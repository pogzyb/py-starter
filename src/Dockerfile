FROM python:3.7-alpine

RUN apk update && \
    apk upgrade && \
    apk add \
    bash

ENV HOME /code

COPY ./src/ ${HOME}/src/
WORKDIR ${HOME}/src

RUN pip install -r requirements.txt --upgrade pip

COPY ./run.sh /usr/local/bin/run.sh
RUN chmod u+x /usr/local/bin/run.sh

EXPOSE ${APP_PORT}

CMD ["/usr/local/bin/run.sh"]