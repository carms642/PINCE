#!/usr/bin/python3
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
from mainwindow import Ui_MainWindow as mainwindow
from selectprocess import Ui_MainWindow as processwindow

class GuiUtils(object):

#centering a window
    def center(self):
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

#centering a child window
    def parentcenter(self):
        self.move(self.parent().frameGeometry().center().x() - self.frameGeometry().width()/2, self.parent().frameGeometry().center().y() - self.frameGeometry().height()/2)

#the mainwindow
class mainForm(QMainWindow, mainwindow):
    def __init__(self, parent=None):
        super().__init__()
        GuiUtils.center(self)
        self.setupUi(self)
        self.processbutton.clicked.connect(self.onclick)

#shows the process select window
    def onclick(self):
        self.window = processForm(self)
        self.window.show()

#closes all windows on exit
    def closeEvent(self, event):
        app = QApplication.instance()
        app.closeAllWindows()

#process select window
class processForm(QMainWindow, processwindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        GuiUtils.parentcenter(self)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = mainForm()
    window.show()
    sys.exit(app.exec_())