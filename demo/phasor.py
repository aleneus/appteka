import sys

from PyQt5 import QtWidgets

import sys
import os

sys.path.insert(0, os.path.abspath("."))

from appteka.pyqt import gui
from appteka.pyqtgraph import phasor


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__make_gui()

    def __make_gui(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        self.phw = gui.add_widget(phasor.PhasorDiagram(), main_layout)

    def draw_phasors(self):
        self.phw.draw_phasor(1, 0.5)
        self.phw.draw_phasor(2, 0.7)
        self.phw.draw_phasor(3, 0.9)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    d = Dialog()
    d.show()
    d.draw_phasors()
    sys.exit(app.exec())
