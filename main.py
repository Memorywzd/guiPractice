# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__1__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('第一个gui程序')
    w.show()

    sys.exit(app.exec_())