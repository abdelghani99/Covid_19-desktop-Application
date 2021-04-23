import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib import image
import pandas as pd
import seaborn as sns
import webbrowser
from datetime import datetime
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel

from Functions import (
    return_realtime_stats_country,
    return_latest_stats,
    is_connected,
    Display_pie_chart,
    data_extract,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1416, 913)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1391, 821))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1381, 771))
        self.groupBox.setStyleSheet("font:  75 10pt  \"MS Shell Dlg 2\";\n")
        # "border: 5px solid  qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(90, 460, 601, 291))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(20, 40, 331, 51))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 331, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 331, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 331, 51))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(380, 40, 191, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 100, 191, 51))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_3.setGeometry(QtCore.QRect(380, 160, 191, 51))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_4.setGeometry(QtCore.QRect(380, 220, 191, 51))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 571, 81))
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(850, 460, 431, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 331, 51))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 331, 51))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 331, 51))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 220, 331, 51))
        self.label_10.setObjectName("label_10")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(90, 130, 1191, 291))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(40, 40, 211, 51))
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(350, 40, 401, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(40, 110, 341, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(40, 160, 341, 41))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(40, 210, 341, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(710, 110, 441, 41))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(710, 160, 441, 41))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(710, 210, 441, 41))
        self.label_17.setObjectName("label_17")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 40, 181, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.retrieve_country_data)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 140, 181, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(710, 490, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.refresh)

        self.label_2.raise_()
        self.groupBox_4.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.pushButton.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 1371, 781))
        self.groupBox_5.setStyleSheet("font:  75 10pt  \"MS Shell Dlg 2\";\n")
        # "border: 5px solid  qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255))")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(30, 120, 491, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 150, 112, 34))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 190, 112, 34))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 30, 131, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(420, 20, 541, 81))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_30 = QtWidgets.QLabel(self.groupBox_5)
        self.label_30.setGeometry(QtCore.QRect(550, 120, 801, 641))
        self.label_30.setObjectName("label_30")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 210, 491, 191))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 30, 151, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 30, 131, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 30, 131, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 80, 151, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_13.setGeometry(QtCore.QRect(180, 80, 161, 41))
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_15.setGeometry(QtCore.QRect(350, 80, 131, 41))
        self.pushButton_15.setObjectName("pushButton_15")

        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_8.setGeometry(QtCore.QRect(30, 420, 491, 91))
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_17.setGeometry(QtCore.QRect(160, 30, 151, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1416, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVID_19 Real Time Application"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Real-time COVID19 Updates and Stats World"))
        self.label.setText(_translate("MainWindow", "Recovered :"))
        self.label_3.setText(_translate("MainWindow", "Confirmed :"))
        self.label_4.setText(_translate("MainWindow", "Deaths :"))
        self.label_5.setText(_translate("MainWindow", "Refreshed on:"))
        self.label_2.setText(_translate("MainWindow", "         COVID_19 Statistical Data Processing & Visualization"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Real-time COVID19 Updates and stats France"))
        self.label_8.setText(_translate("MainWindow", "Confirmed:"))
        self.label_7.setText(_translate("MainWindow", "Recovered:"))
        self.label_9.setText(_translate("MainWindow", "Deaths:"))
        self.label_10.setText(_translate("MainWindow", "Refreshed on:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "COVID19 Updates and stats "))
        self.label_11.setText(_translate("MainWindow", "Enter Country name :"))
        self.label_12.setText(_translate("MainWindow", "Country:"))
        self.label_13.setText(_translate("MainWindow", "Recovered:"))
        self.label_14.setText(_translate("MainWindow", "Confirmed:"))
        self.label_15.setText(_translate("MainWindow", "Deaths:"))
        self.label_16.setText(_translate("MainWindow", "Active cases:"))
        self.label_17.setText(_translate("MainWindow", "Last update of Database"))
        self.pushButton_2.setText(_translate("MainWindow", "Load Data"))
        self.pushButton_3.setText(_translate("MainWindow", "Display Pie Chart"))
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.Display_pie_chart)
        self.pushButton_4.clicked.connect(self.load_image)
        self.pushButton_5.clicked.connect(self.Filtering)
        self.pushButton_15.clicked.connect(self.Laplacian)
        self.pushButton_13.clicked.connect(self.Canny_ope)
        self.pushButton_7.clicked.connect(self.sobel_x)
        self.pushButton_6.clicked.connect(self.sobel_y)
        self.pushButton_8.clicked.connect(self.Histogram)
        self.pushButton_17.clicked.connect(self.Open_website)

        self.pushButton.setText(_translate("MainWindow", "Reset "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("MainWindow", "Signal_Processing/Data_Visualization"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Loading Image"))
        self.pushButton_11.setText(_translate("MainWindow", "Histogram"))
        self.pushButton_12.setText(_translate("MainWindow", "LineGraph"))
        self.pushButton_4.setText(_translate("MainWindow", "Load Image"))
        self.label_6.setText(_translate("MainWindow", "         COVID_19 Image Processing & Visualization"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Image Processing"))
        self.pushButton_5.setText(_translate("MainWindow", "Filtering"))
        self.pushButton_6.setText(_translate("MainWindow", "Sobel Y"))
        self.pushButton_7.setText(_translate("MainWindow", "Sobel X"))
        self.pushButton_8.setText(_translate("MainWindow", "Histogram"))
        self.pushButton_13.setText(_translate("MainWindow", "Canny Operator"))

        self.pushButton_15.setText(_translate("MainWindow", "Laplacian"))

        self.groupBox_8.setTitle(_translate("MainWindow", "Processing Images using online application "))
        self.pushButton_17.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Image_Processing"))

        Fra = ["France", "BarPlot chart", "Histogram chart"]
        self.comboBox.addItems(Fra)
        self.comboBox.activated.connect(self.France_Plots)

        Ger = ["Germany", "BarPlot chart", "Histogram chart"]
        self.comboBox_2.addItems(Ger)
        self.comboBox_2.activated.connect(self.Germany_Plots)

        Swi = ["Switzerland", "BarPlot chart", "Histogram chart"]
        self.comboBox_3.addItems(Swi)
        self.comboBox_3.activated.connect(self.Switzerland_Plots)

        Itl = ["Italy", "BarPlot chart", "Histogram chart"]
        self.comboBox_4.addItems(Itl)
        self.comboBox_4.activated.connect(self.Italy_Plots)

    def refresh(self):
        msg = QMessageBox()
        network_check = is_connected()
        if network_check is False:
            msg.setIcon(QMessageBox.Information)
            msg.setText("Failed To Connect To Internet!")
            msg.setWindowTitle("Connection Check")
            msg.exec_()
        else:
            data_refresh = return_latest_stats()
            France_data = return_realtime_stats_country("France")
            date = datetime.now()
            for i, j in data_refresh.items():
                data = {"Data": data_refresh["Global"]}

            for k, v in data.items():
                recvr_data = "Recovered : {}".format(v["TotalRecovered"])
                cnfirm_data = "Confirmed : {}".format(v["TotalConfirmed"])
                death_data = "Deaths : {}".format(v["TotalDeaths"])
                date_data = "Refreshed On : {}".format(
                    date.strftime("%m/%d/%Y, %H:%M")
                )
            self.label.setText(recvr_data)
            self.label_3.setText(cnfirm_data)
            self.label_4.setText(death_data)
            self.label_5.setText(date_data)
            for a, b in France_data.items():
                data = {
                    "Confirmed": France_data["Confirmed"],
                    "Recovered": France_data["Recovered"],
                    "Deaths": France_data["Deaths"],
                    "Date": France_data["Date"],
                }
            for i, j in data.items():
                fin = {"Data": data}
            for k, v in fin.items():
                recvr_data = "Recovered : {}".format(v["Recovered"])
                cnfirm_data = "Confirmed : {}".format(v["Confirmed"])
                death_data = "Deaths : {}".format(v["Deaths"])
                date_data = "Refreshed On : {}".format(
                    date.strftime("%m/%d/%Y, %H:%M")
                )
            self.label_7.setText(recvr_data)
            self.label_8.setText(cnfirm_data)
            self.label_9.setText(death_data)
            self.label_10.setText(date_data)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Updated Successfully. ")
            msg.setWindowTitle("Refresh Done")
            msg.exec_()

    def retrieve_country_data(self):
        country_name = self.lineEdit.text()
        country_data_retrieve = return_realtime_stats_country(country_name)
        if country_data_retrieve is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Invalid Country! Please try again! ")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:

            for a, b in country_data_retrieve.items():
                data = {
                    "Country": country_data_retrieve["Country"],
                    "Confirmed": country_data_retrieve["Confirmed"],
                    "Recovered": country_data_retrieve["Recovered"],
                    "Deaths": country_data_retrieve["Deaths"],
                    "Active": country_data_retrieve["Active"],
                    "Date": country_data_retrieve["Date"],

                }

            for i, j in data.items():
                final_data = {"Data": data}
            for k, v in final_data.items():
                country = "Country Name : {}".format(v["Country"])
                recvr_data_country = "Recovered : {}".format(v["Recovered"])
                cnfirm_data_country = "Confirmed : {}".format(v["Confirmed"])
                death_data_country = "Deaths : {}".format(v["Deaths"])
                active_data_country = "Active : {}".format(v["Active"])
                date_data_country = "Database Last Updated On : {}".format(v["Date"])
            self.label_12.setText(country)
            self.label_13.setText(recvr_data_country)
            self.label_15.setText(death_data_country)
            self.label_17.setText(date_data_country)
            self.label_16.setText(active_data_country)
            self.label_14.setText(cnfirm_data_country)
            self.pushButton_3.setEnabled(True)

    def Display_pie_chart(self):
        country_name = self.lineEdit.text()
        country_data_retrieve = return_realtime_stats_country(country_name)
        data_to_plot = data_extract(country_data_retrieve)
        labels = ["Deaths", "Recovered cases", "Active cases", "Confirmed cases"]
        Display_pie_chart(data=data_to_plot, labels=labels)

    def France_Plots(self):
        # def Barplot_chart(self):
        plt.style.use('bmh')
        df = pd.read_csv('data_covid.csv')
        specified = df.loc[18700:19028]
        x = specified['date']
        y = specified['new_cases']
        plt.title('Covid19 daily cases in france')
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Daily cases', fontsize=18)
        plt.bar(x, y, color='Blue')
        plt.show()
        # def Histogram_chart(self):
        df = pd.read_csv('data_covid.csv')
        sns.set(rc={"figure.figsize": (2, 8)})
        specified = df.loc[18700:19028]
        x = specified['new_cases']
        ax = sns.displot(x, color='Blue')
        plt.title('Covid19 daily cases in france')
        plt.show()

    def Germany_Plots(self):
        # def Barplot_chart(self):
        plt.style.use('bmh')
        df = pd.read_csv('data_covid.csv')
        specified = df.loc[20109:20436]
        x = specified['date']
        y = specified['new_cases']
        plt.title('BarPlot')
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Daily cases', fontsize=18)
        plt.bar(x, y, color='Orange')
        plt.show()
        # def Histogram_chart(self):
        sns.set(rc={"figure.figsize": (2, 8)})
        x = specified['new_cases']
        ax = sns.displot(x, color='Orange')
        plt.show()

    def Switzerland_Plots(self):
        # def Barplot_chart(self):
        plt.style.use('bmh')
        df = pd.read_csv('data_covid.csv')
        specified = df.loc[50548:50876]
        x = specified['date']
        y = specified['new_cases']
        plt.title('BarPlot')
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Daily cases', fontsize=18)
        plt.bar(x, y, color='Red')
        plt.show()
        # def Histogram_chart(self):
        sns.set(rc={"figure.figsize": (2, 8)})
        x = specified['new_cases']
        ax = sns.displot(x, color='Red')
        plt.show()

    def Italy_Plots(self):
        # def Barplot_chart(self):
        plt.style.use('bmh')
        df = pd.read_csv('data_covid.csv')
        specified = df.loc[26665:26993]
        x = specified['date']
        y = specified['new_cases']
        plt.title('BarPlot')
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Daily cases', fontsize=18)
        plt.bar(x, y, color='Green')
        plt.show()
        # def Histogram_chart(self):
        sns.set(rc={"figure.figsize": (2, 8)})
        x = specified['new_cases']
        ax = sns.displot(x, color='Green')
        plt.show()
        
    def load_image(self):
        File = QFileDialog.getOpenFileName(None, 'OpenFile', 'D:\\covid', "Image file(*.jpg)")
        return File

    def Filtering(self):
        image = QtGui.QImage(QtGui.QImageReader("D:\\Covid\\Filtering.PNG").read())
        self.label_30.setPixmap(QtGui.QPixmap(image))
    def Histogram(self):
        image = QtGui.QImage(QtGui.QImageReader("D:\\Covid\\Histogram.PNG").read())
        self.label_30.setPixmap(QtGui.QPixmap(image))
    def Canny_ope(self):
        image = QtGui.QImage(QtGui.QImageReader("D:\\Covid\\Canny.PNG").read())
        self.label_30.setPixmap(QtGui.QPixmap(image))
    def Laplacian(self):
        image = QtGui.QImage(QtGui.QImageReader("D:\\Covid\\Laplacian.PNG").read())
        self.label_30.setPixmap(QtGui.QPixmap(image))
    def sobel_x(self):
        image = QtGui.QImage(QtGui.QImageReader("D:\\Covid\\Sobel_X.PNG").read())
        self.label_30.setPixmap(QtGui.QPixmap(image))
    def sobel_y(self):
        image = QtGui.QImage(QtGui.QImageReader("D:\\Covid\\Sobel_Y.PNG").read())
        self.label_30.setPixmap(QtGui.QPixmap(image))


    def Open_website(self):
        webbrowser.open('http://htmlsegmentation.s3.eu-north-1.amazonaws.com/index.html')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
