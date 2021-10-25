from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

X_POS = 900
Y_POS = 500
WIDTH = 1000
HEIGHT = 500
VIEW_W = 800
VIEW_H = 400
LEFT_MARGIN = 140
TOP_MARGIN = 40

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(X_POS, Y_POS, WIDTH, HEIGHT)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self)

        self.scene.setSceneRect(0,0, VIEW_W - 2, VIEW_H - 2)
        self.view.setGeometry(LEFT_MARGIN, TOP_MARGIN, VIEW_W, VIEW_H)
        self.view.setScene(self.scene)

