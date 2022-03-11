# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csd_morlet.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 455)
        MainWindow.setMinimumSize(QtCore.QSize(406, 455))
        MainWindow.setMaximumSize(QtCore.QSize(406, 455))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Multitaper_method_lb = QtWidgets.QLabel(self.groupBox)
        self.Multitaper_method_lb.setMinimumSize(QtCore.QSize(0, 25))
        self.Multitaper_method_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Multitaper_method_lb.setFont(font)
        self.Multitaper_method_lb.setObjectName("Multitaper_method_lb")
        self.horizontalLayout_5.addWidget(self.Multitaper_method_lb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self._compute_btn = QtWidgets.QPushButton(self.groupBox)
        self._compute_btn.setMinimumSize(QtCore.QSize(100, 25))
        self._compute_btn.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._compute_btn.setFont(font)
        self._compute_btn.setObjectName("_compute_btn")
        self.horizontalLayout_5.addWidget(self._compute_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(35)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._chan_lb = QtWidgets.QLabel(self.groupBox)
        self._chan_lb.setMinimumSize(QtCore.QSize(100, 25))
        self._chan_lb.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self._chan_lb.setFont(font)
        self._chan_lb.setObjectName("_chan_lb")
        self.verticalLayout_2.addWidget(self._chan_lb)
        self._freq_band_lb = QtWidgets.QLabel(self.groupBox)
        self._freq_band_lb.setMinimumSize(QtCore.QSize(0, 25))
        self._freq_band_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._freq_band_lb.setFont(font)
        self._freq_band_lb.setObjectName("_freq_band_lb")
        self.verticalLayout_2.addWidget(self._freq_band_lb)
        self._freq_step_lb = QtWidgets.QLabel(self.groupBox)
        self._freq_step_lb.setMinimumSize(QtCore.QSize(0, 25))
        self._freq_step_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._freq_step_lb.setFont(font)
        self._freq_step_lb.setObjectName("_freq_step_lb")
        self.verticalLayout_2.addWidget(self._freq_step_lb)
        self._denom_ncycles_lb = QtWidgets.QLabel(self.groupBox)
        self._denom_ncycles_lb.setMinimumSize(QtCore.QSize(0, 25))
        self._denom_ncycles_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._denom_ncycles_lb.setFont(font)
        self._denom_ncycles_lb.setObjectName("_denom_ncycles_lb")
        self.verticalLayout_2.addWidget(self._denom_ncycles_lb)
        self._n_jobs_lb = QtWidgets.QLabel(self.groupBox)
        self._n_jobs_lb.setMinimumSize(QtCore.QSize(0, 25))
        self._n_jobs_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._n_jobs_lb.setFont(font)
        self._n_jobs_lb.setObjectName("_n_jobs_lb")
        self.verticalLayout_2.addWidget(self._n_jobs_lb)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self._select_chan_btn = QtWidgets.QToolButton(self.groupBox)
        self._select_chan_btn.setMinimumSize(QtCore.QSize(100, 25))
        self._select_chan_btn.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._select_chan_btn.setFont(font)
        self._select_chan_btn.setObjectName("_select_chan_btn")
        self.verticalLayout.addWidget(self._select_chan_btn)
        self._freq_band_le = QtWidgets.QLineEdit(self.groupBox)
        self._freq_band_le.setMinimumSize(QtCore.QSize(100, 25))
        self._freq_band_le.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._freq_band_le.setFont(font)
        self._freq_band_le.setFocusPolicy(QtCore.Qt.ClickFocus)
        self._freq_band_le.setAlignment(QtCore.Qt.AlignCenter)
        self._freq_band_le.setObjectName("_freq_band_le")
        self.verticalLayout.addWidget(self._freq_band_le)
        self._freq_step_le = QtWidgets.QLineEdit(self.groupBox)
        self._freq_step_le.setMinimumSize(QtCore.QSize(100, 25))
        self._freq_step_le.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._freq_step_le.setFont(font)
        self._freq_step_le.setFocusPolicy(QtCore.Qt.ClickFocus)
        self._freq_step_le.setAlignment(QtCore.Qt.AlignCenter)
        self._freq_step_le.setObjectName("_freq_step_le")
        self.verticalLayout.addWidget(self._freq_step_le)
        self._denom_ncycles_le = QtWidgets.QLineEdit(self.groupBox)
        self._denom_ncycles_le.setMinimumSize(QtCore.QSize(100, 25))
        self._denom_ncycles_le.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._denom_ncycles_le.setFont(font)
        self._denom_ncycles_le.setFocusPolicy(QtCore.Qt.ClickFocus)
        self._denom_ncycles_le.setAlignment(QtCore.Qt.AlignCenter)
        self._denom_ncycles_le.setObjectName("_denom_ncycles_le")
        self.verticalLayout.addWidget(self._denom_ncycles_le)
        self._n_jobs_le = QtWidgets.QLineEdit(self.groupBox)
        self._n_jobs_le.setMinimumSize(QtCore.QSize(100, 25))
        self._n_jobs_le.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._n_jobs_le.setFont(font)
        self._n_jobs_le.setFocusPolicy(QtCore.Qt.ClickFocus)
        self._n_jobs_le.setAlignment(QtCore.Qt.AlignCenter)
        self._n_jobs_le.setObjectName("_n_jobs_le")
        self.verticalLayout.addWidget(self._n_jobs_le)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(35)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self._mean_freqs_lb = QtWidgets.QLabel(self.groupBox_2)
        self._mean_freqs_lb.setMinimumSize(QtCore.QSize(0, 25))
        self._mean_freqs_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._mean_freqs_lb.setFont(font)
        self._mean_freqs_lb.setObjectName("_mean_freqs_lb")
        self.verticalLayout_6.addWidget(self._mean_freqs_lb)
        self._mean_freq_band_lb = QtWidgets.QLabel(self.groupBox_2)
        self._mean_freq_band_lb.setMinimumSize(QtCore.QSize(0, 25))
        self._mean_freq_band_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._mean_freq_band_lb.setFont(font)
        self._mean_freq_band_lb.setObjectName("_mean_freq_band_lb")
        self.verticalLayout_6.addWidget(self._mean_freq_band_lb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self._mean_freqs_cbx = QtWidgets.QComboBox(self.groupBox_2)
        self._mean_freqs_cbx.setMinimumSize(QtCore.QSize(100, 25))
        self._mean_freqs_cbx.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._mean_freqs_cbx.setFont(font)
        self._mean_freqs_cbx.setObjectName("_mean_freqs_cbx")
        self._mean_freqs_cbx.addItem("")
        self._mean_freqs_cbx.addItem("")
        self.verticalLayout_5.addWidget(self._mean_freqs_cbx)
        self._mean_freq_band_le = QtWidgets.QLineEdit(self.groupBox_2)
        self._mean_freq_band_le.setMinimumSize(QtCore.QSize(100, 25))
        self._mean_freq_band_le.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._mean_freq_band_le.setFont(font)
        self._mean_freq_band_le.setFocusPolicy(QtCore.Qt.ClickFocus)
        self._mean_freq_band_le.setAlignment(QtCore.Qt.AlignCenter)
        self._mean_freq_band_le.setObjectName("_mean_freq_band_le")
        self.verticalLayout_5.addWidget(self._mean_freq_band_le)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self._plot_btn = QtWidgets.QPushButton(self.groupBox_2)
        self._plot_btn.setMinimumSize(QtCore.QSize(120, 25))
        self._plot_btn.setMaximumSize(QtCore.QSize(500, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self._plot_btn.setFont(font)
        self._plot_btn.setObjectName("_plot_btn")
        self.verticalLayout_4.addWidget(self._plot_btn)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Calculation Parameters"))
        self.Multitaper_method_lb.setText(_translate("MainWindow", "Morlet"))
        self._compute_btn.setText(_translate("MainWindow", "Compute"))
        self._compute_btn.setShortcut(_translate("MainWindow", "Return"))
        self._chan_lb.setText(_translate("MainWindow", "Channels"))
        self._freq_band_lb.setText(_translate("MainWindow", "Freq band (Hz)"))
        self._freq_step_lb.setText(_translate("MainWindow", "Freq step (Hz)"))
        self._denom_ncycles_lb.setText(_translate("MainWindow", "Denom of n_cycles for each freq"))
        self._n_jobs_lb.setText(_translate("MainWindow", "Number of jobs"))
        self._select_chan_btn.setText(_translate("MainWindow", "..."))
        self._freq_step_le.setText(_translate("MainWindow", "1"))
        self._denom_ncycles_le.setText(_translate("MainWindow", "2"))
        self._n_jobs_le.setText(_translate("MainWindow", "3"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Figure Configuration"))
        self._mean_freqs_lb.setText(_translate("MainWindow", "Mean across freqs"))
        self._mean_freq_band_lb.setText(_translate("MainWindow", "Freq band (Hz)"))
        self._mean_freqs_cbx.setItemText(0, _translate("MainWindow", "True"))
        self._mean_freqs_cbx.setItemText(1, _translate("MainWindow", "False"))
        self._plot_btn.setText(_translate("MainWindow", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
