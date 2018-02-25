import sys
from MainApp import *
from Dialog1 import *
from Dialog2 import *
from PyQt4 import Qt, QtGui


class MyForm(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton1, QtCore.SIGNAL('clicked()'), self.openDialog1)
        QtCore.QObject.connect(self.ui.pushButton2, QtCore.SIGNAL('clicked()'), self.openDialog2)    


    def openDialog1(self):
        editDialog = Dialog1()
        editDialog.exec_()

    def openDialog2(self):
        editDialog = Dialog2()
        editDialog.exec_()        



class Dialog1(QtGui.QDialog):
    isEdit = False
    def __init__(self, studentId=0, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class Dialog2(QtGui.QDialog):
    isEdit = False
    def __init__(self, studentId=0, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
