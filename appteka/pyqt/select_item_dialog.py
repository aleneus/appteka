"""Select item Qt dialog."""

from PyQt5 import QtWidgets
from appteka.pyqt import gui


class SelectItemDialog(QtWidgets.QDialog):
    """ Dialog for selecting string item from list. """
    def __init__(self, title="Select column", question="Select item",
                 ok_caption="Ok", cancel_caption="Cancel",
                 parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._items = []
        self._index = None

        self._make_gui(title, question, ok_caption, cancel_caption)

    def _make_gui(self, title, question, ok_caption, cancel_caption):
        self.setWindowTitle(title)
        main_layout = QtWidgets.QVBoxLayout(self)
        gui.add_label(question, main_layout)
        self._quant_list = gui.add_widget(QtWidgets.QListWidget(), main_layout)
        self._quant_list.setWordWrap(True)
        self._quant_list.setSpacing(2)

        buttons_layout = gui.add_sublayout(main_layout, 'h')
        gui.add_button(ok_caption, self._ok_clicked,
                       buttons_layout)
        gui.add_button(cancel_caption, self._cancel_clicked,
                       buttons_layout)

    def exec(self):
        """ Execute dialog. """
        for item in self._items:
            self._quant_list.addItem(item)
        return super().exec()

    def _ok_clicked(self):
        """ OK button clicked handler. """
        self._index = self._quant_list.currentRow()
        self.accept()

    def _cancel_clicked(self):
        """ Cancel button clicked handler. """
        self.reject()

    def set_items(self, str_list):
        """ Set the names of items. """
        self._items = str_list

    def get_item_name(self):
        """ Return name selected item. """
        ind = self.get_item_index()
        name = self._items[ind]
        return name

    def get_item_index(self):
        """ Return index of selected item. """
        if self._index is None:
            raise RuntimeError("Index is None.")
        ind = self._index
        return ind
