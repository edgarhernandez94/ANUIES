import serial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SerialReaderThread(QThread):
    dataReceived = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_port = None
        self.running = False
        self.first_newline_detected = False

    def run(self):
        try:
            self.serial_port = serial.Serial(self.port, self.baudrate)
            self.running = True
            while self.running:
                if self.serial_port.in_waiting:
                    data = self.serial_port.readline().decode().strip()
                    
                    # Si es la primera vez que detectamos un salto de línea
                    if not self.first_newline_detected:
                        self.first_newline_detected = True
                        continue
                    
                    self.dataReceived.emit(data)
        except serial.SerialException:
            pass
        finally:
            if self.serial_port and self.serial_port.is_open:
                self.serial_port.close()

    def stop(self):
        self.running = False
