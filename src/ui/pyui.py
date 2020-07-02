from ui_VMS import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_VMS()
        self.ui.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    #myapp.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #myapp.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    myapp.show()
    sys.exit(app.exec_())