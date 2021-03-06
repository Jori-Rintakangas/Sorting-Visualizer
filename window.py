from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt, QTimer, QEventLoop
import random
import sys

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
ARRAY_LENGTH = 64

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.lines = {}
        self.arr_to_sort = []
        self.speed = 20
        self.count = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.position = START
        self.delay_loop = QEventLoop()
        self.red_pen = QPen(QtGui.QColor(255, 0, 0))
        self.black_pen = QPen(QtGui.QColor(0, 0, 0))
        self.init_ui()

    def closeEvent(self, event):
        event.accept()
        sys.exit(self.delay_loop.exit())

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
        self.animation_speed.setInvertedAppearance(True)
        self.animation_speed.setRange(1, 200)
        self.animation_speed.setValue(40)
        self.animation_speed.valueChanged.connect(self.change_speed)

        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText('Animation Speed')
        self.text_label.move(25, 180)

        self.new_array_button = QtWidgets.QPushButton(self)
        self.new_array_button.setGeometry(20, 250, 100, 30)
        self.new_array_button.setText('New Array')
        self.new_array_button.clicked.connect(self.new_array)

    def sort_array(self):
        self.visualize_button.setEnabled(False)
        self.new_array_button.setEnabled(False)
        sort_method = self.sort_methods.currentText()
        if sort_method == 'Bubble Sort':
            self.bubble_sort()
        elif sort_method == 'Quick Sort':
            end = len(self.arr_to_sort) - 1
            self.quick_sort(self.arr_to_sort, 0, end)
        elif sort_method == 'Merge Sort':
            self.merge_sort(self.arr_to_sort)
        self.new_array_button.setEnabled(True)

    def change_speed(self):
        self.speed = self.animation_speed.value()

    def delay(self):
        self.delay_loop = QEventLoop()
        QTimer.singleShot(self.speed, self.delay_loop.quit)
        self.delay_loop.exec_()

    def create_array(self):
        return random.sample(range(2, 350), ARRAY_LENGTH)

    def new_array(self):
        self.reset()
        self.visualize_button.setEnabled(False)
        self.new_array_button.setEnabled(False)
        pen = self.black_pen
        pen.setWidth(4)
        arr = self.create_array()
        start = START
        for length in arr:
            line = self.scene.addLine(0, 0, 0, length, pen)
            line.moveBy(start, VIEW_H-length)
            self.lines[length] = line
            self.arr_to_sort.append(length)
            start += STEP
        self.visualize_button.setEnabled(True)
        self.new_array_button.setEnabled(True)

    def reset(self):
        self.count = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.position = START
        self.scene.clear()
        self.lines.clear()
        self.arr_to_sort.clear()

    def bubble_sort(self):
        for i in range(1, len(self.arr_to_sort)):

            for j in range(0, len(self.arr_to_sort)-i):
                first = self.arr_to_sort[j]
                second = self.arr_to_sort[j+1]

                if first > second:
                    self.arr_to_sort[j] = second
                    self.arr_to_sort[j+1] = first
                    self.delay()
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
                        self.delay()
                        self.swap_lines(self.arr_to_sort[partition_ind], self.arr_to_sort[i])

                    self.arr_to_sort[i] = self.arr_to_sort[partition_ind]
                    self.arr_to_sort[partition_ind] = element
                    partition_ind += 1

            self.delay()
            self.swap_lines(self.arr_to_sort[partition_ind], self.arr_to_sort[end])

            self.arr_to_sort[end] = self.arr_to_sort[partition_ind]
            self.arr_to_sort[partition_ind] = pivot

            self.quick_sort(arr, start, partition_ind - 1)
            self.quick_sort(arr, partition_ind + 1, end)

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr

        length = len(arr)
        left = arr[0:length//2]
        right = arr[length//2:length]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)

    def merge(self, left, right):
        combined = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                combined.append(left[0])
                left.pop(0)
            else:
                combined.append(right[0])
                right.pop(0)

        if len(left) == 0:
            combined.extend(right)
        else:
            combined.extend(left)

        self.delay()
        self.sort_lines(combined)
        self.delay()
        return combined

    def swap_lines(self, first, second):
        x_1 = self.lines[first].x()
        x_2 = self.lines[second].x()
        diff = x_2 - x_1

        self.lines[first].moveBy(diff, 0)
        self.lines[second].moveBy(-diff, 0)

    def sort_lines(self, lines):
        self.delay()
        if len(lines) == ARRAY_LENGTH / 16:
            self.position = START + self.count * STEP
            self.count += ARRAY_LENGTH / 16

        elif len(lines) == ARRAY_LENGTH / 8:
            self.position = START + self.count2 * STEP
            self.count2 += ARRAY_LENGTH / 8

        elif len(lines) == ARRAY_LENGTH / 4:
            self.position = START + self.count3 * STEP
            self.count3 += ARRAY_LENGTH / 4

        elif len(lines) == ARRAY_LENGTH / 2:
            self.position = START + self.count4 * STEP
            self.count4 += ARRAY_LENGTH / 2

        elif len(lines) == ARRAY_LENGTH:
            self.position = START
        self.delay()
        for line in lines:
            self.lines[line].setPos(self.position, VIEW_H - line)
            self.position += STEP
