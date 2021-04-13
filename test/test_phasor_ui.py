import unittest
from PyQt5 import QtCore
from pyqtgraph import setConfigOption

from appteka.pyqt import testing
from appteka.pyqtgraph.phasor_ui import PhasorDiagramUI

setConfigOption("antialias", True)


class TestPhasorDiagramUI(unittest.TestCase):
    def test_u_and_i(self):
        app = testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_i(3, 'i0', color=(255, 255, 0), width=2)
        d.add_i(4, 'i0', color=(255, 0, 0), width=2)
        d.add_i(5, 'i0', color=(0, 255, 0), width=2)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)
        d.update_data(3, 1, 1)
        d.update_data(4, 1.2, 3)
        d.update_data(5, 1.1, 5)

        app(d, [
            "Grid OK",
            "Legend OK",
            "3 U phasors",
            "3 I phasors",
        ])

    def test_only_u(self):
        app = testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        app(d, [
            "Grid OK",
            "3 U phasors",
        ])

    def test_only_i(self):
        app = testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_i(3, 'i0', color=(255, 255, 0), width=2)
        d.add_i(4, 'i0', color=(255, 0, 0), width=2)
        d.add_i(5, 'i0', color=(0, 255, 0), width=2)

        d.update_data(3, 1, 1)
        d.update_data(4, 1.2, 3)
        d.update_data(5, 1.1, 5)

        app(d, [
            "Grid OK",
            "3 I phasors",
        ])

    def test_add_u_repeat_key(self):
        testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_u(0, 'u0')
        with self.assertRaises(ValueError):
            d.add_u(0, 'u0')

    def test_set_visible(self):
        app = testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        d.set_visible(1, False)
        d.set_visible(2, False)
        d.set_visible(2, True)

        app(d, [
            "Legend: u0, u1, u2",
            "2 U phasors",
        ])

    def test_remove_phasors(self):
        app = testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        d.set_visible(1, False)
        d.remove_phasors()

        app(d, ["Only grid"])

    def test_remove_phasors_and_add_again(self):
        app = testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        d.set_visible(1, False)
        d.remove_phasors()

        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        app(d, ["No smoke"])

    def this_test_text(self):
        app = testing.TestApp(self)
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        d.set_text("50.01")

        app(d, ["Text: 50.01"])
