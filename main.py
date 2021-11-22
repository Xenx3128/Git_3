import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Circles.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(252, 240, 3))
            radius = random.randint(10, 150)
            x, y = random.randint(radius, 800 - radius), random.randint(50 + radius, 600 - radius)
            painter.drawEllipse(QPoint(x, y), radius, radius)
            painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())