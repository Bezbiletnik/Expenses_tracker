# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main(2)elxoKO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from canvas import Canvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMinimumSize(QSize(0, 40))
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle_menu = QFrame(self.Top_Bar)
        self.frame_toggle_menu.setObjectName(u"frame_toggle_menu")
        self.frame_toggle_menu.setMaximumSize(QSize(70, 40))
        self.frame_toggle_menu.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle_menu.setFrameShape(QFrame.NoFrame)
        self.frame_toggle_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle_menu)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle_menu)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_page_1 = QPushButton(self.frame_top_menus)
        self.Btn_page_1.setObjectName(u"Btn_page_1")
        self.Btn_page_1.setMinimumSize(QSize(0, 40))
        self.Btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(225, 225, 225);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_page_1)

        self.Btn_page_2 = QPushButton(self.frame_top_menus)
        self.Btn_page_2.setObjectName(u"Btn_page_2")
        self.Btn_page_2.setMinimumSize(QSize(0, 40))
        self.Btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(225, 225, 225);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_page_2)

        self.Btn_page_3 = QPushButton(self.frame_top_menus)
        self.Btn_page_3.setObjectName(u"Btn_page_3")
        self.Btn_page_3.setMinimumSize(QSize(0, 40))
        self.Btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(225, 225, 225);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout_3 = QHBoxLayout(self.page_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.choice_frame = QFrame(self.frame_2)
        self.choice_frame.setObjectName(u"choice_frame")
        self.choice_frame.setFrameShape(QFrame.StyledPanel)
        self.choice_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.choice_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_upload = QPushButton(self.choice_frame)
        self.btn_upload.setObjectName(u"btn_upload")
        font = QFont()
        font.setPointSize(15)
        self.btn_upload.setFont(font)
        self.btn_upload.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_upload)

        self.btn_remove = QPushButton(self.choice_frame)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setFont(font)
        self.btn_remove.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_remove)


        self.verticalLayout_6.addWidget(self.choice_frame)

        self.table_frame = QFrame(self.frame_2)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.table_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.expanses_table = QTableWidget(self.table_frame)
        if (self.expanses_table.columnCount() < 3):
            self.expanses_table.setColumnCount(3)
        font1 = QFont()
        font1.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(85, 170, 255));
        self.expanses_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.expanses_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.expanses_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.expanses_table.setObjectName(u"expanses_table")
        self.expanses_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.expanses_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.expanses_table.horizontalHeader().setDefaultSectionSize(230)

        self.verticalLayout_10.addWidget(self.expanses_table)


        self.verticalLayout_6.addWidget(self.table_frame)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(175, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.main_frame = QFrame(self.frame)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.main_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.date_label = QLabel(self.main_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setMaximumSize(QSize(16777215, 40))
        self.date_label.setFont(font1)
        self.date_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.date_label)

        self.date_time_edit = QDateTimeEdit(self.main_frame)
        self.date_time_edit.setObjectName(u"date_time_edit")
        self.date_time_edit.setFont(font1)
        self.date_time_edit.setAutoFillBackground(False)
        self.date_time_edit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.date_time_edit.setCalendarPopup(True)

        self.verticalLayout_9.addWidget(self.date_time_edit)

        self.amount_label = QLabel(self.main_frame)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setMaximumSize(QSize(16777215, 16777215))
        self.amount_label.setFont(font1)
        self.amount_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.amount_label)

        self.amount_edit = QLineEdit(self.main_frame)
        self.amount_edit.setObjectName(u"amount_edit")
        self.amount_edit.setFont(font1)
        self.amount_edit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.amount_edit)

        self.category_label = QLabel(self.main_frame)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setMaximumSize(QSize(16777215, 16777215))
        self.category_label.setFont(font1)
        self.category_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.category_label)

        self.category_box = QComboBox(self.main_frame)
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.addItem("")
        self.category_box.setObjectName(u"category_box")
        self.category_box.setFont(font1)
        self.category_box.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.category_box)

        self.btn_save = QPushButton(self.main_frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_save)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.verticalLayout_11.addWidget(self.main_frame)


        self.horizontalLayout_3.addWidget(self.frame)

        self.Pages_Widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.canvas = Canvas(self.page_2)
        self.canvas.setObjectName(u"canvas")

        self.horizontalLayout_5.addWidget(self.canvas)

        self.Pages_Widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Pages_Widget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.Btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Transaction", None))
        self.Btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Statistic", None))
        self.Btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Wallet", None))
        self.btn_upload.setText(QCoreApplication.translate("MainWindow", u"UPLOAD", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        ___qtablewidgetitem = self.expanses_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.expanses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem2 = self.expanses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.date_time_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy", None))
        self.amount_label.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.amount_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"$ 0", None))
        self.category_label.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.category_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Bills", None))
        self.category_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Education", None))
        self.category_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Food", None))
        self.category_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Health", None))
        self.category_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Shopping", None))

        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
    # retranslateUi

