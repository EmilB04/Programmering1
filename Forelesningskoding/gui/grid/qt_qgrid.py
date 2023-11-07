import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class HovedVindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Test")
        self.setGeometry(200, 200, 600, 400)
        
        layout = QGridLayout()
        self.setLayout(layout)

        minLabel = QLabel()
        minLabel.setText("Dette er en label")
        layout.addWidget(minLabel, 0,0)
        
        minKnapp = QPushButton()
        minKnapp.setText("Dette er en knapp")
        layout.addWidget(minKnapp, 0,1)
        
        min_inputlinje = QLineEdit()
        min_inputlinje.setPlaceholderText("Enkel linke. Dette er standardtekst")
        layout.addWidget(min_inputlinje, 0,2)
        
        min_radioKnapp = QRadioButton("Dette er en radioknapp")
        layout.addWidget(min_radioKnapp, 1,0)
        
        min_checkboks = QCheckBox("Dette er en checkboks")
        layout.addWidget(min_checkboks, 1,1)
        
        min_combobox = QComboBox()
        min_combobox.addItems(["En", "To", "Tre"])
        min_combobox.insertItem(0, "Velg et alternativ")
        min_combobox.setCurrentIndex(0) # Velger hvor den skal starte
        layout.addWidget(min_combobox, 1,2)
        
        min_tekst = QTextEdit()
        min_tekst.setPlaceholderText("Dette er en tekstboks")
        layout.addWidget(min_tekst, 2,0)
        
        min_beskjed = QMessageBox()
        min_beskjed.setText("Dette er en beskjedboks til deg")
        layout.addWidget(min_beskjed, 2,1)
        min_beskjed.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel) # Hvis man vil ha to knapper. Ok vil alltid være der
        
        min_slider = QSlider(Qt.Orientation.Horizontal) # Kan også være Qt.Orientation.Vertical
        min_slider.setRange(0, 100)    # min og max verdi
        min_slider.setValue(50)
        layout.addWidget(min_slider, 2,2)
        
        
        
        
        self.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = HovedVindu()
    sys.exit(app.exec())
    