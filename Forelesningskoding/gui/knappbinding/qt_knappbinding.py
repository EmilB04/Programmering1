import sys
from PyQt6.QtWidgets import *

class HovedVindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Knappbinding")
        self.setGeometry(200, 200, 600, 400)
        
        
        
        
        self.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    hovedvindu = HovedVindu()
    sys.exit(app.exec())
