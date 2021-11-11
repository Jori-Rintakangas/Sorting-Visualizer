from PyQt5 import QtWidgets
import PyQt5
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt

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

        sort_methods = QtWidgets.QComboBox(self)
        sort_methods.setGeometry(20, 40, 100, 30)
        methods = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
        sort_methods.insertItems(0, methods)

        visualize_button = QtWidgets.QPushButton(self)
        visualize_button.setGeometry(20, 90, 100, 30)
        visualize_button.setText('Visualize')

        animation_speed = QtWidgets.QSlider(Qt.Horizontal, self)
        animation_speed.setGeometry(20, 160, 100, 20)

        text_label = QtWidgets.QLabel(self)
        text_label.setText('Animation Speed')
        text_label.move(25, 180)

        new_array_button = QtWidgets.QPushButton(self)
        new_array_button.setGeometry(20, 250, 100, 30)
        new_array_button.setText('New Array')





