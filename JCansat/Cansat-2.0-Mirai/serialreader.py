import serial
from PyQt5.QtCore import QThread, pyqtSignal
from serial.tools import list_ports


class SerialReaderThread(QThread):
    dataReceived = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_port = None
        self.running = False

    def run(self):
        try:
            self.serial_port = serial.Serial(self.port, int(self.baudrate), timeout=1)
            self.running = True

            while self.running:
                data = self.serial_port.readline().decode().strip()
                self.dataReceived.emit(data)
        except serial.SerialException as e:
            self.stop()
            self.dataReceived.emit("")  # Emit an empty string to indicate an error occurred

    def stop(self):
        self.running = False
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
