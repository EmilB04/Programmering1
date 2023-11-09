import sys
import random as rd
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QFormLayout, QComboBox, QDoubleSpinBox, QPushButton, QLabel, QGridLayout, QWidget, QApplication
#---------------------------------------------#

PLANETER = ["Merkus", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
TYNGDEKRAFT = [3.7, 8.87, 9.807, 3.721, 23.79, 10.44, 8.87, 11.15]
PLANET_BILDER = ["bilder/sun.png", "bilder/merkur.png", "bilder/venus.png", "bilder/jorden.png", "bilder/mars.png", "bilder/jupiter.png", "bilder/saturn.png", "bilder/uranus.png", "bilder/neptun.png"]

class HovedVindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vekt på planeten")
        self.setGeometry(500, 150, 500, 400)
    
        windowIcon = QIcon("bilder/sun.png")
        self.setWindowIcon(windowIcon)
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.toppLabel = QLabel()
        self.toppLabel.setText("Vekt på planeten")
        self.toppLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #---------------------------------------------------------#
        self.skjema = QFormLayout()
        self.meny_comobox = QComboBox()
        self.meny_comobox.setPlaceholderText("Velg en planet")
        self.meny_comobox.addItem("Tilfeldig planet")
        
        for planet in PLANETER:
            self.meny_comobox.addItem(planet)
        self.meny_comobox.activated.connect(self.oppdater_bilde)
        self.skjema.addRow("Velg en planet:", self.meny_comobox)

        self.vekt_input = QDoubleSpinBox()
        self.vekt_input.setPrefix("Din vekt i kg:       ")
        self.vekt_input.setDecimals(1)
        self.skjema.addRow(self.vekt_input)
        
        self.regnUtKnapp = QPushButton("Regn ut")
        self.regnUtKnapp.clicked.connect(self.regn_ut)
        self.skjema.addRow(self.regnUtKnapp)
        
        self.bildeLabel = QLabel()
        self.pixmap = QPixmap("bilder/sun.png")
        self.pixmap = self.pixmap.scaledToWidth(300)
        self.bildeLabel.setPixmap(self.pixmap)
        
        self.bunnLabel = QLabel()
        self.bunnLabel.setText("Velg en planet og skriv inn vekten din")
        self.bunnLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        #--------
        self.layout.addWidget(self.toppLabel, 0, 0, 1, 2)
        self.layout.addLayout(self.skjema, 1, 0)
        self.layout.addWidget(self.bildeLabel, 1, 1)
        self.layout.addWidget(self.bunnLabel, 2, 0, 1, 2)
        
        #--------


        self.show()
        
    def oppdater_bilde(self):
        self.pixmap.load(PLANET_BILDER[self.meny_comobox.currentIndex()])
        self.pixmap = self.pixmap.scaledToWidth(300)
        self.bildeLabel.setPixmap(self.pixmap)
        
    def regn_ut(self):
        self.planetnummer = self.meny_comobox.currentIndex()
        if self.planetnummer == 0:
            self.planetnummer = rd.randint(0, len(PLANETER))
        
        self.ny_vekt = beregn_vekt(self.vekt_input.value(), TYNGDEKRAFT[self.planetnummer])
        
        self.bunnLabel.setText(f"Du fikk planeten {PLANETER[self.planetnummer]}, hvor din vekt er {self.ny_vekt} kg, med tyngekraft {TYNGDEKRAFT[self.planetnummer]} m/s^2")
        
def beregn_vekt(din_vekt, planettyngdekraft, jordens_tyngdekraft = 9.807):
    beregnet_vekt = din_vekt / jordens_tyngdekraft * planettyngdekraft
    return f"{beregnet_vekt:.2f}"


#---------------------------------------------#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = HovedVindu()
    vindu.show()
    sys.exit(app.exec())