# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import pyqtgraph as pg
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)

        self.channel_sample = QtWidgets.QFrame()
        self.Channel1Components = QtWidgets.QHBoxLayout()
        self.channel_sample.setLayout(self.Channel1Components)
        self.verticalLayout_2.addWidget(self.channel_sample)
        self.Channel1Components.setObjectName("Channel1Components")


        self.graphicsView_recover = pg.PlotWidget(self.tab)
        self.graphicsView_recover.plotItem.showGrid(True, True)
        self.graphicsView_recover.setObjectName("graphicsView_recover")
        self.Channel1Components.addWidget(self.graphicsView_recover)
        #self.verticalLayout_2.addWidget(self.graphicsView_recover)
        

       
        self.channel_recover = QtWidgets.QFrame()
        self.channel_recoverComponents = QtWidgets.QHBoxLayout()
        self.channel_recover.setLayout(self.channel_recoverComponents)
        self.verticalLayout_2.addWidget(self.channel_recover)

        
        self.graphicsView_sample = pg.PlotWidget(self.tab)
        self.graphicsView_sample.plotItem.showGrid(True, True)
        self.graphicsView_sample.setObjectName("graphicsView_sample")
        self.channel_recoverComponents.addWidget(self.graphicsView_sample)
       # self.verticalLayout_2.addWidget(self.graphicsView_sample)
        #self.horizontalScrollBar = QtWidgets.QScrollBar(self.tab)
        #self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        #self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        #self.verticalLayout_2.addWidget(self.horizontalScrollBar)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
       

        self.GraphViewSignal = pg.PlotWidget(self.tab_2)
        self.GraphViewSignal.plotItem.showGrid(True, True)
        self.GraphViewSignal.setGeometry(QtCore.QRect(0, 10, 881, 321))
        self.GraphViewSignal.setObjectName("GraphViewSignal")
        

        self.GraphViewComposer = pg.PlotWidget(self.tab_2)
        self.GraphViewComposer.plotItem.showGrid(True, True)
        self.GraphViewComposer.setGeometry(QtCore.QRect(0, 350, 881, 341))
        self.GraphViewComposer.setObjectName("GraphViewComposer")

        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(873, 0, 101, 711))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(940, 10, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(940, 40, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(940, 70, 101, 31))
        self.label_2.setObjectName("label_2")
        self.spinBoxMagnitude = QtWidgets.QSpinBox(self.tab_2)
        self.spinBoxMagnitude.setGeometry(QtCore.QRect(940, 100, 111, 31))
        self.spinBoxMagnitude.setObjectName("spinBoxMagnitude")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(940, 140, 81, 31))
        self.label_3.setObjectName("label_3")
        self.spinBox_frequency = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_frequency.setGeometry(QtCore.QRect(940, 170, 111, 31))
        self.spinBox_frequency.setObjectName("spinBox_frequency")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(940, 210, 71, 21))
        self.label_4.setObjectName("label_4")
        self.spinBox_Phase = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_Phase.setGeometry(QtCore.QRect(940, 240, 111, 31))
        self.spinBox_Phase.setObjectName("spinBox_Phase")
        self.pushButton_ADD = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_ADD.setGeometry(QtCore.QRect(940, 290, 121, 31))
        self.pushButton_ADD.setObjectName("pushButton_ADD")
        # self.pushButton_DRAW = QtWidgets.QPushButton(self.tab_2)
        # self.pushButton_DRAW.setGeometry(QtCore.QRect(940, 330, 121, 31))
        # self.pushButton_DRAW.setObjectName("pushButton_DRAW")
        # self.pushButton_DELETE = QtWidgets.QPushButton(self.tab_2)
        # self.pushButton_DELETE.setGeometry(QtCore.QRect(940, 370, 121, 31))
        # self.pushButton_DELETE.setObjectName("pushButton_DELETE")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(920, 330, 161, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox_choosesignal = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_choosesignal.setGeometry(QtCore.QRect(950, 400, 111, 31))
        self.comboBox_choosesignal.setObjectName("comboBox_choosesignal")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(950, 350, 101, 20))
        self.label_5.setObjectName("label_5")
        # self.pushButton_clear = QtWidgets.QPushButton(self.tab_2)
        # self.pushButton_clear.setGeometry(QtCore.QRect(950, 600, 111, 31))
        # self.pushButton_clear.setObjectName("pushButton_clear")
        # self.pushButton_DRAW2 = QtWidgets.QPushButton(self.tab_2)
        # self.pushButton_DRAW2.setGeometry(QtCore.QRect(950, 560, 111, 31))
        # self.pushButton_DRAW2.setObjectName("pushButton_DRAW2")
        self.pushButton_Delete = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Delete.setGeometry(QtCore.QRect(950, 450, 111, 31))
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.pushButton_confirmSum = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_confirmSum.setGeometry(QtCore.QRect(952, 500, 111, 31))
        self.pushButton_confirmSum.setObjectName("pushButton_confirmSum")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuopen = QtWidgets.QMenu(self.menufile)
        self.menuopen.setObjectName("menuopen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionchannel_1 = QtWidgets.QAction(MainWindow)
        self.actionchannel_1.setObjectName("actionchannel_1")
        self.menuopen.addAction(self.actionchannel_1)
        self.menufile.addAction(self.menuopen.menuAction())
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionexit)
        self.menubar.addAction(self.menufile.menuAction())
        # self.sample = QtWidgets.QPushButton(self.tab)
        # self.sample.setGeometry(QtCore.QRect(700,0,81,28))
        # self.sample.setObjectName("stop")
        # self.sample.setText("sample")
        #self.verticalLayout_2.addWidget(self.sample)
        self.recover_upper_graph = QtWidgets.QPushButton(self.tab)
        self.recover_upper_graph.setGeometry(QtCore.QRect(800,0,201,28))
        self.recover_upper_graph.setObjectName("stop")
        self.recover_upper_graph.setText("Recover in upper graph ")
        #self.verticalLayout_2.addWidget(self.recover_upper_graph)
        self.recover_down_graph = QtWidgets.QPushButton(self.tab)
        self.recover_down_graph.setGeometry(QtCore.QRect(800,28,201,28))
        self.recover_down_graph.setObjectName("stop")
        self.recover_down_graph.setText("Recover in same graph")
       
        self.slider = QtWidgets.QSlider(self.tab)
        self.slider.setGeometry(QtCore.QRect(200,0,500,30))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.label_slider = QtWidgets.QLabel(self.tab)
        self.label_slider.setGeometry(QtCore.QRect(700, 28, 91, 21))
        self.label_slider.setObjectName("label")
        self.label_slider1 = QtWidgets.QLabel(self.tab)
        self.label_slider1.setGeometry(QtCore.QRect(150, 28, 91, 21))
        self.label_slider1.setObjectName("label")
        self.label_slider2 = QtWidgets.QLabel(self.tab)
        self.label_slider2.setGeometry(QtCore.QRect(425, 28, 91, 21))
        self.label_slider2.setObjectName("label")
        #self.verticalLayout_2.addWidget(self.slider)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Toggle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "Signal Name:"))
        self.label_2.setText(_translate("MainWindow", "Magnitude :"))
        self.label_3.setText(_translate("MainWindow", "Frequency :"))
        self.label_4.setText(_translate("MainWindow", "Phase :"))
        self.pushButton_ADD.setText(_translate("MainWindow", "ADD"))
        # self.pushButton_DRAW.setText(_translate("MainWindow", "DRAW"))
        # self.pushButton_DELETE.setText(_translate("MainWindow", "DELETE"))
        self.label_5.setText(_translate("MainWindow", "Choose signal"))
        # self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        # self.pushButton_DRAW2.setText(_translate("MainWindow", "DRAW"))
        self.pushButton_Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_confirmSum.setText(_translate("MainWindow", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuopen.setTitle(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionchannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.label_slider.setText(_translate("MainWindow", "3Fmax"))
        self.label_slider1.setText(_translate("MainWindow", "Fmax"))
        self.label_slider2.setText(_translate("MainWindow", "2Fmax"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())