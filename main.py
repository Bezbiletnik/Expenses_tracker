import sys
import datetime
import platform

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate,
                            QDateTime, QMetaObject, QObject, QPoint,
                            QRect, QSize, QTime, QUrl, Qt, QEvent
                            )
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient
                           )
from PySide2.QtWidgets import *
from PySide2.QtSql import (QSqlDatabase, QSqlQuery)

# GUI FILES

from ui_main import Ui_MainWindow
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btn_Toggle.setIcon(QIcon('icons/menu.svg'))
        self.ui.Btn_page_1.setIcon(QIcon('icons/transaction.svg'))
        self.ui.Btn_page_2.setIcon(QIcon('icons/pie-chart.svg'))
        self.ui.Btn_page_3.setIcon(QIcon('icons/wallet.svg'))
        # TOGGLE MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggle_menu(self, 250, True))

        # PAGES
        # PAGE 1
        self.ui.Btn_page_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        UIFunctions.load_data(self)
        self.ui.date_time_edit.setDateTime(datetime.datetime.now())
        self.ui.btn_upload.clicked.connect(lambda: UIFunctions.load_data(self))
        self.ui.btn_remove.clicked.connect(lambda: UIFunctions.remove_row(self))
        self.ui.btn_save.clicked.connect(lambda: UIFunctions.save_data(self))

        # PAGE 2
        self.ui.Btn_page_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))
        self.ui.Btn_page_2.clicked.connect(lambda: UIFunctions.graph_plot(self))
        # PAGE 3
        self.ui.Btn_page_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
