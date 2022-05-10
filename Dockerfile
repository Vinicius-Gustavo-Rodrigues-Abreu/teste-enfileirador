FROM debian

RUN apt update -y && apt upgrade -y
RUN apt install python3 python3-pip git -y

RUN apt clean -y

RUN mkdir app && cd app && git clone https://gitlab.com/p7705/teste-enfileirador.git && cd teste-enfileirador

RUN python3 main.py
