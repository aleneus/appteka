# appteka - helpers collection

# Copyright (C) 2018-2019 Aleksandr Popov

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

import math

import pyqtgraph as pg


class PhasorDiagram(pg.PlotWidget):
    def __init__(self):
        super().__init__()
        self.setAspectLocked()
        self.addLine(x=0, pen=0.2)
        self.addLine(y=0, pen=0.2)

        circle = pg.QtGui.QGraphicsEllipseItem(-0.5, -0.5, 0.5*2, 0.5*2)
        circle.setPen(pg.mkPen(0.2))
        self.addItem(circle)

        circle = pg.QtGui.QGraphicsEllipseItem(-1, -1, 1*2, 1*2)
        circle.setPen(pg.mkPen(0.2))
        self.addItem(circle)

    def draw_phasor(self, am, ph):
        x = am * math.cos(ph)
        y = am * math.sin(ph)
        self.plot([0, x], [0, y])
