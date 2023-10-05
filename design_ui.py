# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(564, 513)
        icon = QIcon()
        icon.addFile(u"images.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_add = QGridLayout()
        self.gridLayout_add.setObjectName(u"gridLayout_add")
        self.description = QLabel(self.centralwidget)
        self.description.setObjectName(u"description")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.description.setFont(font)

        self.gridLayout_add.addWidget(self.description, 1, 0, 1, 1)

        self.RB_unimportant = QRadioButton(self.centralwidget)
        self.RB_unimportant.setObjectName(u"RB_unimportant")
        self.RB_unimportant.setFont(font)

        self.gridLayout_add.addWidget(self.RB_unimportant, 5, 1, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.btn_add.setFont(font1)
        self.btn_add.setStyleSheet(u"background-color: rgb(168, 168, 168);\n"
"color: rgb(0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u"download.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon1)
        self.btn_add.setIconSize(QSize(40, 40))
        self.btn_add.setAutoDefault(False)
        self.btn_add.setFlat(False)

        self.gridLayout_add.addWidget(self.btn_add, 5, 2, 1, 3)

        self.tb_description = QLineEdit(self.centralwidget)
        self.tb_description.setObjectName(u"tb_description")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.tb_description.setFont(font2)
        self.tb_description.setStyleSheet(u"background-color: rgb(168, 168, 168);\n"
"color: rgb(0, 0, 0);")
        self.tb_description.setAlignment(Qt.AlignCenter)

        self.gridLayout_add.addWidget(self.tb_description, 1, 1, 1, 4)

        self.date = QLabel(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setFont(font)

        self.gridLayout_add.addWidget(self.date, 3, 0, 1, 1)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setFont(font)

        self.gridLayout_add.addWidget(self.title, 0, 0, 1, 1)

        self.tb_time = QLineEdit(self.centralwidget)
        self.tb_time.setObjectName(u"tb_time")
        self.tb_time.setFont(font2)
        self.tb_time.setStyleSheet(u"background-color: rgb(168, 168, 168);\n"
"color: rgb(0, 0, 0);")
        self.tb_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_add.addWidget(self.tb_time, 3, 4, 1, 1)

        self.tb_title = QLineEdit(self.centralwidget)
        self.tb_title.setObjectName(u"tb_title")
        self.tb_title.setFont(font2)
        self.tb_title.setStyleSheet(u"background-color: rgb(168, 168, 168);\n"
"color: rgb(0, 0, 0);")
        self.tb_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_add.addWidget(self.tb_title, 0, 1, 1, 4)

        self.tb_date = QLineEdit(self.centralwidget)
        self.tb_date.setObjectName(u"tb_date")
        self.tb_date.setFont(font2)
        self.tb_date.setStyleSheet(u"background-color: rgb(168, 168, 168);\n"
"color: rgb(0, 0, 0);")
        self.tb_date.setAlignment(Qt.AlignCenter)

        self.gridLayout_add.addWidget(self.tb_date, 3, 1, 1, 2)

        self.RB_important = QRadioButton(self.centralwidget)
        self.RB_important.setObjectName(u"RB_important")
        self.RB_important.setFont(font)

        self.gridLayout_add.addWidget(self.RB_important, 5, 0, 1, 1)

        self.time = QLabel(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setFont(font)

        self.gridLayout_add.addWidget(self.time, 3, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_add, 1, 0, 1, 2)

        self.gridLayout_main = QGridLayout()
        self.gridLayout_main.setObjectName(u"gridLayout_main")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.tabWidget.setFont(font3)
        self.tabWidget.setStyleSheet(u"background-color: rgb(168, 168, 168);\n"
"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.tab_reminder = QWidget()
        self.tab_reminder.setObjectName(u"tab_reminder")
        self.gridLayout_4 = QGridLayout(self.tab_reminder)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_reminder = QGridLayout()
        self.gridLayout_reminder.setObjectName(u"gridLayout_reminder")

        self.gridLayout_4.addLayout(self.gridLayout_reminder, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_reminder, "")
        self.tab_done = QWidget()
        self.tab_done.setObjectName(u"tab_done")
        self.gridLayout_6 = QGridLayout(self.tab_done)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_done = QGridLayout()
        self.gridLayout_done.setObjectName(u"gridLayout_done")

        self.gridLayout_6.addLayout(self.gridLayout_done, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_done, "")

        self.gridLayout_main.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_main, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_add.setDefault(False)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDo List", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(QCoreApplication.translate("MainWindow", u"Programmer: Ali Yaghoubian", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.description.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.RB_unimportant.setText(QCoreApplication.translate("MainWindow", u"Unimportant", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.tb_date.setText("")
        self.RB_important.setText(QCoreApplication.translate("MainWindow", u"Important", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reminder), QCoreApplication.translate("MainWindow", u"Remember", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_done), QCoreApplication.translate("MainWindow", u"Done", None))
    # retranslateUi

