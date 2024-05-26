
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowFullScreen)
        self.setWindowModality(Qt.ApplicationModal)
        self.map_view = QWebEngineView(self)
        self.setCentralWidget(self.map_view)
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.back_to_main_window)
        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.map_view)
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.load_google_maps()
    def load_google_maps(self):
        # Reemplaza 'TU_CLAVE_DE_API' con tu propia clave de API de Google Maps
        api_key = 'AIzaSyDpzjZlUy9R6r4-l5ZMRajrRbvP8gEX_I8'
        latitude = 19.16018  # Reemplaza con la latitud deseada
        longitude = -100.13440  # Reemplaza con la longitud deseada

        html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps</title>
                <style>
                    html, body, #map {{
                        height: 100%;
                        margin: 0;
                        padding: 0;
                    }}
                </style>
            </head>
            <body>
                <div id="map"></div>
                <script src="https://maps.googleapis.com/maps/api/js?key={api_key}"></script>
                <script>
                    function initMap() {{
                        var center = {{ lat: {latitude}, lng: {longitude} }};
                        var map = new google.maps.Map(document.getElementById('map'), {{
                            center: center,
                            zoom: 14
                        }});
                    }}
                    initMap();
                </script>
            </body>
            </html>
        '''

        self.map_view.setHtml(html)
    def back_to_main_window(self):
        self.close()
