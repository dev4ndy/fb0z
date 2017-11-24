#!/usr/bin/python

import time
from time import sleep
import serial


class Conexion:
    puerto_serie = None

    def __init__(self):
        hola=1
        #self.conectar()

    def conectar(self):
        self.puerto_serie = serial.Serial('/dev/ttyACM1',
                                          baudrate=9600,
                                          bytesize=serial.EIGHTBITS,
                                          parity=serial.PARITY_NONE,
                                          stopbits=serial.STOPBITS_ONE,
                                          timeout=1,
                                          xonxoff=0,
                                          rtscts=0
                                          )

    def close(self):
        return 1
        #self.puerto_serie.close()

    def lectura(self):
        #self.puerto_serie.setDTR(True)  # indica que el canal esta listo para comunicarse
        sleep(5)
        #lectura = self.puerto_serie.readline().strip()
        #print(time.strftime("%c"))
        #lectura = float(lectura.replace(',', '.'))
        return 25
