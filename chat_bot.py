import os
import sys

from PyQt5 import QtWidgets, uic

_scriptdir = os.path.dirname(os.path.realpath(__file__))


class MainDialog(*uic.loadUiType(os.path.join(_scriptdir, 'main_dialog_chat.ui',))):
    from part2 import Ui_MainDialog

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bindevents1()

    def bindevents1(self):
        self.yesButton.clicked.connect(self.yes)
        self.noButton.clicked.connect(self.finish)

    def finish(self):
        self.noButton.clicked.connect(self.close)
  
    def yes(self):
        self.Ui_MainDialog.yes1(self, MainDialog)
        self.yesButton.clicked.connect(self.yes2)

    def yes2(self):
        self.Ui_MainDialog.yes2(self)
        self.yesButton.clicked.connect(self.yes3)

    def yes3(self):
        self.Ui_MainDialog.yes3(self)
        self.yesButton.clicked.connect(self.yes4)

    def yes4(self):
        self.Ui_MainDialog.yes4(self)
        self.yesButton.clicked.connect(self.patrol)
        self.noButton.clicked.connect(self.garrison)

    def patrol(self):
        self.Ui_MainDialog.patrol(self)
        self.yesButton.clicked.connect(self.usual)
        self.noButton.clicked.connect(self.deviance)

    def usual(self):
        self.Ui_MainDialog.usual(self)
        self.yesButton.clicked.connect(self.attack)
        self.noButton.clicked.connect(self.escape)

    def attack(self):
        self.Ui_MainDialog.attack(self)
        self.yesButton.clicked.connect(self.close)
        self.noButton.clicked.connect(self.close)

    def escape(self):
        self.Ui_MainDialog.escape(self)
        self.yesButton.clicked.connect(self.close)
        self.noButton.clicked.connect(self.close)

    def deviance(self):
        self.Ui_MainDialog.deviance(self)
        self.yesButton.clicked.connect(self.close)
        self.noButton.clicked.connect(self.close)

    def garrison(self):
        self.Ui_MainDialog.garrison(self)
        self.yesButton.clicked.connect(self.yes5)
        self.noButton.clicked.connect(self.nobody)

    def yes5(self):
        self.Ui_MainDialog.yes5(self)
        self.yesButton.clicked.connect(self.close)
        self.noButton.clicked.connect(self.close)

    def nobody(self):
        self.Ui_MainDialog.nobody(self)
        self.yesButton.clicked.connect(self.yes5)
        self.noButton.clicked.connect(self.yes5)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainDialog()
    w.show()

    sys.exit(app.exec_())
    