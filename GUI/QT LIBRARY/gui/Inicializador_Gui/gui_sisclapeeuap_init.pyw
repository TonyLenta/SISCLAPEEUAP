from PyQt5.QtWidgets import QDialog
import sys
from gui_sisclapeeuap import *

class GUIinit(QtWidgets.QDialog): 
    def __init__(self, parent=None) :
        QtWidgets.QWidget.__init__(self, parent)
        self.ui =Ui_framePrincipal()
        self.ui.setupUi(self)


if __name__== "__main__":
              app = QtWidgets.QApplication(sys.argv)
              myapp = GUIinit()
              myapp.show()
              sys.exit(app.exec_())