#
# Author: Rohtash Lakra
#
from random import randint
from threading import Thread
from time import sleep


class Worker(Thread):

    def __init__(self, speed, buffer, daemon: bool = True):
        super().__init__(daemon=daemon)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0

    def __str__(self) -> str:
        return f"Worker <name={self.name}, working={self.working}, progress={self.progress}, speed={self.speed}>"

    def __repr__(self):
        return str(self)

    @property
    def state(self):
        if self.working:
            return f"{self.progress} ({self.progress})"
        return ":Worker: Idle"

    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))

    def simulate_working(self):
        self.working = True
        self.progress = 0
        delay = randint(1, 1 + 15 // self.speed)
        for _ in range(100):
            sleep(delay // 100)
            self.progress += 1
