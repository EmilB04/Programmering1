import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class HovedVindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVBoxLayout Test")
        self.resize(300, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        button1 = QPushButton("TRYKK HER") # Metode 1
        button2 = QPushButton()            # Metode 2
        button2.setText("TRYKK HER OGSÅ")  # Metode 2
        button3 = QPushButton("IKKE TRYKK HER")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)


        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = HovedVindu()
    sys.exit(app.exec())