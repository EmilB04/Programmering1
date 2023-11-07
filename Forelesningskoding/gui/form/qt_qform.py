import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class HovedVindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oppmeldingsskjema")
        self.setGeometry(200, 200, 600, 400)
        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow("Fornavn:", QLineEdit(self))
        layout.addRow("Etternavn:", QLineEdit(self))
        layout.addRow("E-post:", QLineEdit(self))
        layout.addRow("Passord:", QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow("Bekreft passord:", QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        
        layout.addRow(QPushButton("Registrer"))
        
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    hovedvindu = HovedVindu()
    sys.exit(app.exec())
