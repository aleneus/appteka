# appteka - helpers collection

# Copyright (C) 2018-2025 Aleksandr Popov

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
""" This module implements the SimpleSignal class which makes the
event handling more convenient. """


class SimpleSignal:
    """Provides simple signals and slots mechanism."""

    def __init__(self):
        """Constructor.

        Create empty list of connected function.
        """
        self.slots = []

    def emit(self, *args):
        """Emit signal."""
        for func in self.slots:
            if func:
                func(*args)

    def connect(self, slot):
        """Connect signal with slot.

        Parameters
        ----------
        slot
            Function to be connected with signal.
        """
        for i, _ in enumerate(self.slots):
            if self.slots[i] == slot:
                return

            if self.slots[i] is None:
                self.slots[i] = slot
                return

        self.slots.append(slot)

    def disconnect(self, slot):
        """Disconnect slot from signal.

        Parameters
        ----------
        slot
            Name of connected function.
        """
        for i, _ in enumerate(self.slots):
            if self.slots[i] == slot:
                self.slots[i] = None
