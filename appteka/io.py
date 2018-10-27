# appteka - helpers collection

# Copyright (C) 2018 Aleksandr Popov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.

# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Writing data to IO text buffer using queue and working in separate
thread."""


from collections import deque
from threading import Thread, Lock, Event
from time import sleep


class QueuedWriter:
    """Tool for record data to text buffer using queue and thread."""
    def __init__(self, buff=None):
        self._buff = buff
        self._queue = deque([])
        self._lock = Lock()
        self._must_write = False
        self._convert_func = {
            'name': lambda x: x,
            'kwargs': {},
        }

    def set_buff(self, buff):
        """Set IO buffer."""
        self._buff = buff

    def set_convert_func(self, func, **kwargs):
        """Set function for convertion data sample to string."""
        self._convert_func = {
            'name': func,
            'kwargs': kwargs,
        }

    def save_queue(self):
        """Move data from queue to buffer."""
        while len(self._queue) > 0:
            sample = self._queue.popleft()
            line = self._convert_func['name'](
                sample,
                **self._convert_func['kwargs'],
            )
            self._buff.write(line)

    def start_record(self):
        """Start record."""
        self._thread = PyRecordThread()
        self._thread.set_writer(self)
        self._thread.start()

    def stop_record(self):
        """Stop record."""
        self._thread.stop()
        with self._lock:
            self._must_write = False

    def add_data(self, sample):
        """Add data sample."""
        self._queue.append(sample)


class PyRecordThread(Thread):
    """Thread in which samples recorded to IO buffer."""
    def __init__(self):
        super().__init__()
        self._lock = Lock()
        self._must_write = False
        self._can_quit = Event()
        self._writer = None

    def set_writer(self, writer):
        self._writer = writer

    def run(self):
        """Record data from queue to buffer."""
        self._can_quit.clear()
        with self._lock:
            self._must_write = True
        while self._must_write:
            sleep(1)
            self._writer.save_queue()
        self._writer.save_queue()
        self._can_quit.set()

    def stop(self):
        """Stop thread."""
        with self._lock:
            self._must_write = False
        self._can_quit.wait()
        self.join()


def _example():
    from random import randint

    def convert_func(sample):
        """Convert function."""
        return '{}: {}\n'.format(*sample)

    writer = QueuedWriter()
    writer.set_convert_func(convert_func)
    buf = open('output.txt', 'w')
    writer.set_buff(buf)

    i = 0
    while True:
        try:
            sample = (i, randint(0, 100))
            print(sample)
            writer.add_data(sample)
            writer.save_queue()
            sleep(0.02)
            i += 1
        except KeyboardInterrupt:
            print("Good bye...")
            break

    buf.close()


if __name__ == "__main__":
    _example()
