# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1751, 881))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dataset_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.dataset_table.setObjectName("dataset_table")
        self.dataset_table.setColumnCount(14)
        self.dataset_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataset_table.setHorizontalHeaderItem(13, item)
        self.gridLayout.addWidget(self.dataset_table, 1, 1, 1, 1)
        self.dataset_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dataset_label.setObjectName("dataset_label")
        self.gridLayout.addWidget(self.dataset_label, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sample_dataset_2 = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_dataset_2.sizePolicy().hasHeightForWidth())
        self.sample_dataset_2.setSizePolicy(sizePolicy)
        self.sample_dataset_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.sample_dataset_2.setObjectName("sample_dataset_2")
        self.sample_dataset_2.setColumnCount(2)
        self.sample_dataset_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sample_dataset_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sample_dataset_2.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.sample_dataset_2)
        self.distribution_layout_1 = QtWidgets.QVBoxLayout()
        self.distribution_layout_1.setObjectName("distribution_layout_1")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.distribution_layout_1.addWidget(self.label)
        self.horizontalLayout.addLayout(self.distribution_layout_1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 6, 0, 1, 1)
        self.standart_dev = QtWidgets.QLabel(self.gridLayoutWidget)
        self.standart_dev.setText("")
        self.standart_dev.setObjectName("standart_dev")
        self.gridLayout_2.addWidget(self.standart_dev, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 7, 0, 1, 1)
        self.model_score_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.model_score_1.setText("")
        self.model_score_1.setObjectName("model_score_1")
        self.gridLayout_2.addWidget(self.model_score_1, 7, 1, 1, 1)
        self.correl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.correl.setText("")
        self.correl.setObjectName("correl")
        self.gridLayout_2.addWidget(self.correl, 4, 1, 1, 1)
        self.coeff_pirson = QtWidgets.QLabel(self.gridLayoutWidget)
        self.coeff_pirson.setText("")
        self.coeff_pirson.setObjectName("coeff_pirson")
        self.gridLayout_2.addWidget(self.coeff_pirson, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.count = QtWidgets.QLabel(self.gridLayoutWidget)
        self.count.setText("")
        self.count.setObjectName("count")
        self.gridLayout_2.addWidget(self.count, 0, 1, 1, 1)
        self.coefficient_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.coefficient_1.setText("")
        self.coefficient_1.setObjectName("coefficient_1")
        self.gridLayout_2.addWidget(self.coefficient_1, 6, 1, 1, 1)
        self.avg = QtWidgets.QLabel(self.gridLayoutWidget)
        self.avg.setText("")
        self.avg.setObjectName("avg")
        self.gridLayout_2.addWidget(self.avg, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)
        self.intercept_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.intercept_1.setText("")
        self.intercept_1.setObjectName("intercept_1")
        self.gridLayout_2.addWidget(self.intercept_1, 5, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.regression_layout_1 = QtWidgets.QVBoxLayout()
        self.regression_layout_1.setObjectName("regression_layout_1")
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_19.setObjectName("label_19")
        self.regression_layout_1.addWidget(self.label_19)
        self.horizontalLayout.addLayout(self.regression_layout_1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sample_dataset_3 = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_dataset_3.sizePolicy().hasHeightForWidth())
        self.sample_dataset_3.setSizePolicy(sizePolicy)
        self.sample_dataset_3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.sample_dataset_3.setObjectName("sample_dataset_3")
        self.sample_dataset_3.setColumnCount(3)
        self.sample_dataset_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sample_dataset_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sample_dataset_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sample_dataset_3.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.sample_dataset_3)
        self.regression_layout_2 = QtWidgets.QVBoxLayout()
        self.regression_layout_2.setObjectName("regression_layout_2")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_20.setObjectName("label_20")
        self.regression_layout_2.addWidget(self.label_20)
        self.horizontalLayout_2.addLayout(self.regression_layout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 2, 0, 1, 1)
        self.intercept_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.intercept_2.setText("")
        self.intercept_2.setObjectName("intercept_2")
        self.gridLayout_3.addWidget(self.intercept_2, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)
        self.coefficient_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.coefficient_2.setText("")
        self.coefficient_2.setObjectName("coefficient_2")
        self.gridLayout_3.addWidget(self.coefficient_2, 1, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_35.setObjectName("label_35")
        self.gridLayout_3.addWidget(self.label_35, 0, 0, 1, 1)
        self.model_score_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.model_score_2.setText("")
        self.model_score_2.setObjectName("model_score_2")
        self.gridLayout_3.addWidget(self.model_score_2, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.correlation_layout = QtWidgets.QVBoxLayout()
        self.correlation_layout.setObjectName("correlation_layout")
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_23.setObjectName("label_23")
        self.correlation_layout.addWidget(self.label_23)
        self.horizontalLayout_2.addLayout(self.correlation_layout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(1580, 900, 161, 41))
        self.load_button.setObjectName("load_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.dataset_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.dataset_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Track name"))
        item = self.dataset_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Artist name"))
        item = self.dataset_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.dataset_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "BPM"))
        item = self.dataset_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Energy"))
        item = self.dataset_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dance"))
        item = self.dataset_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "DB"))
        item = self.dataset_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Liveness"))
        item = self.dataset_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Valence"))
        item = self.dataset_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Len"))
        item = self.dataset_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Acoustic"))
        item = self.dataset_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Speech"))
        item = self.dataset_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "POP"))
        self.dataset_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Датасет</p></body></html>"))
        item = self.sample_dataset_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Energy"))
        item = self.sample_dataset_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dance"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Распределение</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Количество=</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Coefficient=</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Model score=</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Среднее=</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Значимость корреляции=</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Коэф. Пирсона=</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Стандартное отклонение=</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Intercept=</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Регрессия</p></body></html>"))
        item = self.sample_dataset_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Energy"))
        item = self.sample_dataset_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BPM"))
        item = self.sample_dataset_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dance"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Регрессия</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Model score=</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Coefficient=</p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Intercept=</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Корреляция</p></body></html>"))
        self.load_button.setText(_translate("MainWindow", "Загрузить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())