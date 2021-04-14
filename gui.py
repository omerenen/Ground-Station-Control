from pyqtgraph import PlotWidget, PlotCurveItem
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import os

from matplotlib.figure import Figure
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from stl import mesh
import math


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(f'exports/canligoruntu.avi',
                              fourcc, 20.0, (640, 480))

        while True:
            ret, cv_img = cap.read()
            out.write(cv_img)
            if ret:
                self.change_pixmap_signal.emit(cv_img)


class Ui_mainForm(Figure):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(1920, 1080)
        mainForm.setStyleSheet("background-color: #efefef")
        self.msg = QtWidgets.QMessageBox()
        self.label = QtWidgets.QLabel(mainForm)
        self.label.setGeometry(QtCore.QRect(780, 30, 361, 171))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./assets/apis.png"))
        self.label.setObjectName("label")
        self.packetLabel = QtWidgets.QLabel(mainForm)
        self.packetLabel.setGeometry(QtCore.QRect(70, 50, 120, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.packetLabel.setFont(font)
        self.packetLabel.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(0, 0, 0);")
        self.packetLabel.setObjectName("packetLabel")
        self.packetNo = QtWidgets.QLabel(mainForm)
        self.packetNo.setGeometry(QtCore.QRect(70, 60, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(26)
        self.packetNo.setFont(font)
        self.packetNo.setStyleSheet("background-color: transparent;\n"
                                    "color: rgb(0, 0, 0);")
        self.packetNo.setObjectName("packetNo")
        self.saatLabel = QtWidgets.QLabel(mainForm)
        self.saatLabel.setGeometry(QtCore.QRect(250, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.saatLabel.setFont(font)
        self.saatLabel.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(0, 0, 0);")
        self.saatLabel.setObjectName("saatLabel")
        self.saatBilgi = QtWidgets.QLabel(mainForm)
        self.saatBilgi.setGeometry(QtCore.QRect(250, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        self.saatBilgi.setFont(font)
        self.saatBilgi.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(0, 0, 0);")
        self.saatBilgi.setObjectName("saatBilgi")
        self.sicaklikLabel = QtWidgets.QLabel(mainForm)
        self.sicaklikLabel.setGeometry(QtCore.QRect(440, 50, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.sicaklikLabel.setFont(font)
        self.sicaklikLabel.setStyleSheet("background-color: transparent;\n"
                                         "color: rgb(0, 0, 0);")
        self.sicaklikLabel.setObjectName("sicaklikLabel")
        self.sicaklikBilgi = QtWidgets.QLabel(mainForm)
        self.sicaklikBilgi.setGeometry(QtCore.QRect(440, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(26)
        self.sicaklikBilgi.setFont(font)
        self.sicaklikBilgi.setStyleSheet("background-color: transparent;\n"
                                         "color: rgb(0, 0, 0);")
        self.sicaklikBilgi.setObjectName("sicaklikBilgi")
        self.basincLabel = QtWidgets.QLabel(mainForm)
        self.basincLabel.setGeometry(QtCore.QRect(600, 50, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.basincLabel.setFont(font)
        self.basincLabel.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(0, 0, 0);")
        self.basincLabel.setObjectName("basincLabel")
        self.basincBilgi = QtWidgets.QLabel(mainForm)
        self.basincBilgi.setGeometry(QtCore.QRect(600, 60, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(26)
        self.basincBilgi.setFont(font)
        self.basincBilgi.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(0, 0, 0);")
        self.basincBilgi.setObjectName("basincBilgi")
        self.yukseklikBilgi = QtWidgets.QLabel(mainForm)
        self.yukseklikBilgi.setGeometry(QtCore.QRect(600, 130, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(26)
        self.yukseklikBilgi.setFont(font)
        self.yukseklikBilgi.setStyleSheet("background-color: transparent;\n"
                                          "color: rgb(0, 0, 0);")
        self.yukseklikBilgi.setObjectName("yukseklikBilgi")
        self.hizLabel = QtWidgets.QLabel(mainForm)
        self.hizLabel.setGeometry(QtCore.QRect(70, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.hizLabel.setFont(font)
        self.hizLabel.setStyleSheet("background-color: transparent;\n"
                                    "color: rgb(0, 0, 0);")
        self.hizLabel.setObjectName("hizLabel")
        self.hizBilgi = QtWidgets.QLabel(mainForm)
        self.hizBilgi.setGeometry(QtCore.QRect(70, 130, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(26)
        self.hizBilgi.setFont(font)
        self.hizBilgi.setStyleSheet("background-color: transparent;\n"
                                    "color: rgb(0, 0, 0);")
        self.hizBilgi.setObjectName("hizBilgi")
        self.yukselikLabel = QtWidgets.QLabel(mainForm)
        self.yukselikLabel.setGeometry(QtCore.QRect(600, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.yukselikLabel.setFont(font)
        self.yukselikLabel.setStyleSheet("background-color: transparent;\n"
                                         "color: rgb(0, 0, 0);")
        self.yukselikLabel.setObjectName("yukselikLabel")
        self.donusBilgi = QtWidgets.QLabel(mainForm)
        self.donusBilgi.setGeometry(QtCore.QRect(440, 130, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(26)
        self.donusBilgi.setFont(font)
        self.donusBilgi.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.donusBilgi.setObjectName("donusBilgi")
        self.donusLabel = QtWidgets.QLabel(mainForm)
        self.donusLabel.setGeometry(QtCore.QRect(440, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.donusLabel.setFont(font)
        self.donusLabel.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.donusLabel.setObjectName("donusLabel")
        self.gerilimLabel = QtWidgets.QLabel(mainForm)
        self.gerilimLabel.setGeometry(QtCore.QRect(250, 120, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.gerilimLabel.setFont(font)
        self.gerilimLabel.setStyleSheet("background-color: transparent;\n"
                                        "color: rgb(0, 0, 0);")
        self.gerilimLabel.setObjectName("gerilimLabel")
        self.gerilimBilgi = QtWidgets.QLabel(mainForm)
        self.gerilimBilgi.setGeometry(QtCore.QRect(250, 130, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(26)
        self.gerilimBilgi.setFont(font)
        self.gerilimBilgi.setStyleSheet("background-color: transparent;\n"
                                        "color: rgb(0, 0, 0);")
        self.gerilimBilgi.setObjectName("gerilimBilgi")
        self.enlemLabel = QtWidgets.QLabel(mainForm)
        self.enlemLabel.setGeometry(QtCore.QRect(1360, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.enlemLabel.setFont(font)
        self.enlemLabel.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.enlemLabel.setObjectName("enlemLabel")
        self.pitchLabel = QtWidgets.QLabel(mainForm)
        self.pitchLabel.setGeometry(QtCore.QRect(1170, 120, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.pitchLabel.setFont(font)
        self.pitchLabel.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.pitchLabel.setObjectName("pitchLabel")
        self.enlemBilgi = QtWidgets.QLabel(mainForm)
        self.enlemBilgi.setGeometry(QtCore.QRect(1360, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(18)
        self.enlemBilgi.setFont(font)
        self.enlemBilgi.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.enlemBilgi.setObjectName("enlemBilgi")
        ##--------------
        
        # self.pwmLabel = QtWidgets.QLabel(mainForm)
        # self.pwmLabel.setGeometry(QtCore.QRect(1440, 120, 121, 16))
        # font = QtGui.QFont()
        # font.setFamily("Gilroy-Medium")
        # self.pwmLabel.setFont(font)
        # self.pwmLabel.setStyleSheet("background-color: transparent;\n"
        #                               "color: rgb(0, 0, 0);")
        # self.pwmLabel.setObjectName("pwmLabel")
        # self.pwmBilgi = QtWidgets.QLabel(mainForm)
        # self.pwmBilgi.setGeometry(QtCore.QRect(1440, 130, 131, 41))
        # font = QtGui.QFont()
        # font.setFamily("Gilroy-Bold")
        # font.setPointSize(18)
        # self.pwmBilgi.setFont(font)
        # self.pwmBilgi.setStyleSheet("background-color: transparent;\n"
        #                               "color: rgb(0, 0, 0);")
        # self.pwmBilgi.setObjectName("pwmBilgi")
        ##--------------

        self.pitchBilgi = QtWidgets.QLabel(mainForm)
        self.pitchBilgi.setGeometry(QtCore.QRect(1170, 130, 320, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(20)
        self.pitchBilgi.setFont(font)
        self.pitchBilgi.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.pitchBilgi.setObjectName("pitchBilgi")
        self.boylamLabel = QtWidgets.QLabel(mainForm)
        self.boylamLabel.setGeometry(QtCore.QRect(1550, 50, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.boylamLabel.setFont(font)
        self.boylamLabel.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(0, 0, 0);")
        self.boylamLabel.setObjectName("boylamLabel")
        self.boylamBilgi = QtWidgets.QLabel(mainForm)
        self.boylamBilgi.setGeometry(QtCore.QRect(1550, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(18)
        self.boylamBilgi.setFont(font)
        self.boylamBilgi.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(0, 0, 0);")
        self.boylamBilgi.setObjectName("boylamBilgi")
        self.yukseklikGPSLabel = QtWidgets.QLabel(mainForm)
        self.yukseklikGPSLabel.setGeometry(QtCore.QRect(1750, 50, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.yukseklikGPSLabel.setFont(font)
        self.yukseklikGPSLabel.setStyleSheet("background-color: transparent;\n"
                                             "color: rgb(0, 0, 0);")
        self.yukseklikGPSLabel.setObjectName("yukseklikGPSLabel")
        self.yukseklikGPSBilgi = QtWidgets.QLabel(mainForm)
        self.yukseklikGPSBilgi.setGeometry(QtCore.QRect(1750, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(18)
        self.yukseklikGPSBilgi.setFont(font)
        self.yukseklikGPSBilgi.setStyleSheet("background-color: transparent;\n"
                                             "color: rgb(0, 0, 0);")
        self.yukseklikGPSBilgi.setObjectName("yukseklikGPSBilgi")
        self.uyduBilgi = QtWidgets.QLabel(mainForm)
        self.uyduBilgi.setGeometry(QtCore.QRect(1550, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(20)
        self.uyduBilgi.setFont(font)
        self.uyduBilgi.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(0, 0, 0);")
        self.uyduBilgi.setObjectName("uyduBilgi")
        self.uyduLabel = QtWidgets.QLabel(mainForm)
        self.uyduLabel.setGeometry(QtCore.QRect(1550, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.uyduLabel.setFont(font)
        self.uyduLabel.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(0, 0, 0);")
        self.uyduLabel.setObjectName("uyduLabel")
        self.videoBilgi = QtWidgets.QLabel(mainForm)
        self.videoBilgi.setGeometry(QtCore.QRect(1750, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(20)
        self.videoBilgi.setFont(font)
        self.videoBilgi.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.videoBilgi.setObjectName("videoBilgi")
        self.videoLabel = QtWidgets.QLabel(mainForm)
        self.videoLabel.setGeometry(QtCore.QRect(1750, 120, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.videoLabel.setFont(font)
        self.videoLabel.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(0, 0, 0);")
        self.videoLabel.setObjectName("videoLabel")
        self.ayrilButton = QtWidgets.QPushButton(mainForm)
        self.ayrilButton.setGeometry(QtCore.QRect(1170, 50, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ayrilButton.setFont(font)
        self.ayrilButton.setStyleSheet("QPushButton#ayrilButton\n"
                                       "{\n"
                                       "background-color: transparent;\n"
                                       "border-top-color: rgb(0, 0, 0);\n"
                                       "font: 11pt \"Gilroy-Medium\";\n"
                                       "border: 1px solid black;\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "}\n"
                                       "QPushButton#ayrilButton:pressed\n"
                                       "{\n"
                                       "  background-color:black;\n"
                                       "color:white;\n"
                                       "}")
        self.ayrilButton.setObjectName("ayrilButton")
#---
        self.tahrikButton = QtWidgets.QPushButton(mainForm)
        self.tahrikButton.setGeometry(QtCore.QRect(1530, 970, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tahrikButton.setFont(font)
        self.tahrikButton.setStyleSheet("QPushButton#tahrikButton\n"
                                        "{\n"
                                        "background-color: transparent;\n"
                                        "border-top-color: rgb(0, 0, 0);\n"
                                        "font: 11pt \"Gilroy-Medium\";\n"
                                        "border: 1px solid black;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton#tahrikButton:pressed\n"
                                        "{\n"
                                        "  background-color:black;\n"
                                        "color:white;\n"
                                        "}")
        self.tahrikButton.setObjectName("tahrikButton")
#---
        self.baslatButton = QtWidgets.QPushButton(mainForm)
        self.baslatButton.setGeometry(QtCore.QRect(90, 970, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.baslatButton.setFont(font)
        self.baslatButton.setStyleSheet("QPushButton#baslatButton\n"
                                        "{\n"
                                        "background-color: transparent;\n"
                                        "border-top-color: rgb(0, 0, 0);\n"
                                        "font: 11pt \"Gilroy-Medium\";\n"
                                        "border: 1px solid black;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton#baslatButton:pressed\n"
                                        "{\n"
                                        "  background-color:black;\n"
                                        "color:white;\n"
                                        "}")
        self.baslatButton.setObjectName("baslatButton")
#---
        self.durdurButton = QtWidgets.QPushButton(mainForm)
        self.durdurButton.setGeometry(QtCore.QRect(300, 970, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.durdurButton.setFont(font)
        self.durdurButton.setStyleSheet("QPushButton#durdurButton\n"
                                        "{\n"
                                        "background-color: transparent;\n"
                                        "border-top-color: rgb(0, 0, 0);\n"
                                        "font: 11pt \"Gilroy-Medium\";\n"
                                        "border: 1px solid black;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton#durdurButton:pressed\n"
                                        "{\n"
                                        "  background-color:black;\n"
                                        "color:white;\n"
                                        "}")
        self.durdurButton.setObjectName("durdurButton")
#---
        self.tahrikButtonStop = QtWidgets.QPushButton(mainForm)
        self.tahrikButtonStop.setGeometry(QtCore.QRect(1720, 970, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tahrikButtonStop.setFont(font)
        self.tahrikButtonStop.setStyleSheet("QPushButton#tahrikButtonStop\n"
                                        "{\n"
                                        "background-color: transparent;\n"
                                        "border-top-color: rgb(0, 0, 0);\n"
                                        "font: 11pt \"Gilroy-Medium\";\n"
                                        "border: 1px solid black;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton#tahrikButtonStop:pressed\n"
                                        "{\n"
                                        "  background-color:black;\n"
                                        "color:white;\n"
                                        "}")
        self.tahrikButtonStop.setObjectName("tahrikButtonStop")
#---
        self.raspBilgi = QtWidgets.QLabel(mainForm)
        self.raspBilgi.setGeometry(QtCore.QRect(90, 970, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(20)
        self.raspBilgi.setFont(font)
        self.raspBilgi.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(0, 0, 0);")
        self.raspBilgi.setObjectName("raspBilgi")
        self.raspLabel = QtWidgets.QLabel(mainForm)
        self.raspLabel.setGeometry(QtCore.QRect(90, 960, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        self.raspLabel.setFont(font)
        self.raspLabel.setStyleSheet("background-color: transparent;\n"
                                     "color: rgb(0, 0, 0);")
        self.raspLabel.setObjectName("raspLabel")
        self.pitchLabel_2 = QtWidgets.QLabel(mainForm)
        self.pitchLabel_2.setGeometry(QtCore.QRect(900, 180, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(9)
        self.pitchLabel_2.setFont(font)
        self.pitchLabel_2.setStyleSheet("background-color: transparent;\n"
                                        "color: rgb(0, 0, 0);")
        self.pitchLabel_2.setObjectName("pitchLabel_2")
        # --------------------------------------------------------------------------------------------------------------------
        # alt kisim
        # --------------------------------------------------------------------------------------------------------------------
        self.gonderButton = QtWidgets.QPushButton(mainForm)
        self.gonderButton.setGeometry(QtCore.QRect(1278, 970, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gonderButton.setFont(font)
        self.gonderButton.setStyleSheet("QPushButton#gonderButton\n"
                                        "{\n"
                                        "background-color: transparent;\n"
                                        "border-top-color: rgb(0, 0, 0);\n"
                                        "font: 11pt \"Gilroy-Medium\";\n"
                                        "border: 1px solid black;\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton#gonderButton:pressed\n"
                                        "{\n"
                                        "  background-color:black;\n"
                                        "color:white;\n"
                                        "}")
        self.gonderButton.setObjectName("gonderButton")
        self.gonderButton.setEnabled(False)
        self.secButton = QtWidgets.QPushButton(mainForm)
        self.secButton.setGeometry(QtCore.QRect(1080, 970, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.secButton.setFont(font)
        self.secButton.setStyleSheet("QPushButton#secButton\n"
                                     "{\n"
                                     "background-color: transparent;\n"
                                     "border-top-color: rgb(0, 0, 0);\n"
                                     "font: 11pt \"Gilroy-Medium\";\n"
                                     "border: 1px solid black;\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "}\n"
                                     "QPushButton#secButton:pressed\n"
                                     "{\n"
                                     "  background-color:black;\n"
                                     "color:white;\n"
                                     "}")
        self.secButton.setObjectName("secButton")
        self.lineEdit = QtWidgets.QLineEdit(mainForm)
        self.lineEdit.setGeometry(QtCore.QRect(570, 970, 470, 41))
        self.lineEdit.setStyleSheet(
            "background-color:transparent;color:rgb(0, 0, 0)")
        self.lineEdit.setReadOnly(True)
        self.videoBaslik = QtWidgets.QLabel(mainForm)
        self.videoBaslik.setGeometry(QtCore.QRect(565, 930, 880, 30))
        self.videoBaslik.setStyleSheet("background-color: transparent;")
        self.videoBaslik.setText("")
        self.videoBaslik.setPixmap(QtGui.QPixmap("./assets/video_section.png"))
        self.videoBaslik.setObjectName("videoBaslik")
        # --------------------------------------------------------------------------------------------------------------------
        self.basincGraph = PlotWidget(mainForm)
        self.basincGraph.setGeometry(QtCore.QRect(60, 250, 421, 291))
        self.basincGraph.setStyleSheet("background-color: transparent;")
        self.basincGraph.setBackground(None)
        self.basincGraph.setObjectName("basincGraph")
        self.basincGraph.setTitle('Basınç (Pascal)', **{'color': '#000'})
        self.basincGraphCurve = PlotCurveItem(pen=pg.mkPen('#000', width=1))
        self.basincGraph.addItem(self.basincGraphCurve)

        self.yukselikGraph = PlotWidget(mainForm)
        self.yukselikGraph.setGeometry(QtCore.QRect(510, 250, 471, 291))
        self.yukselikGraph.setStyleSheet("background-color: transparent;")
        self.yukselikGraph.setObjectName("yukselikGraph")
        self.yukselikGraph.setBackground(None)
        self.yukselikGraph.setTitle('Yükseklik (metre)', **{'color': '#000'})
        self.yukseklikGraphCurve = PlotCurveItem(
            pen=pg.mkPen('#000', width=1))  # set a color
        self.yukselikGraph.addItem(self.yukseklikGraphCurve)

        self.hizGraph = PlotWidget(mainForm)
        self.hizGraph.setGeometry(QtCore.QRect(1010, 250, 421, 291))
        self.hizGraph.setStyleSheet("background-color: transparent;")
        self.hizGraph.setObjectName("hizGraph")
        self.hizGraph.setBackground(None)
        self.hizGraph.setTitle('Hız (m/s)', **{'color': '#000'})
        self.hizGraphCurve = PlotCurveItem(pen=pg.mkPen('#000', width=1))
        self.hizGraph.addItem(self.hizGraphCurve)

        self.sicaklikGraph = PlotWidget(mainForm)
        self.sicaklikGraph.setGeometry(QtCore.QRect(1460, 250, 421, 291))
        self.sicaklikGraph.setStyleSheet("background-color: transparent;")
        self.sicaklikGraph.setObjectName("sicaklikGraph")
        self.sicaklikGraph.setBackground(None)
        self.sicaklikGraph.setTitle('Sıcaklık(°C)', **{'color': '#000'})
        self.sicaklikGraphCurve = PlotCurveItem(pen=pg.mkPen('#000', width=1))
        self.sicaklikGraph.addItem(self.sicaklikGraphCurve)

        self.gpsGraph = PlotWidget(mainForm)
        self.gpsGraph.setGeometry(QtCore.QRect(60, 590, 421, 291))
        self.gpsGraph.setStyleSheet("background-color: transparent;")
        self.gpsGraph.setObjectName("gpsGraph")
        self.gpsGraph.setBackground(None)
        self.gpsGraph.setTitle('GPS 2D (derece)', **{'color': '#000'})
        self.gpsGraphCurve = PlotCurveItem(pen=pg.mkPen('#000', width=1))
        self.gpsGraph.addItem(self.gpsGraphCurve)

        self.gerilimGraph = PlotWidget(mainForm)
        self.gerilimGraph.setGeometry(QtCore.QRect(1460, 590, 421, 291))
        self.gerilimGraph.setStyleSheet("background-color: transparent;")
        self.gerilimGraph.setObjectName("gerilimGraph")
        self.gerilimGraph.setBackground(None)
        self.gerilimGraph.setTitle('Gerilim (V)', **{'color': '#000'})
        self.gerilimGraphCurve = PlotCurveItem(pen=pg.mkPen('#000', width=1))
        self.gerilimGraph.addItem(self.gerilimGraphCurve)

        self.camera = QLabel(mainForm)
        self.camera.setGeometry(QtCore.QRect(575, 620, 471, 261))
        self.camera.setStyleSheet("background-color: transparent;")
        self.camera.setObjectName("camera")

        self.cameraLabel = QtWidgets.QLabel(mainForm)
        self.cameraLabel.setGeometry(QtCore.QRect(720, 585, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.cameraLabel.setFont(font)
        self.cameraLabel.setStyleSheet(
            "background-color: transparent;color: rgb(0, 0, 0);")

        # ----------------------------------------------------------------------------------
        self.tridi = QtWidgets.QLabel(mainForm)
        self.tridi.setGeometry(QtCore.QRect(1175, 585, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tridi.setFont(font)
        self.tridi.setStyleSheet(
            "background-color: transparent;color: rgb(0, 0, 0);")

        # ----------------------------------------------------------------------------------
        # canlı görüntü
        # ----------------------------------------------------------------------------------
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def update_image(self, cv_img):
        # self.camera değişkenini güncelleme
        qt_img = self.convert_cv_qt(cv_img)
        self.camera.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):

        # opencv görüntüsünü QPixmap'e çevirme
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
            rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(471, 291, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

        # ----------------------------------------------------------------------------------

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate(
            "mainForm", "ITU APIS ARGE | YER İSTASYONU"))
        self.packetLabel.setText(_translate("mainForm", "PAKET NUMARASI"))
        self.packetNo.setText(_translate("mainForm", "..."))
        self.saatLabel.setText(_translate("mainForm", "GÖNDERME SAATİ"))
        self.saatBilgi.setText(_translate("mainForm", "..."))
        self.sicaklikLabel.setText(_translate("mainForm", "SICAKLIK (°C)"))
        self.sicaklikBilgi.setText(_translate("mainForm", "..."))
        self.basincLabel.setText(_translate("mainForm", "BASINÇ (pascal)"))
        self.basincBilgi.setText(_translate("mainForm", "..."))
        self.yukseklikBilgi.setText(_translate("mainForm", "..."))
        self.cameraLabel.setText(_translate("mainForm", "Canlı Görüntü"))
        # self.pwmLabel.setText(_translate("mainForm", "PWM"))
        # self.pwmBilgi.setText(_translate("mainForm", "..."))

        self.hizLabel.setText(_translate("mainForm", "HIZ (m/s)"))
        self.hizBilgi.setText(_translate("mainForm", "..."))
        self.yukselikLabel.setText(_translate("mainForm", "YÜKSEKLİK (metre)"))
        self.donusBilgi.setText(_translate("mainForm", "..."))
        self.donusLabel.setText(_translate("mainForm", "DÖNÜŞ SAYISI"))
        self.gerilimLabel.setText(_translate("mainForm", "PİL GERİLİMİ (voltaj)"))
        self.gerilimBilgi.setText(_translate("mainForm", "..."))
        self.enlemLabel.setText(_translate("mainForm", "GPS ENLEM (derece)"))
        self.pitchLabel.setText(_translate("mainForm", "PITCH/ROLL/YAW (derece)"))
        self.enlemBilgi.setText(_translate("mainForm", "..."))
        self.pitchBilgi.setText(_translate("mainForm", ".../.../..."))
        self.boylamLabel.setText(_translate("mainForm", "GPS BOYLAM(derece)"))
        self.boylamBilgi.setText(_translate("mainForm", "..."))
        self.yukseklikGPSLabel.setText(_translate("mainForm", "GPS YÜKSEKLİK (metre)"))
        self.yukseklikGPSBilgi.setText(_translate("mainForm", "..."))
        self.uyduBilgi.setText(_translate("mainForm", "..."))
        self.uyduLabel.setText(_translate("mainForm", "UYDU STATÜSÜ"))
        self.videoBilgi.setText(_translate("mainForm", "..."))
        self.videoLabel.setText(_translate(
            "mainForm", "VİDEO AKTARIM BİLGİSİ"))
        self.raspBilgi.setText(_translate("mainForm", ""))
        self.raspLabel.setText(_translate(
            "mainForm", ""))
        self.ayrilButton.setText(_translate("mainForm", "AYRIL"))
        self.tahrikButton.setText(_translate("mainForm", "MOTOR BAŞLAT"))
        self.tahrikButtonStop.setText(_translate("mainForm", "MOTOR DURDUR"))
        self.baslatButton.setText(_translate("mainForm", "BASLA"))
        self.durdurButton.setText(_translate("mainForm", "DURDUR"))
        self.tridi.setText(_translate("mainForm", "3D Simulasyon"))

        self.gonderButton.setText(_translate("mainForm", "GÖNDER"))
        self.secButton.setText(_translate("mainForm", "DOSYA SEÇ"))

        self.pitchLabel_2.setText(_translate("mainForm", "TAKIM NO : 53413 "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./assets/ico.png'))
    mainForm = QtWidgets.QWidget()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())
