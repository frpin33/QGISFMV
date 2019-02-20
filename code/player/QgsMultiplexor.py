# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QDialog
from QGIS_FMV.gui.ui_FmvMultiplexer import Ui_VideoMultiplexer

try:
    from pydevd import *
except ImportError:
    None


class Multiplexor(QDialog, Ui_VideoMultiplexer):
    """ About Dialog """

    def __init__(self, iface, parent=None):
        """ Contructor """
        super(Multiplexor, self).__init__(parent)
        self.setupUi(self)

    def OpenFile(self):
        return

    def SaveFile(self):
        return

    def CreateMISB(self):
        return
