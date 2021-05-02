import sqlalchemy
import matplotlib
import sqlite3
import pandas as pd
import numpy as np
from main import *
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')

engine = sqlalchemy.create_engine('sqlite:///a.db')


class UIFunctions(MainWindow):
    def toggle_menu(self, max_width, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            max_extend = max_width
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def remove_row(self):
        connection = sqlite3.connect('a.db')
        cur = connection.cursor()
        if self.ui.expanses_table.rowCount() > 0:
            self.ui.expanses_table.removeRow(self.ui.expanses_table.rowCount()-1)
            cur.execute('''DELETE FROM expenses WHERE  rowid = (SELECT Max(rowid) FROM expenses)''')
            connection.commit()
            cur.close()
            connection.close()

    def load_data(self):

        self.ui.expanses_table.setRowCount(0)
        connection = sqlite3.connect('a.db')
        cur = connection.cursor()
        cur.execute('''SELECT * FROM expenses''')

        rows = cur.fetchall()
        for row in rows:
            inx = rows.index(row)
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, row[1])
            self.ui.expanses_table.insertRow(inx)
            self.ui.expanses_table.setItem(inx, 0, QTableWidgetItem(row[0]))
            self.ui.expanses_table.setItem(inx, 1, item)
            self.ui.expanses_table.setItem(inx, 2, QTableWidgetItem(row[2]))

        cur.close()
        connection.close()

    def save_data(self):
        connection = sqlite3.connect('a.db')
        cur = connection.cursor()
        result = ''
        for num in range(3):
            section = self.ui.date_time_edit.sectionAt(num)
            value = self.ui.date_time_edit.sectionText(section)
            result += f'/{value}'

        cur.execute('''INSERT INTO expenses(date, amount, categories) VALUES (?, ?, ?)''',
                    (result[1:], self.ui.amount_edit.text(), self.ui.category_box.currentText()))

        cur.close()
        connection.commit()
        connection.close()

    def graph_plot(self):
        df = pd.read_sql_table('expenses', engine)
        results = df.groupby(['categories']).sum()
        ax = self.ui.canvas.figure.subplots()
        ax.pie(x=results.values.flatten(), labels=results.axes[0])
        self.ui.canvas.draw()
