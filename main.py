import sys
import random

from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox, QSpinBox, QPushButton
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTextEdit, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.qp = QtGui.QPainter()

        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        self.qp.begin(self)
        r = random.randint(5, 50)
        x = random.randint(r, self.width() - r)
        y = random.randint(r, self.height() - r)
        self.qp.setPen(QtGui.QColor(190, 190, 0))
        self.qp.setBrush(QtGui.QColor(0, 0, 0, 0))
        self.qp.drawEllipse(x, y, r, r)
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
