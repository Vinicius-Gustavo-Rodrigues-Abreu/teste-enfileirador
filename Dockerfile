FROM python

WORKDIR /app

RUN git clone https://github.com/Vinicius-Gustavo-Rodrigues-Abreu/teste-enfileirador.git

CMD python3 teste-enfileirador/main.py
