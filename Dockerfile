FROM python:3
MAINTAINER Augustin Barbe <augustin.barbe@gmail.com>

ENV INSTALL_PATH /chess-ai
RUN mkdir ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --editable .

ARG color
ARG bot_id
ARG game_id

ENV COLOR_BOT=${color} \
    GAME_ID=${game_id} \
    ID_BOT=${bot_id}

CMD python run.py
