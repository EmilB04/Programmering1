import sys
from PyQt6.QtWidgets import *

class HovedVindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Knappbinding")
        self.setGeometry(200, 200, 600, 400)
        
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        knapp = QPushButton("Trykk her")
        knapp.clicked.connect(self.knapp_trykket) # Kobler den til funksjonen
        layout.addWidget(knapp)

        self.show()
        
    def knapp_trykket(self):
        print("Knappen ble trykket!")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    hovedvindu = HovedVindu()
    sys.exit(app.exec())
