import sys
import time
import serial
import struct
import threading
import numpy as np
from time import sleep
import csv


class Data():
    def __init__(self, port):
        self.tempData = 0
        self.readout = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.packet_number_array = []
        self.pressure_array = []
        self.height_array = []
        self.speed_array = []
        self.temperature_array = []
        self.pitch_array = []
        self.roll_array = []
        self.yaw_array = []
        self.voltage_array = []
        self.gps_lat_array = []
        self.gps_long_array = []

        try:
            self.sp = serial.Serial(port, 115200)
            self.bufferLock = threading.Lock()

            thread = threading.Thread(target=self.updateThread, args=())
            thread.daemon = True
            thread.start()

        except ValueError as e:
            print("Serial port error ...")
            return None

    def ayrilKomut(self):
        self.sp.write('a'.encode())
        print('Ayrilma basildi')

    def videoPaketGuncellemeKomut(self):
        self.sp.write('e'.encode())
        print('VPG')

    def motorStart(self):
        self.sp.write('mb'.encode())
        print('msa basildi')

    def motorStop(self):
        self.sp.write('md'.encode())
        print('mstp basildi')

    def updateThread(self):
        
        while True:
            while (self.sp.inWaiting() == 0):
                pass

            self.bufferLock.acquire()

            td = self.sp.readline().decode('UTF-8')[:-2]

            rbuf = td.split(',')
            with open('exports/TMUY2020_53413_TLM.csv', mode='a+', newline='', encoding='utf-8') as csvFile:
                writeData = csv.writer(
                    csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writeData.writerow(rbuf)
                
            # check
            team_number = int(rbuf[0])
            packet_number = int(rbuf[1])
            time_time = str(rbuf[2])
            pressure = int(rbuf[3])
            height = float(rbuf[4])
            speed = float(rbuf[5])
            temperature = float(rbuf[6])
            voltage = float(rbuf[7])
            gps_lat = float(rbuf[8])
            gps_long = float(rbuf[9])
            gps_alt = float(rbuf[10])
            satellite_state = str(rbuf[11])
            pitch = float(rbuf[12])
            roll = float(rbuf[13])
            yaw = float(rbuf[14])
            spinning_number = int(rbuf[15])
            video_state = str(rbuf[16])
            # pwm_bilgi = float(rbuf[17])


            self.readout = [team_number, packet_number, time_time, pressure, height, speed, temperature, voltage,
                            gps_lat, gps_long, gps_alt, satellite_state, pitch, roll, yaw, spinning_number, video_state]

            # append to graph buffers
            self.packet_number_array = np.append(
                self.packet_number_array, packet_number)
            self.pressure_array = np.append(self.pressure_array, pressure)
            self.height_array = np.append(self.height_array, height)
            self.speed_array = np.append(self.speed_array, speed)
            self.temperature_array = np.append(
                self.temperature_array, temperature)
            self.voltage_array = np.append(self.voltage_array, voltage)
            self.pitch_array = np.append(self.pitch_array, pitch)
            self.roll_array = np.append(self.roll_array, roll)
            self.yaw_array = np.append(self.yaw_array, yaw)
            self.gps_lat_array = np.append(self.gps_lat_array, gps_lat)
            self.gps_long_array = np.append(self.gps_long_array, gps_long)

        # unlock

            self.bufferLock.release()

    def getReadout(self):
        self.bufferLock.acquire()
        tmp = self.readout
        self.bufferLock.release()
        return tmp

    # -------------------------------------------------------------------------
    def getArrays(self):
        self.bufferLock.acquire()
        tmp = [self.packet_number_array, self.pressure_array, self.height_array, self.speed_array,
               self.temperature_array, self.pitch_array, self.roll_array, self.yaw_array, self.voltage_array, self.gps_lat_array, self.gps_long_array]
        self.bufferLock.release()
        return tmp


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("What is serial port?")
        sys.exit(0)

    print("Serial port: " + sys.argv[1])
    dt = Data(sys.argv[1])

    tempDatum = 0

    while True:
        time.sleep(1)
        print(dt.getReadout()[1])
        tempDatum = dt.getReadout()[1]
