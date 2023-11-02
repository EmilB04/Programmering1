from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
import sys

class Vindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enkelt vindu") # tittel på "adresselinjen/tittelfeltet"
        self.resize(300, 300)

        label = QLabel()                    # Kaller på ekstern funksjon som lager en label
        label.setText("Hello World!")       # Teksten som skal vises på skjermen

        label_img = QLabel()
        pixmap = QPixmap("squarePants.jpg")
        label_img.setPixmap(pixmap) 

        layout = QVBoxLayout(label)
        self.setLayout(layout)
        layout.addWidget(label)
        layout.addWidget(label_img)

# Programmet starter her
app = QApplication(sys.argv) # ALLTID MED

vindu = Vindu()
vindu.show()

sys.exit(app.exec())    # ALLTID MED
class Vindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enkelt vindu") # tittel på "adresselinjen/tittelfeltet"
        self.resize(300, 300)

        label = QLabel()                    # Kaller på ekstern funksjon som lager en label
        label.setText("Hello World!")       # Teksten som skal vises på skjermen
        label.setStyleSheet("font-size: 40px;")
        label_img = QLabel()
        pixmap = QPixmap("squarePants.jpg")
        label_img.setPixmap(pixmap) 

        layout = QVBoxLayout(label)
        self.setLayout(layout)
        layout.addWidget(label)

# Programmet starter her
app = QApplication(sys.argv) # ALLTID MED

vindu = Vindu()
vindu.show()




sys.exit(app.exec())    # ALLTID MED