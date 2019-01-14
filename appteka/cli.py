"""Helpers for CLI."""

import time
import sys


class ProgressMessages:
    """This class provides the console progress messages in format:

    Some operation ... ready [n sec].
    """
    def __init__(self, digits=1):
        self.start_time = None
        self.digits = digits

    def begin(self, message):
        """Show start part of message and three points."""
        self.start_time = time.time()
        sys.stdout.write("{} ... ".format(message))
        sys.stdout.flush()

    def end(self):
        """Show end part of message."""
        end_time = round(time.time()-self.start_time, self.digits)
        sys.stdout.write("ready [{} sec]\n".format(end_time))
