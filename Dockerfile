FROM debian

RUN apt update -y && apt upgrade -y
RUN apt install python3 python3-pip git -y

RUN apt clean -y

RUN mkdir app && cd app && git clone https://github.com/Vinicius-Gustavo-Rodrigues-Abreu/teste-enfileirador.git

CMD python3 /app/teste-enfileirador/main.py
