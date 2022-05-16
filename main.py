import signal
import sys
import time
from typing import Iterable


class Queueer:

    def __init__(self, objects: Iterable):
        self.objects = objects
        self.last_idx_proc = 0

    def enqueue():
        ...

    def handle_exit(self, *_):
        ...


class TestQueueer(Queueer):

    def enqueue(self):
        for i, _ in enumerate(self.objects):
            print(f'[+] Enfilerando {i}...', flush=True)
            time.sleep(1.5)
            self.last_idx_proc = i

    def handle_exit(self, *_):
        queued = self.objects[:self.last_idx_proc + 1]
        missing = self.objects[self.last_idx_proc + 1:]

        print(f'[*] Enfileirou {len(queued)} ids...', flush=True)
        print(f'[*] Faltou enfileirar {len(missing)} ids...', flush=True)

        sys.exit(1)


def execute():
    print("-" * 100, flush=True)
    print("SINAIS SAÍDA NOS PROCESSOS DE ENFILEIRAMENTO".center(100), flush=True)
    print("-" * 100, flush=True)

    queueer = TestQueueer([i for i in range(5000)])

    signal.signal(signal.SIGINT, queueer.handle_exit)
    signal.signal(signal.SIGTERM, queueer.handle_exit)
    signal.signal(signal.SIGQUIT, queueer.handle_exit)

    while True:
        queueer.enqueue()
        time.sleep(5)


if __name__ == '__main__':
    execute()
