#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author=Daguhh
"""

import sys
import os

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
    QPushButton,
    QLabel,
    QGridLayout,
    QTextEdit
)
from PyQt5.QtGui import QPixmap
import qrcode
from PIL.ImageQt import ImageQt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.dx = 0
        self.dy = 0

        grid = QGridLayout()

        textqr = QLabel('Enter text to convert')
        self.textboxqr = QTextEdit()
        self.textboxqr.setMaximumWidth(150)
        grid.addWidget(textqr, 1, 6)
        grid.addWidget(self.textboxqr, 2, 6)

        self.pixmap = QPixmap(200,200)
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        grid.addWidget(self.label, 0, 0, 5, 5)
        #grid.addItem(pixmap,1,0,4,4)

        btn = QPushButton('Generate', self)
        btn.setToolTip('Generate qr code from text')
        btn.clicked.connect(self.generate)
        grid.addWidget(btn,3,6)

        self.generate()

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Generate QRcodes')


        self.show()

    def generate(self):

        text = self.textboxqr.toPlainText()
        img = qrcode.make(text)
        self.qim = ImageQt(img)
        qim = self.qim.scaledToHeight(200)
        self.pixmap = QPixmap.fromImage(qim)
        import ipdb
        #ipdb.set_trace()
        self.label.setPixmap(self.pixmap)

    def resizeEvent(self, e):

        print(self.label.size())
        self.dx += e.size().width() - e.oldSize().width()
        self.dy += e.size().height() - e.oldSize().height()
        #dx, dy = [x2 - x1 for x1, x2 in zip(e.size()., e.oldSize())]
        print(f'dx : {self.dx}, dy : {self.dy}')

        qim = self.qim.scaledToHeight(self.label.size().height()-10)
        self.pixmap = QPixmap.fromImage(qim)
        self.label.setPixmap(self.pixmap)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
