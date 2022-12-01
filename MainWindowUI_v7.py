from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from AddMemberUI_v5 import Ui_add_member
from Pandasmodel_v1 import PandasModel
from EditMemberUI_v5 import Ui_edit_member
from RemoveMemberUI import Ui_remove_member
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import pymongo
import pandas as pd
from PyQt6.QtCharts import QChart, QChartView, QPieSeries
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import plotly_express as px
import plotly.io as pio
from PyQt6.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setGeometry(QtCore.QRect(170, 0, 975, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setStyleSheet("#mainBody{background-color:#f4f4f4}\n""\n""")
        self.mainBody.setObjectName("mainBody")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainBody)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 980, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(270, 250, 49, 16))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)
        self.mreg_widjet = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mreg_widjet.sizePolicy().hasHeightForWidth())
        self.mreg_widjet.setSizePolicy(sizePolicy)
        self.mreg_widjet.setStyleSheet("#mreg_widjet{background-color:#f4f4f4}\n""")
        self.mreg_widjet.setObjectName("mreg_widjet")
        self.label_2 = QtWidgets.QLabel(self.mreg_widjet)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setObjectName("label_2")
        self.pushButton_add = QtWidgets.QPushButton(self.mreg_widjet)
        self.pushButton_add.setGeometry(QtCore.QRect(860, 168, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Estonian, QtCore.QLocale.Country.Estonia))
        self.pushButton_add.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_edit = QtWidgets.QPushButton(self.mreg_widjet)
        self.pushButton_edit.setGeometry(QtCore.QRect(860, 239, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_edit.sizePolicy().hasHeightForWidth())
        self.pushButton_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_edit.setFont(font)
        self.pushButton_edit.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Estonian, QtCore.QLocale.Country.Estonia))
        self.pushButton_edit.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.pushButton_remove = QtWidgets.QPushButton(self.mreg_widjet)
        self.pushButton_remove.setGeometry(QtCore.QRect(860, 310, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_remove.setFont(font)
        self.pushButton_remove.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Estonian, QtCore.QLocale.Country.Estonia))
        self.pushButton_remove.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.tableView = QtWidgets.QTableView(self.mreg_widjet)
        self.tableView.setGeometry(QtCore.QRect(10, 95, 830, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableView.setFont(font)
        self.tableView.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableView.setStyleSheet
        ("#tableView{\n"
        "border:none;\n"
        "QHeaderView::section{Background-color:#af3074;border-radius:14px\n""}\n""")
        stylesheet = "QHeaderView::section{Background-color:#e065a7;}"
        self.tableView.setStyleSheet(stylesheet)
        self.tableView.setObjectName("tableView")
        self.label_4 = QtWidgets.QLabel(self.mreg_widjet)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.mreg_widjet)
        self.textEdit.setGeometry(QtCore.QRect(850, 380, 111, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setStyleSheet("QTextEdit{\n""background-color:#f4f4f4;\n""border:None\n""}\n""")
        self.textEdit.setObjectName("textEdit")
        self.searchField = QtWidgets.QLineEdit(self.mreg_widjet)
        self.searchField.setGeometry(QtCore.QRect(520, 45, 321, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchField.sizePolicy().hasHeightForWidth())
        self.searchField.setSizePolicy(sizePolicy)
        self.searchField.setObjectName("searchField")
        self.comboBox = QtWidgets.QComboBox(self.mreg_widjet)
        self.comboBox.setGeometry(QtCore.QRect(850, 45, 111, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.label_6 = QtWidgets.QLabel(self.mreg_widjet)
        self.label_6.setGeometry(QtCore.QRect(430, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(False)
        self.label_6.setObjectName("label_6")
        self.pushButton_refresh = QtWidgets.QPushButton(self.mreg_widjet)
        self.pushButton_refresh.setGeometry(QtCore.QRect(860, 520, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Estonian, QtCore.QLocale.Country.Estonia))
        self.pushButton_refresh.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.stackedWidget.addWidget(self.mreg_widjet)
        self.page_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy)
        self.page_3.setObjectName("page_3")
        self.frame_byMonth = QtWidgets.QFrame(self.page_3)
        self.frame_byMonth.setGeometry(QtCore.QRect(30, 49, 911, 291))
        self.frame_byMonth.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_byMonth.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_byMonth.setObjectName("frame_byMonth")
        self.label_3 = QtWidgets.QLabel(self.frame_byMonth)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_byMonth = QtWidgets.QLabel(self.frame_byMonth)
        self.label_byMonth.setGeometry(QtCore.QRect(0, 20, 911, 271))
        self.label_byMonth.setText("")
        self.label_byMonth.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_byMonth.setObjectName("label_byMonth")
        self.frame_bySex = QtWidgets.QFrame(self.page_3)
        self.frame_bySex.setGeometry(QtCore.QRect(30, 350, 451, 241))
        self.frame_bySex.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bySex.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bySex.setObjectName("frame_bySex")
        self.label_7 = QtWidgets.QLabel(self.frame_bySex)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_bySex = QtWidgets.QLabel(self.frame_bySex)
        self.label_bySex.setGeometry(QtCore.QRect(0, 20, 451, 221))
        self.label_bySex.setText("")
        self.label_bySex.setObjectName("label_bySex")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(350, 20, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame_byAge = QtWidgets.QFrame(self.page_3)
        self.frame_byAge.setGeometry(QtCore.QRect(490, 350, 451, 241))
        self.frame_byAge.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_byAge.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_byAge.setObjectName("frame_byAge")
        self.label_8 = QtWidgets.QLabel(self.frame_byAge)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_byAge = QtWidgets.QLabel(self.frame_byAge)
        self.label_byAge.setGeometry(QtCore.QRect(0, 20, 451, 221))
        self.label_byAge.setText("")
        self.label_byAge.setObjectName("label_byAge")
        self.stackedWidget.addWidget(self.page_3)
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setGeometry(QtCore.QRect(0, 0, 175, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy)
        self.leftMenu.setStyleSheet("#leftMenu{background-color:#2f5373}\n"
        "\n"
        "QPushButton{\n"
        "  border:none;\n"
        "  background-color:transparent;\n"
        "  background:none;\n"
        "  padding:0;\n"
        "  margin:0;\n"
        "  color: #fff;\n"
        "}\n"
        "QFrame{border:none;}")
        self.leftMenu.setObjectName("leftMenu")
        self.frame = QtWidgets.QFrame(self.leftMenu)
        self.frame.setGeometry(QtCore.QRect(9, 9, 161, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Menu_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Menu_label.setFont(font)
        self.Menu_label.setObjectName("Menu_label")
        self.verticalLayout_2.addWidget(self.Menu_label)
        self.frame_2 = QtWidgets.QFrame(self.leftMenu)
        self.frame_2.setGeometry(QtCore.QRect(8, 57, 175, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("QPushButton:hover {background-color : #af3074;}\n""QPushButton{text-align:left}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_Home = QtWidgets.QPushButton(self.frame_2)
        self.btn_Home.setGeometry(QtCore.QRect(0, 28, 162, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Home.sizePolicy().hasHeightForWidth())
        self.btn_Home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_Home.setFont(font)
        self.btn_Home.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_Home.setIcon(icon)
        self.btn_Home.setIconSize(QtCore.QSize(24, 24))
        self.btn_Home.setObjectName("btn_Home")
        self.btn_memview = QtWidgets.QPushButton(self.frame_2)
        self.btn_memview.setGeometry(QtCore.QRect(0, 126, 162, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_memview.sizePolicy().hasHeightForWidth())
        self.btn_memview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_memview.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("trending-up.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_memview.setIcon(icon1)
        self.btn_memview.setIconSize(QtCore.QSize(24, 24))
        self.btn_memview.setObjectName("btn_memview")
        self.btn_memreg = QtWidgets.QPushButton(self.frame_2)
        self.btn_memreg.setGeometry(QtCore.QRect(0, 77, 162, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_memreg.sizePolicy().hasHeightForWidth())
        self.btn_memreg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_memreg.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("user-plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_memreg.setIcon(icon2)
        self.btn_memreg.setIconSize(QtCore.QSize(24, 24))
        self.btn_memreg.setObjectName("btn_memreg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        # Add up Code --------------------------------------
        self.display_table()
        self.tableView.verticalHeader().setVisible(False)

        #Connect -------------------------------------------
        self.pushButton_add.clicked.connect(self.add_member)
        self.pushButton_edit.clicked.connect(self.edit_member)
        self.pushButton_remove.clicked.connect(self.remove_member)
        self.pushButton_refresh.clicked.connect(self.display_table)

        self.btn_Home.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.btn_memreg.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.btn_memview.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))

        self.searchField.textChanged.connect(self.searchItem)
        self.btn_memview.clicked.connect(self.bar_chart)
        self.btn_memview.clicked.connect(self.pie_chart)
        self.btn_memview.clicked.connect(self.hist_chart)

    def add_member(self):
        dialog = QDialog()
        ui = Ui_add_member()
        ui.setupUi(dialog)
        dialog.exec()

    def edit_member(self):
        dialog = QDialog()
        ui = Ui_edit_member()
        ui.setupUi(dialog)
        dialog.exec()

    def remove_member(self):
        dialog = QDialog()
        ui = Ui_remove_member()
        ui.setupUi(dialog)
        dialog.exec()


    def display_table(self):
        try:
            self.comboBox.clear()
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            database = client["db_Quiz1"]
            collection = database["members"]
            df_json = pd.DataFrame(list(collection.find()))
            df_json.drop(columns=['_id'],inplace=True)
            df_json.fillna("",inplace=True)
            df_json = df_json.sort_values(by='Cus_ID',ascending=False)
            self.model = PandasModel(df_json)
            self.tableView.setModel(self.model)
            self.comboBox.addItems(df_json.columns)

        except:
            print('Connection to MongoDB Database Error')

        return(df_json,self.model)
       
    def searchItem(self, v):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        database = client["db_Quiz1"]
        collection = database["members"]
        df_json = pd.DataFrame(list(collection.find()))
        df_json.drop(columns=['_id'],inplace=True)
        df_json.fillna("",inplace=True)
        df_json = df_json.sort_values(by='Cus_ID',ascending=False)
        self.model = PandasModel(df_json)
        if df_json is None:
            return
        
        column_index = df_json.columns.get_loc(self.comboBox.currentText())
        for row_index in range(self.model.rowCount()):
            if v in self.model.index(row_index, column_index).data():
                self.tableView.setRowHidden(row_index, False)
            else:
                self.tableView.setRowHidden(row_index, True)

    def pie_chart(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        database = client["db_Quiz1"]
        collection = database["members"]
        df_json = pd.DataFrame(list(collection.find()))
        df_json.drop(columns=['_id'],inplace=True)
        df_json.fillna("",inplace=True)
        group_sex = df_json.groupby('Sex')['Name'].count().reset_index()
        fig = px.pie(group_sex,values = 'Name',names='Sex',width=451,height=321)
        pio.write_image(fig, "pie_chart.png")
        pixmap = QPixmap("pie_chart.png")
        self.label_bySex.setPixmap(pixmap)
        self.label_bySex.setScaledContents(False)
        self.label_bySex.show()

    def hist_chart(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        database = client["db_Quiz1"]
        collection = database["members"]
        df_json = pd.DataFrame(list(collection.find()))
        df_json.drop(columns=['_id'],inplace=True)
        df_json.fillna("",inplace=True)
        fig = px.histogram(df_json, x="Age", nbins=30,width=461,height=321)
        pio.write_image(fig, "hist_chart.png")
        pixmap = QPixmap("hist_chart.png")
        self.label_byAge.setPixmap(pixmap)
        self.label_byAge.setScaledContents(False)
        self.label_byAge.show()
    
    def bar_chart(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        database = client["db_Quiz1"]
        collection = database["members"]
        df_json = pd.DataFrame(list(collection.find()))
        df_json.drop(columns=['_id'],inplace=True)
        df_json.fillna("",inplace=True)
        df_json['month'] = df_json['RegisterDate'].dt.month
        group_date = df_json.groupby('month')['Name'].count().reset_index()
        group_date.rename(columns = {'Name':'Number'}, inplace = True)
        fig = px.line(group_date, x='month', y='Number',markers=True,width=871,height=301)
        pio.write_image(fig, "bar_chart.png")
        pixmap = QPixmap("bar_chart.png")
        self.label_byMonth.setPixmap(pixmap)
        self.label_byMonth.setScaledContents(False)
        self.label_byMonth.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PAGE 1"))
        self.label_2.setText(_translate("MainWindow", "MEMBER REGISTERATION "))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_edit.setText(_translate("MainWindow", "Edit"))
        self.pushButton_remove.setText(_translate("MainWindow", "Remove"))
        self.label_4.setText(_translate("MainWindow", "View Member List"))
        self.label_6.setText(_translate("MainWindow", "Search/Filter:"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Member Register by Month</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Member by Sex"))
        self.label_5.setText(_translate("MainWindow", "MEMBER ANALYTICS"))
        self.label_8.setText(_translate("MainWindow", "Member by Age"))
        self.Menu_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">MAIN MENU</span></p></body></html>"))
        self.btn_Home.setText(_translate("MainWindow", "Home"))
        self.btn_memview.setText(_translate("MainWindow", "Members Analytics"))
        self.btn_memreg.setText(_translate("MainWindow", "Member Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
