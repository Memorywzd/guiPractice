import sys
from PyQt5.QtWidgets import *


class FileOperation(QWidget):
    def __init__(self):
        super(FileOperation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('File Operation')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('打开文件', self)
        self.bt1.move(350, 20)
        self.bt2 = QPushButton('选择字体', self)
        self.bt2.move(350, 70)
        self.bt3 = QPushButton('选择颜色', self)
        self.bt3.move(350, 120)

        self.bt1.clicked.connect(self.openFile)
        self.bt2.clicked.connect(self.choiceFont)
        self.bt3.clicked.connect(self.choiceColor)

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, '打开文件', './')
        if filename[0]:
            with open(filename[0], 'r', encoding='gb18030', errors='ignore') as f:
                self.tx.setText(f.read())

    def choiceFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)

    def choiceColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = FileOperation()
    ui.show()
    sys.exit(app.exec_())
