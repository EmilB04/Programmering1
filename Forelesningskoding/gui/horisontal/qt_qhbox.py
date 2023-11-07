import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout

class HovedVindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Test")

        layout = QHBoxLayout()
        self.setLayout(layout)
        self.setGeometry(200, 200, 300, 400)

        button1 = QPushButton("TRYKK HER") # Metode 1
        button2 = QPushButton()            # Metode 2
        button2.setText("TRYKK HER OGSÅ")  # Metode 2
        button3 = QPushButton("IKKE TRYKK HER")

        layout.addStretch(1)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addStretch(1)

        layout.setSpacing(20) # Luft mellom elementene
        layout.setContentsMargins(80,0,80,0) # Margin  rundt layouten

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = HovedVindu()
    sys.exit(app.exec())