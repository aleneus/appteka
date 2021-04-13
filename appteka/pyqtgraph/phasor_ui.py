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

from math import degrees
import cmath
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets


DEFAULT_WIDGET_SIZE = QtCore.QSize(500, 500)

DEFAULT_COLOR = (255, 255, 255)
DEFAULT_WIDTH = 1

DEFAULT_MIN_RANGE = 0.001
I_SCALE = 0.7
ROUND_TO = 3


class PhasorDiagramUI(pg.PlotWidget):
    def __init__(self, parent=None, min_range=DEFAULT_MIN_RANGE):
        super().__init__(parent)

        self.setAspectLocked(True)
        self.addLine(x=0, pen=0.2)
        self.addLine(y=0, pen=0.2)
        self.showAxis('bottom', False)
        self.showAxis('left', False)

        policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred,
        )
        policy.setHeightForWidth(True)
        self.setSizePolicy(policy)

        self.setMouseEnabled(x=False, y=False)
        self.disableAutoRange()
        self.plotItem.setMenuEnabled(False)
        self.hideButtons()

        self.__min_range = min_range

        self.__phasors = {}
        self.__items = {}
        self.__names = {}

        self.__to_quant = {}
        self.__amps = {'u': {}, 'i': {}}
        self.__range = {'u': DEFAULT_MIN_RANGE, 'i': DEFAULT_MIN_RANGE}

        self.__init_grid()
        self.__init_labels()

    def add_u(self, key, name=None, **kwargs):
        """Add new U phasor to the diagram."""
        self.__add_phasor(key, name, **kwargs)
        self.__to_quant[key] = 'u'

    def add_i(self, key, name=None, **kwargs):
        """Add new I phasor to the diagram."""
        self.__add_phasor(key, name, **kwargs)
        self.__to_quant[key] = 'i'

    def __add_phasor(self, key, name=None, **kwargs):
        if key in self.__items:
            raise ValueError("repeated key: {}".format(key))

        color = kwargs.get('color')
        if not color:
            color = DEFAULT_COLOR

        width = kwargs.get('width')
        if not width:
            width = DEFAULT_WIDTH

        line = self.plot(pen=pg.mkPen(color, width=width))
        arr = pg.ArrowItem(
            tailLen=0,
            tailWidth=1,
            pen=pg.mkPen(color, width=width),
            headLen=width+4,
            brush=None
        )
        self.addItem(arr)

        self.__items[key] = {'line': line, 'arr': arr}
        self.__names[key] = name

        self.__to_front(self.__label['u'])
        self.__to_front(self.__label['i'])

    def update_data(self, key, amp, phi):
        """Change phasor value."""
        self.__phasors[key] = (amp, phi)
        self.__update()
        self.update_range(key, amp)

    def __update(self):
        for key in self.__phasors:
            phasor = self.__phasors[key]

            compl = None
            quant = self.__to_quant[key]
            if quant == 'i':
                compl = cmath.rect(
                    phasor[0] * self.__i_radius() / self.__range['i'],
                    phasor[1])
            else:
                compl = cmath.rect(phasor[0], phasor[1])

            x = compl.real
            y = compl.imag

            items = self.__items[key]
            items['line'].setData([0, x], [0, y])
            items['arr'].setStyle(angle=180 - degrees(phasor[1]))
            items['arr'].setPos(x, y)

    def update_range(self, key, amp):
        """Update range."""

        quant = self.__to_quant[key]

        self.__amps[quant][key] = amp
        if amp > self.__range[quant]:
            self.__range[quant] = amp
        else:
            self.__range[quant] = max(self.__amps[quant].values())

        if self.__range[quant] < self.__min_range:
            self.__range[quant] = self.__min_range

        self.setRange(QtCore.QRectF(*self.__u_rect()))
        self.__update_grid()
        self.__update_labels()

    def __init_grid(self):
        self.__circle_u = pg.QtGui.QGraphicsEllipseItem()
        self.__circle_u.setPen(pg.mkPen(0.2))
        self.addItem(self.__circle_u)

        self.__circle_i = pg.QtGui.QGraphicsEllipseItem()
        self.__circle_i.setPen(pg.mkPen(0.2))
        self.addItem(self.__circle_i)

    def __update_grid(self):
        self.__circle_u.setRect(*self.__u_rect())
        rad = self.__i_radius()
        self.__circle_i.setRect(-rad, -rad, 2*rad, 2*rad)

    def __u_rect(self):
        return (
            -self.__range['u'],
            -self.__range['u'],
            2*self.__range['u'],
            2*self.__range['u'],
        )

    def __init_labels(self):
        self.__label = {}
        for quant in ['u', 'i']:
            self.__label[quant] = pg.TextItem()
            self.addItem(self.__label['u'])

    def __update_labels(self):
        for quant in ['u', 'i']:
            self.__label[quant].setText("{}".format(
                round(self.__range[quant], ROUND_TO)))

        self.__label['u'].setPos(0, self.__range['u'])
        self.__label['i'].setPos(0, self.__i_radius())

    def __i_radius(self):
        return I_SCALE * self.__range['u']

    def __to_front(self, item):
        self.removeItem(item)
        self.addItem(item)

    def sizeHint(self):
        # pylint: disable=invalid-name,no-self-use,missing-docstring
        return DEFAULT_WIDGET_SIZE

    def heightForWidth(self, width):
        # pylint: disable=invalid-name,no-self-use,missing-docstring
        return width
