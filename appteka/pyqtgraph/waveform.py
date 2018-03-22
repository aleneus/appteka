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

import pyqtgraph as pg
from appteka.timestamps import get_time, get_date

class TimeStampAxisItem(pg.AxisItem):
    """ Axis with times or dates as ticks. """
    def __init__(self, what_show='time', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enableAutoSIPrefix(enable=False)
        if what_show not in ['time', 'date']:
            raise ValueError("show must be 'time' or 'date'")
        self.what_show = what_show
        
    def tickStrings(self, values, scale, spacing):
        if self.what_show == 'time':
            return [get_time(v) for v in values]
        elif self.what_show == 'date':
            return [get_date(v) for v in values]

class AxisItemsFactory:
    """ Factory for creating custom axis items with time stamps. """
    def get_items(top=True):
        res = {'bottom' : TimeStampAxisItem(what_show='time', orientation='bottom')}
        if top:
            res['top'] = TimeStampAxisItem(what_show='date', orientation='top')
        return res

class Waveform(pg.PlotWidget):
    """ Customized PyQtGraph.PlotWidget. """
    def __init__(self, xlabel=None):
        super().__init__(axisItems=AxisItemsFactory.get_items())
        self.state = {
            'online' : False,
            'plot_color' : (255,255,255),
        }
        self.showGrid(x=True, y=True)
        self.setMouseEnabled(x=True, y=False)
        self.showAxis('top')
        self.showAxis('right')
        if xlabel is not None:
            self.setLabel('bottom', xlabel)
        self.setDownsampling(mode='peak')
        self.setClipToView(True)
        self.enableAutoRange(True)
        self.curve = self.plot()

    def reset(self):
        self.clear()
        self.curve = self.plot()
        self.set_plot_color(self.state['plot_color'])
        self.setMouseEnabled(x=True, y=False)
        self.enableAutoRange(True)
        
    def set_online(self, value):
        self.state['online'] = value

    def set_plot_color(self, color):
        self.curve.setPen(color)
        self.state['plot_color'] = color

    def update_data(self, t, x):
        if self.state['online'] and not self.isVisible():
            return
        if len(t) <= 0:
            return
        self.curve.setData(t, x)
        self.setLimits(xMin=t[0], xMax=t[-1])
        self.setRange(
            xRange=(t[0], t[-1]),
            yRange=(min(x), max(x)),
            disableAutoRange=False
        )

class MultiWaveform(pg.GraphicsLayoutWidget):
    """ Customized PyQtGraph.GraphicsLayoutWidget. """
    def __init__(self):
        """ Initialization. """
        super().__init__()
        self.state = {
            'online' : False,
            'plot_color' : (255,255,255),
        }
        self.plots = {}
        self.curves = {}
        self._main = None
        self.__main_plot_limits = None

    def set_main_plot(self, key):
        """ Set the plot used for synchronization (main plot). """
        self._main = key
    def get_main_plot(self):
        """ Set the plot used for synchronization (main plot). """
        return self._main
    main_plot = property(get_main_plot, set_main_plot, doc="Plot used for synchronization")

    def _init_plot(self, key):
        """ Bring plot to initial state. """
        if key not in self.plots.keys():
            return
        plot = self.plots[key]
        plot.setDownsampling(mode='peak')
        plot.showGrid(x=True, y=True)
        plot.setMouseEnabled(x=True, y=False)
        plot.showAxis('right')
        for axis in ['left', 'right']:
            plot.getAxis(axis).setStyle(tickTextWidth=40, autoExpandTextSpace=False)
        plot.enableAutoRange(True)

    def add_plot(self, key, title=None, main=False):
        """ Add plot. """
        self.plots[key] = self.addPlot(len(self.plots), 0, axisItems=AxisItemsFactory.get_items())
        self._init_plot(key)
        if title is not None:
            self.plots[key].setTitle(title, justify='left')
        self.curves[key] = self.plots[key].plot()
        self.curves[key].setPen(self.state['plot_color'])
        if main:
            self._main = key

    def remove_plots(self):
        """ Remove all plots. """
        for key in self.plots.keys():
            self.removeItem(self.plots[key])
        self.plots = {}
        self.curves = {}

    def update_data(self, key, t, x):
        """ Update data on the plot. """
        if len(t) == 0:
            return
        
        xlims = (t[0], t[-1])
        
        if self.state['online']:
            if not self.isVisible():
                return
        else:
            if key == self._main:
                self.__main_plot_limits = xlims
            elif self._main is not None:
                    xlims = self.__main_plot_limits
                    
        self.curves[key].setData(t, x)
        self.plots[key].setLimits(xMin=xlims[0], xMax=xlims[-1])
        self.plots[key].setRange(xRange=xlims)
        
    def set_online(self, value):
        """ Turn on or turn off the online mode. """
        self.state['online'] = value
        for plot in self.plots.values():
            plot.setClipToView(value)
        
    def set_plot_color(self, color):
        """ Set color for all plots. """
        for c in self.curves.values():
            c.setPen(color)
        self.state['plot_color'] = color

    def set_link_to_main(self, value=True):
        """ Link plots to main or unlink. """
        for key in self.plots.keys():
            if key == self._main:
                continue
            self.plots[key].setXLink(self.plots[self._main] if value else None)