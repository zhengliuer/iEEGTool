# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'electrodes_viz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 900))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self._brain_gp = QtWidgets.QGroupBox(self.centralwidget)
        self._brain_gp.setMinimumSize(QtCore.QSize(420, 0))
        self._brain_gp.setMaximumSize(QtCore.QSize(420, 16777215))
        self._brain_gp.setCheckable(True)
        self._brain_gp.setObjectName("_brain_gp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._brain_gp)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._transparency_lb = QtWidgets.QLabel(self._brain_gp)
        self._transparency_lb.setMinimumSize(QtCore.QSize(75, 25))
        self._transparency_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        self._transparency_lb.setObjectName("_transparency_lb")
        self.horizontalLayout.addWidget(self._transparency_lb)
        self._transparency_slider = QtWidgets.QSlider(self._brain_gp)
        self._transparency_slider.setMinimumSize(QtCore.QSize(250, 25))
        self._transparency_slider.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self._transparency_slider.setFont(font)
        self._transparency_slider.setFocusPolicy(QtCore.Qt.ClickFocus)
        self._transparency_slider.setAutoFillBackground(False)
        self._transparency_slider.setMaximum(100)
        self._transparency_slider.setSingleStep(10)
        self._transparency_slider.setPageStep(10)
        self._transparency_slider.setProperty("value", 10)
        self._transparency_slider.setSliderPosition(10)
        self._transparency_slider.setOrientation(QtCore.Qt.Horizontal)
        self._transparency_slider.setInvertedAppearance(False)
        self._transparency_slider.setInvertedControls(False)
        self._transparency_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self._transparency_slider.setTickInterval(10)
        self._transparency_slider.setObjectName("_transparency_slider")
        self.horizontalLayout.addWidget(self._transparency_slider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._hemi_lb = QtWidgets.QLabel(self._brain_gp)
        self._hemi_lb.setMinimumSize(QtCore.QSize(113, 25))
        self._hemi_lb.setMaximumSize(QtCore.QSize(1999999, 25))
        self._hemi_lb.setObjectName("_hemi_lb")
        self.horizontalLayout_2.addWidget(self._hemi_lb)
        self._hemi_cbx = QtWidgets.QComboBox(self._brain_gp)
        self._hemi_cbx.setMinimumSize(QtCore.QSize(250, 25))
        self._hemi_cbx.setMaximumSize(QtCore.QSize(1000, 25))
        self._hemi_cbx.setObjectName("_hemi_cbx")
        self._hemi_cbx.addItem("")
        self._hemi_cbx.addItem("")
        self._hemi_cbx.addItem("")
        self.horizontalLayout_2.addWidget(self._hemi_cbx)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self._brain_gp)
        self._electrodes_gp = QtWidgets.QGroupBox(self.centralwidget)
        self._electrodes_gp.setMinimumSize(QtCore.QSize(420, 700))
        self._electrodes_gp.setMaximumSize(QtCore.QSize(420, 16777215))
        self._electrodes_gp.setCheckable(True)
        self._electrodes_gp.setObjectName("_electrodes_gp")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._electrodes_gp)
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._elec_hemi_lb = QtWidgets.QLabel(self._electrodes_gp)
        self._elec_hemi_lb.setMinimumSize(QtCore.QSize(113, 25))
        self._elec_hemi_lb.setMaximumSize(QtCore.QSize(1999999, 25))
        self._elec_hemi_lb.setObjectName("_elec_hemi_lb")
        self.horizontalLayout_3.addWidget(self._elec_hemi_lb)
        self._elec_hemi_cbx = QtWidgets.QComboBox(self._electrodes_gp)
        self._elec_hemi_cbx.setMinimumSize(QtCore.QSize(250, 25))
        self._elec_hemi_cbx.setMaximumSize(QtCore.QSize(1000, 25))
        self._elec_hemi_cbx.setObjectName("_elec_hemi_cbx")
        self._elec_hemi_cbx.addItem("")
        self._elec_hemi_cbx.addItem("")
        self._elec_hemi_cbx.addItem("")
        self.horizontalLayout_3.addWidget(self._elec_hemi_cbx)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._select_lb = QtWidgets.QLabel(self._electrodes_gp)
        self._select_lb.setMinimumSize(QtCore.QSize(113, 25))
        self._select_lb.setMaximumSize(QtCore.QSize(1999999, 25))
        self._select_lb.setObjectName("_select_lb")
        self.horizontalLayout_5.addWidget(self._select_lb)
        self._select_cbx = QtWidgets.QComboBox(self._electrodes_gp)
        self._select_cbx.setMinimumSize(QtCore.QSize(250, 25))
        self._select_cbx.setMaximumSize(QtCore.QSize(1000, 25))
        self._select_cbx.setObjectName("_select_cbx")
        self._select_cbx.addItem("")
        self._select_cbx.addItem("")
        self._select_cbx.addItem("")
        self._select_cbx.addItem("")
        self.horizontalLayout_5.addWidget(self._select_cbx)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self._electrodes_gp)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self._display_cbx = QtWidgets.QCheckBox(self._electrodes_gp)
        self._display_cbx.setMinimumSize(QtCore.QSize(143, 0))
        self._display_cbx.setMaximumSize(QtCore.QSize(143, 16777215))
        self._display_cbx.setChecked(True)
        self._display_cbx.setObjectName("_display_cbx")
        self.horizontalLayout_6.addWidget(self._display_cbx)
        self._roi_cbx = QtWidgets.QCheckBox(self._electrodes_gp)
        self._roi_cbx.setObjectName("_roi_cbx")
        self.horizontalLayout_6.addWidget(self._roi_cbx)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._group_lb = QtWidgets.QLabel(self._electrodes_gp)
        self._group_lb.setMinimumSize(QtCore.QSize(113, 25))
        self._group_lb.setMaximumSize(QtCore.QSize(143, 25))
        self._group_lb.setObjectName("_group_lb")
        self.horizontalLayout_4.addWidget(self._group_lb)
        self._group_cbx = QtWidgets.QComboBox(self._electrodes_gp)
        self._group_cbx.setMinimumSize(QtCore.QSize(250, 25))
        self._group_cbx.setMaximumSize(QtCore.QSize(1000, 25))
        self._group_cbx.setObjectName("_group_cbx")
        self.horizontalLayout_4.addWidget(self._group_cbx)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self._info_table = QtWidgets.QTableWidget(self._electrodes_gp)
        self._info_table.setMinimumSize(QtCore.QSize(0, 0))
        self._info_table.setObjectName("_info_table")
        self._info_table.setColumnCount(0)
        self._info_table.setRowCount(0)
        self.verticalLayout_2.addWidget(self._info_table)
        self.verticalLayout_3.addWidget(self._electrodes_gp)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self._plotter = QtInteractor(self.centralwidget)
        self._plotter.setMinimumSize(QtCore.QSize(800, 800))
        self._plotter.setObjectName("_plotter")
        self.horizontalLayout_7.addWidget(self._plotter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1300, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.actionScreenshot = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icon/screenshot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScreenshot.setIcon(icon)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self._screenshot_action = QtWidgets.QAction(MainWindow)
        self._screenshot_action.setObjectName("_screenshot_action")
        self.menuFile.addAction(self._screenshot_action)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._brain_gp.setTitle(_translate("MainWindow", "Brain"))
        self._transparency_lb.setText(_translate("MainWindow", "Transparency"))
        self._hemi_lb.setText(_translate("MainWindow", "Hemisphere"))
        self._hemi_cbx.setItemText(0, _translate("MainWindow", "Both"))
        self._hemi_cbx.setItemText(1, _translate("MainWindow", "Left"))
        self._hemi_cbx.setItemText(2, _translate("MainWindow", "Right"))
        self._electrodes_gp.setTitle(_translate("MainWindow", "Electrodes"))
        self._elec_hemi_lb.setText(_translate("MainWindow", "Hemisphere"))
        self._elec_hemi_cbx.setItemText(0, _translate("MainWindow", "Both"))
        self._elec_hemi_cbx.setItemText(1, _translate("MainWindow", "Left"))
        self._elec_hemi_cbx.setItemText(2, _translate("MainWindow", "Right"))
        self._select_lb.setText(_translate("MainWindow", "Select"))
        self._select_cbx.setItemText(0, _translate("MainWindow", "Inside the brain"))
        self._select_cbx.setItemText(1, _translate("MainWindow", "Outside the brain"))
        self._select_cbx.setItemText(2, _translate("MainWindow", "Gray matter"))
        self._select_cbx.setItemText(3, _translate("MainWindow", "White matter"))
        self._display_cbx.setText(_translate("MainWindow", "Display"))
        self._roi_cbx.setText(_translate("MainWindow", "Regions of Interest"))
        self._group_lb.setText(_translate("MainWindow", "Group"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionScreenshot.setText(_translate("MainWindow", "Screenshot"))
        self._screenshot_action.setText(_translate("MainWindow", "Screenshot"))
from pyvistaqt import QtInteractor


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
