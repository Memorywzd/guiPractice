# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui5.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(735, 563)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        mainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setToolTip("")
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_4 = QtWidgets.QAction(mainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(mainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(mainWindow)
        self.action_6.setObjectName("action_6")
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_4)
        self.menu.addAction(self.action)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_4)
        self.toolBar.addAction(self.action_6)

        self.retranslateUi(mainWindow)
        self.action_6.triggered.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "界面"))
        mainWindow.setToolTip(_translate("mainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menu.setTitle(_translate("mainWindow", "文件(&F)"))
        self.menu_2.setTitle(_translate("mainWindow", "保存方式(&S)"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.statusBar.setStatusTip(_translate("mainWindow", "ready"))
        self.action.setText(_translate("mainWindow", "新建(&N)"))
        self.action.setToolTip(_translate("mainWindow", "新建"))
        self.action.setShortcut(_translate("mainWindow", "Ctrl+N"))
        self.action_4.setText(_translate("mainWindow", "另存为...(&O)"))
        self.action_4.setToolTip(_translate("mainWindow", "另存为"))
        self.action_4.setShortcut(_translate("mainWindow", "Ctrl+S"))
        self.action_5.setText(_translate("mainWindow", "保存"))
        self.action_5.setToolTip(_translate("mainWindow", "保存"))
        self.action_6.setText(_translate("mainWindow", "退出(&Q)"))
        self.action_6.setToolTip(_translate("mainWindow", "退出"))
        self.action_6.setShortcut(_translate("mainWindow", "Ctrl+Q"))
