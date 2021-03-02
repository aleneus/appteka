# appteka - helpers collection

# Copyright (C) 2018-2021 Aleksandr Popov

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

"""Implementation of the phasor diagram."""

import math
import cmath
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

DEFAULT_CIRCLES_NUM = 6


class PhasorDiagram(pg.PlotWidget):
    """Widget for plotting phasor diagram."""

    def __init__(self, parent=None, size=500):
        super().__init__(parent)
        self.setAspectLocked(True)
        self.addLine(x=0, pen=0.2)
        self.addLine(y=0, pen=0.2)
        self.showAxis('bottom', False)
        self.showAxis('left', False)

        self.setFixedSize(size, size)

        self.__build_grid()
        self.__build_labels()

        self.set_range(1)

        self.setMouseEnabled(x=False, y=False)
        self.disableAutoRange()
        self.plotItem.setMenuEnabled(False)
        self.hideButtons()

        self.legend = None

        self.coordinates = {}
        self.items = {}

    def set_range(self, value):
        """Set range of diagram."""
        self.__update_grid(value)
        self.__update_labels(value)

    def __build_grid(self):
        self.circles = []
        for _ in range(DEFAULT_CIRCLES_NUM):
            circle = pg.QtGui.QGraphicsEllipseItem()
            circle.setPen(pg.mkPen(0.2))
            self.circles.append(circle)
            self.addItem(circle)

    def __build_labels(self):
        self.labels = []
        for _ in range(2):
            label = pg.TextItem()
            self.labels.append(label)
            self.addItem(label)

    def __update_grid(self, value):
        for i in range(DEFAULT_CIRCLES_NUM):
            rad = (i + 1) * value / DEFAULT_CIRCLES_NUM
            self.circles[i].setRect(-rad, -rad, rad*2, rad*2)

        self.setRange(QtCore.QRectF(-rad, rad, 2*rad, -2*rad))

    def __update_labels(self, value):
        self.labels[0].setText("{}".format(value / 2))
        self.labels[0].setPos(0, value / 2)
        self.labels[1].setText("{}".format(value))
        self.labels[1].setPos(0, value)

    def add_phasor(self, name, am=0, ph=0, color=(255, 255, 255), width=1):
        """Add phasor to the diagram."""

        # add coordinates
        self.coordinates[name] = {
            'end': cmath.rect(am, ph),
        }

        # add items to be painted
        items = {
            'line': self.plot(),
            'point': self.plot(pen=None, symbolBrush=color,
                               symbolSize=width+5, symbolPen=None,
                               name=name),
        }
        items['line'].setPen(pg.mkPen(color, width=width))
        self.items[name] = items

        self.__update()

    def remove_phasors(self):
        """Remove phasors and legend."""
        for key in self.items:
            self.removeItem(self.items[key]['point'])
            self.removeItem(self.items[key]['line'])

        self.coordinates = {}

        # remove legend
        if self.legend is not None:
            self.legend.scene().removeItem(self.legend)
        self.legend = None

    def update_phasor(self, name, am, ph):
        """Change phasor value."""
        self.coordinates[name]['end'] = cmath.rect(am, ph)
        self.__update()

    def __update(self):
        for key in self.coordinates:
            data = self.coordinates[key]
            x = data['end'].real
            y = data['end'].imag

            items = self.items[key]
            items['line'].setData([0, x], [0, y])
            items['point'].setData([x], [y])

    def show_legend(self):
        """Show legend."""
        self.legend = self.plotItem.addLegend()
        for key in self.items:
            self.plotItem.legend.addItem(
                self.items[key]['line'], key)
