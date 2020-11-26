import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject


class Signal(QObject):
    signalOnClicked = pyqtSignal()


class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.signal = Signal()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('userDefineSignal')
        self.signal.signalOnClicked.connect(self.about)

    def about(self):
        QMessageBox.about(self, 'Mouse', 'Mouse Was Clicked')

    def mousePressEvent(self, e):
        self.signal.signalOnClicked.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
