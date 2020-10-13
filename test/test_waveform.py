import sys
import os
import unittest

sys.path.insert(0, os.path.abspath("."))
from appteka.pyqt import testing
from appteka.pyqtgraph.waveform import Waveform


class TestWaveform(unittest.TestCase):
    """Test suite for Waveform widget."""
    def test_xlabel(self):
        app = testing.TestApp(self)

        w = Waveform(xlabel="Time [sec]")

        app(w, [
            "x label is 'Time [sec]'",
        ])

    def test_time_axis_false(self):
        app = testing.TestApp(self)

        w = Waveform(time_axis=False)
        w.update_data([0, 1, 2, 3], [1, 2, 1, 2])

        app(w, [
            "x values are usual numbers from 0 to 3",
        ])

    def test_time_axis_true(self):
        app = testing.TestApp(self)

        w = Waveform(None, time_axis=True)
        w.update_data([0, 1, 2, 3], [1, 2, 1, 2])

        app(w, [
            "x values are time values",
        ])

    def test_scaling(self):
        app = testing.TestApp(self)

        w = Waveform()
        w.update_data([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [1, 2, 0, 3, 1, 2, 3, 4, 1, 3])

        app(w, [
            "both axis scaling with mouse wheel",
            "x-scaling with CONTROL pressed",
            "y-scaling with SHIFT pressed",
        ])
