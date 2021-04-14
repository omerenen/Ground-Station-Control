# arayüz
from gui import Ui_mainForm as gui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

# plotting
from data import Data
import pyqtgraph as pg
from pyqtgraph.ptime import time

# veri kaydı
import csv

# otomatik serial port
import glob
import serial

# file dialog
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import shutil

#other
from time import sleep
import sys
import os
import math
import threading

#3d sim
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
from stl import mesh



# ----------------------------------------------------------------------------------------------------------------------
# Otomatik serial port seçme
# ----------------------------------------------------------------------------------------------------------------------


def serialPortFunc():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

# ----------------------------------------------------------------------------------------------------------------------


class main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.MyUI()
        self.root = Tk()
        self.root.withdraw()

        self.isAlive = True

        self.angleDiffPitch = 0
        self.angleDiffRoll = 0
        self.angleDiffYaw = 0

        self.tempDataForPacketNumber = 0

        # gui.py
        self.gui = gui()
        self.gui.setupUi(self)
        self.msg = self.gui.msg

        self.m1 = mesh.Mesh.from_file('assets/uydu.stl')

        self.plottingThread = threading.Thread(
            target=self.pltAndSimFunc, args=())
        self.plottingThread.daemon = True

        # start button
        self.gui.baslatButton.clicked.connect(self.startGcs)

        # stop button
        self.gui.durdurButton.clicked.connect(self.stopGcs)

        # video secme
        self.gui.secButton.clicked.connect(self.chooseFunc)

        # ayrilma
        self.gui.ayrilButton.clicked.connect(self.ayrilFunc)

        # video gönderme
        self.gui.gonderButton.clicked.connect(self.sendFileThread)

        # motor tahrik
        self.gui.tahrikButton.clicked.connect(self.tahrikFunc)

        # motor tahrik stop
        self.gui.tahrikButtonStop.clicked.connect(self.tahrikFuncStop)

    def ayrilFunc(self):
        dt.ayrilKomut()

    def tahrikFunc(self):
        dt.motorStart()

    def tahrikFuncStop(self):
        dt.motorStop()

    def startGcs(self):

        if(self.isAlive == False):
            self.isAlive = True

        elif(self.isAlive == True):
            self.plottingThread.start()

    def stopGcs(self):
        self.isAlive = False

    def checkRaspFunc(self):
        raspState = os.popen('net view').read()

        if 'RASPBERRYPI' in raspState:
            self.gui.raspBilgi.setText(str('Evet'))
        else:
            self.gui.raspBilgi.setText(str('Hayır'))

    def chooseFunc(self):
        fileName = askopenfile(mode='r')
        self.gui.lineEdit.setText(str(fileName.name))
        self.gui.gonderButton.setEnabled(True)

        self.DIRECTORY = self.gui.lineEdit.text()
        self.TARGET_DIRECTORY = r"Z:/"
        self.BASE_NAME = os.path.basename(self.DIRECTORY)

    def sendFile(self):
        shutil.copy(self.DIRECTORY, self.TARGET_DIRECTORY+self.BASE_NAME)

        if(os.path.exists(self.TARGET_DIRECTORY+self.BASE_NAME)):
            self.msg.setWindowTitle('İşlem Tamamlandı')
            self.msg.setText('Dosya gönderimi başarıyla tamamlandı')
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            x = self.msg.exec_()
            dt.videoPaketGuncellemeKomut()

    def sendFileThread(self):
        sendThread = threading.Thread(target=self.sendFile())
        sendThread.start()

    # kapat butonuna basıldığında while döngüsünde çık
    def closeEvent(self, event):
        self.isAlive = False

    def pltAndSimFunc(self):

        while True:

            if(self.isAlive):

                while self.isAlive:

                    # ----------------------------------------------------------------------------------------------------------------------------
                    # COLLECT DATA
                    # ----------------------------------------------------------------------------------------------------------------------------
                    packet_number = dt.getReadout()[1]

                    if(packet_number == self.tempDataForPacketNumber):
                        continue
                    # ----------------------------------------------------------------------------------------------------------------------------

                    # ----------------------------------------------------------------------------------------------------------------------------
                    # SET DATA TO LABEL
                    # ----------------------------------------------------------------------------------------------------------------------------
                    self.gui.packetNo.setText(str(dt.getReadout()[1]))
                    self.gui.saatBilgi.setText(str(dt.getReadout()[2]))
                    self.gui.basincBilgi.setText(str(dt.getReadout()[3]))
                    self.gui.yukseklikBilgi.setText(str(dt.getReadout()[4]))
                    self.gui.hizBilgi.setText(str(dt.getReadout()[5]))
                    self.gui.sicaklikBilgi.setText(str(dt.getReadout()[6]))
                    self.gui.gerilimBilgi.setText(str(dt.getReadout()[7]))
                    self.gui.uyduBilgi.setText(str(dt.getReadout()[11]))
                    self.gui.pitchBilgi.setText(
                        str(dt.getReadout()[12])+'/'+str(dt.getReadout()[13])+'/'+str(dt.getReadout()[14]))  # bak
                    self.gui.donusBilgi.setText(str(dt.getReadout()[15]))
                    self.gui.videoBilgi.setText(str(dt.getReadout()[16]))
                    self.gui.boylamBilgi.setText(str(dt.getReadout()[9]))
                    self.gui.enlemBilgi.setText(str(dt.getReadout()[8]))
                    self.gui.yukseklikGPSBilgi.setText(
                        str(dt.getReadout()[10]))
                    # self.gui.pwmBilgi.setText(str(dt.getReadout()[17]))

                    # ----------------------------------------------------------------------------------------------------------------------------

                    # ----------------------------------------------------------------------------------------------------------------------------
                    # PLOT DATA
                    # ----------------------------------------------------------------------------------------------------------------------------

                    self.gui.yukseklikGraphCurve.setData(
                        dt.getArrays()[0], dt.getArrays()[2])
                    self.gui.sicaklikGraphCurve.setData(
                        dt.getArrays()[0], dt.getArrays()[4])
                    self.gui.hizGraphCurve.setData(
                        dt.getArrays()[0], dt.getArrays()[3])
                    self.gui.basincGraphCurve.setData(
                        dt.getArrays()[0], dt.getArrays()[1])
                    self.gui.gerilimGraphCurve.setData(
                        dt.getArrays()[0], dt.getArrays()[8])
                    self.gui.gpsGraphCurve.setData(
                        dt.getArrays()[10], dt.getArrays()[9])
                    # ----------------------------------------------------------------------------------------------------------------------------
                    # ----------------------------------------------------------------------------------------------------------------------------
                    # ROTATION FUNCTION
                    # ----------------------------------------------------------------------------------------------------------------------------

                    self.angleDiffPitch = (
                        dt.getArrays()[5][-1]-dt.getArrays()[5][-2])
                    self.angleDiffRoll = (
                        dt.getArrays()[6][-1]-dt.getArrays()[6][-2])
                    self.angleDiffYaw = (
                        dt.getArrays()[7][-1]-dt.getArrays()[7][-2])

                    # print(
                    #     f"{self.angleDiffPitch} {self.angleDiffRoll} {self.angleDiffYaw}")

                    if (((self.angleDiffPitch and self.angleDiffRoll) > 80) and (self.angleDiffPitch and self.angleDiffRoll ) < -80):
                        pass

                    else:
                        self.m1.rotate([1, 0, 0], math.radians(
                            self.angleDiffPitch))
                        self.m1.rotate([0, 1, 0], math.radians(
                            self.angleDiffRoll))
                        # self.m1.rotate([0, 0, 1], math.radians(
                        #     self.angleDiffYaw))

                    self.canvas.ax6.add_collection3d(
                        mplot3d.art3d.Poly3DCollection(self.m1.vectors, edgecolor='k'))
                    self.canvas.ax6.auto_scale_xyz(
                        [-135, 135], [-135, 135], [-135, 135])
                    self.canvas.draw()

                    self.canvas.ax6.clear()

                    self.canvas.ax6.grid(False)
                    self.canvas.ax6.set_axis_off()

                    self.tempDataForPacketNumber = packet_number
                    # sleep(0.354)
            else:
                continue
            sleep(.8)

        # ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
# 3D SIMULASYON AXIS
# ----------------------------------------------------------------------------------------------------------------------------

    def MyUI(self):
        self.canvas = Canvas(self, width=7, height=1)
        self.canvas.move(1010, 530)


class Canvas(FigureCanvas, FuncAnimation):
    def __init__(self, parent=None, width=0, height=0, dpi=55):
        self.fig = Figure(figsize=(8, 7.5), dpi=57)
        self.fig.patch.set_facecolor('#efefef')
        self.fig.patch.set_alpha(0)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.ax6 = self.figure.add_subplot(111, projection='3d')
        self.ax6.get_xaxis().set_visible(False)
        self.ax6.set_facecolor('#efefef')

        self.ax6.grid(False)
        self.ax6.set_axis_off()

# ----------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------------
# ÇALIŞTIRMA
# ----------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)

    if len(serialPortFunc()) == 0:
        print('port bulunamadı')
    else:
        print(f"{serialPortFunc()[0]} portunda çalışıyor")
        dt = Data(serialPortFunc()[0])
        sleep(1)
        if(dt.getReadout()[1] == 0):
            print('Telemetri paketi alınamadı')
        else:
            running = main()
            running.show()
            sys.exit(app.exec_())

# ----------------------------------------------------------------------------------------------------------------------------
