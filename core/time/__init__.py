#
# Author: Rohtash Lakra
#
import time


class Timer:

    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._end = time.time()
        self.duration = self._end - self._start

    def get_duration(self) -> float:
        return self.duration

if __name__ == '__main__':
    timer = Timer()
    timer.enter()
    timer.end()
    print(timer.get_duration())
