from PyQt5 import QtWidgets
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsLineItem, QMainWindow
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

        self.lines = {}
        self.arr_to_sort = []

        self.init_ui()

    def init_ui(self):
        self.setGeometry(X_POS, Y_POS, WIDTH, HEIGHT)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self)

        self.scene.setSceneRect(0,0, VIEW_W - 2, VIEW_H - 2)
        self.view.setGeometry(LEFT_MARGIN, TOP_MARGIN, VIEW_W, VIEW_H)
        self.view.setScene(self.scene)

        self.sort_methods = QtWidgets.QComboBox(self)
        self.sort_methods.setGeometry(20, 40, 100, 30)
        methods = ['Bubble Sort', 'Quick Sort', 'Merge Sort']
        self.sort_methods.insertItems(0, methods)

        self.visualize_button = QtWidgets.QPushButton(self)
        self.visualize_button.setGeometry(20, 90, 100, 30)
        self.visualize_button.setText('Visualize')
        self.visualize_button.clicked.connect(self.sort_array)

        self.animation_speed = QtWidgets.QSlider(Qt.Horizontal, self)
        self.animation_speed.setGeometry(20, 160, 100, 20)

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText('Animation Speed')
        self.text_label.move(25, 180)

        self.new_array_button = QtWidgets.QPushButton(self)
        self.new_array_button.setGeometry(20, 250, 100, 30)
        self.new_array_button.setText('New Array')


    def sort_array(self):
        sort_method = self.sort_methods.currentText()
        if sort_method == 'Bubble Sort':
            self.bubble_sort()
        elif sort_method == 'Quick Sort':
            end = len(self.arr_to_sort) - 1
            self.quick_sort(self.arr_to_sort, 0, end)
        else:
            self.merge_sort()


    def create_array(self):
        return random.sample(range(2, 350), 60)

    def new_array(self):
        pen = QPen(QtGui.QColor(0,0,0))
        pen.setWidth(4)
        arr = self.create_array()
        start = START
        for length in arr:
            line = self.scene.addLine(0, 0, 0, length, pen)
            line.moveBy(start, VIEW_H-length)
            self.lines[length] = line
            self.arr_to_sort.append(length)
            start += STEP

    def bubble_sort(self):
        for i in range(1, len(self.arr_to_sort)):

            for j in range(0, len(self.arr_to_sort)-i):
                first = self.arr_to_sort[j]
                second = self.arr_to_sort[j+1]

                if first > second:
                    self.arr_to_sort[j] = second
                    self.arr_to_sort[j+1] = first
                    self.swap_lines(first, second)
        

    def quick_sort(self, arr, start, end):

        if start < end:
            # Partition
            partition_ind = start
            pivot = self.arr_to_sort[end]
            for i in range(start, end):
                
                element = self.arr_to_sort[i]
                if element <= pivot:
                    if partition_ind != i:
                        self.swap_lines(self.arr_to_sort[partition_ind], self.arr_to_sort[i])

                    self.arr_to_sort[i] = self.arr_to_sort[partition_ind]
                    self.arr_to_sort[partition_ind] = element
                    partition_ind += 1

            self.swap_lines(self.arr_to_sort[partition_ind], self.arr_to_sort[end])

            self.arr_to_sort[end] = self.arr_to_sort[partition_ind]
            self.arr_to_sort[partition_ind] = pivot
            

            self.quick_sort(arr, start, partition_ind - 1)
            self.quick_sort(arr, partition_ind + 1, end)
            







    def merge_sort(self):
        pass

    def swap_lines(self, first, second):
        x_1 = self.lines[first].x()
        x_2 = self.lines[second].x()
        diff = x_2 - x_1

        self.lines[first].moveBy(diff, 0)
        self.lines[second].moveBy(-diff, 0)




        
        





