from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowFullScreen)
        self.setWindowModality(Qt.ApplicationModal)
        
        # Definir las dimensiones de la ventana y la posición del widget del mapa
        screen_resolution = QDesktopWidget().screenGeometry()
        self.map_width = screen_resolution.width() - 100
        self.map_height = screen_resolution.height() - 100
        self.map_x = 50
        self.map_y = 50
        
        self.map_view = QWebEngineView(self)
        self.map_view.setGeometry(self.map_x, self.map_y, self.map_width, self.map_height)
        
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.back_to_main_window)
        
        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.map_view)
        
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.load_free_maps()
        
    def load_free_maps(self):
        # URL de la API de mapas gratuita (OpenStreetMap)
        url = 'https://www.openstreetmap.org/#map=10/19.16018/-100.13440'

        self.map_view.load(QUrl(url))
        
    def back_to_main_window(self):
        self.close()
