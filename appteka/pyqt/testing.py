# appteka - helpers collection

# Copyright (C) 2018-2020 Aleksandr Popov

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

"""Implementation of the tool for visual testing of widgets."""

import sys
import threading

from PyQt5 import QtWidgets

from appteka.pyqt import gui


class _TestDialog(QtWidgets.QDialog):
    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.__make_gui()

    def __make_gui(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        self.widget_layout = gui.add_sublayout(main_layout, "h")

        self.assert_layout = gui.add_sublayout(main_layout, "h")
        self.label_assert = gui.add_label("", self.assert_layout)
        self.label_assert.setWordWrap(True)

        self.button_layout = gui.add_sublayout(main_layout, "h")
        self.button_no = gui.add_button("No", self.__on_button_no,
                                        self.button_layout)
        self.button_yes = gui.add_button("Yes", self.__on_button_yes,
                                         self.button_layout)

    def set_widget(self, widget):
        self.widget_layout.addWidget(widget)

    def set_asserts(self, asserts):
        lines = ""
        for assrt in asserts:
            lines += "- {}\n".format(assrt)
        self.label_assert.setText(lines)

    def set_enabled(self, value=True):
        self.button_yes.setEnabled(value)
        self.button_no.setEnabled(value)

    def __on_button_no(self):
        self.app.answer = False
        self.reject()

    def __on_button_yes(self):
        self.app.answer = True
        self.accept()


class TestApp:
    __app = None

    def __init__(self, context):
        if not TestApp.__app:
            TestApp.__app = QtWidgets.QApplication(sys.argv)

        self.answer = False
        self.dialog = _TestDialog(self)
        self.context = context

    def set_widget(self, widget):
        self.dialog.set_widget(widget)

    def set_asserts(self, asserts):
        self.dialog.set_asserts(asserts)

    def enable_after(self, func, interval):

        def enable():
            self.dialog.set_enabled(True)

        self.dialog.set_enabled(False)

        t = threading.Timer(interval, enable)
        func()
        t.start()

    def act(self):
        self.dialog.show()
        TestApp.__app.exec()
        return self.answer

    def __call__(self, w, asserts):
        self.set_widget(w)
        self.set_asserts(asserts)
        self.context.assertTrue(self.act())
