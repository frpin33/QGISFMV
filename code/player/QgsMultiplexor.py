# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl, Qt, QCoreApplication
from PyQt5.QtWidgets import QDialog
from QGIS_FMV.gui.ui_FmvMultiplexer import Ui_VideoMultiplexer
from QGIS_FMV.utils.QgsFmvUtils import askForFiles
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
        self.iface = iface

    def OpenFile(self):
        ''' Open File '''
        sender = self.sender().objectName()
        filename, _ = askForFiles(self, QCoreApplication.translate(
            "Multiplexor", "Open file"),
            exts="csv")

        return

    def SaveFile(self):
        ''' Save file '''
        out, _ = askForFiles(self, QCoreApplication.translate(
            "Multiplexor", "Save file"),
            isSave=True,
            exts="json")

        return

    def CreateMISB(self):
        ''' Create MISB Video '''
        input_video = self.ln_inputVideo.text()
        input_metadata = self.ln_inputMeta.text()
        out_video = self.ln_outVideo.text()
        input_mapping = self.ln_Mapping.text()
        input_avg = self.ln_avg.text()

        return
    
    def parseCSV(self):
        ''' Parse raw metadata file to standar file '''
        return
