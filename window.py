from PyQt5 import QtWidgets
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
import random

X_POS = 900
Y_POS = 500
WIDTH = 1000
HEIGHT = 500
VIEW_W = 800
VIEW_H = 400
LEFT_MARGIN = 140
TOP_MARGIN = 40

STEP = 10
START = 100

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(X_POS, Y_POS, WIDTH, HEIGHT)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self)

        self.scene.setSceneRect(0,0, VIEW_W - 2, VIEW_H - 2)
        self.view.setGeometry(LEFT_MARGIN, TOP_MARGIN, VIEW_W, VIEW_H)
        self.view.setScene(self.scene)

        self.sort_methods = QtWidgets.QComboBox(self)
        self.sort_methods.setGeometry(20, 40, 100, 30)
        methods = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
        self.sort_methods.insertItems(0, methods)

        self.visualize_button = QtWidgets.QPushButton(self)
        self.visualize_button.setGeometry(20, 90, 100, 30)
        self.visualize_button.setText('Visualize')

        self.animation_speed = QtWidgets.QSlider(Qt.Horizontal, self)
        self.animation_speed.setGeometry(20, 160, 100, 20)

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText('Animation Speed')
        self.text_label.move(25, 180)

        self.new_array_button = QtWidgets.QPushButton(self)
        self.new_array_button.setGeometry(20, 250, 100, 30)
        self.new_array_button.setText('New Array')


    def create_array(self):
        return random.sample(range(2, 350), 60)

    def new_array(self):
        pen = QPen(QtGui.QColor(0,0,0))
        pen.setWidth(4)
        arr = self.create_array()
        start = START
        for length in arr:
            self.scene.addLine(start, VIEW_H, start, VIEW_H-length, pen)
            start += STEP


        





