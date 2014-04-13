import sys
from PyQt4 import QtGui
from main_ui import Ui_MainWindow

class Dashboard(QtGui.QMainWindow):

    def __init__(self):
        super(Dashboard, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Dashboard()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
