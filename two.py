import sys
from random import randint, choice, randrange

from z import Ui_MainWindow
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPolygon, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(randrange(1, 400), randrange(1, 400), randrange(1, 400)))
        qp.drawEllipse(randrange(0, 400), randrange(0, 400), randrange(0, 400), randrange(0, 400))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())