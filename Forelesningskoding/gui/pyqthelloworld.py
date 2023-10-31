from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv) # ALLTID MED

vindu = QWidget()
vindu.setWindowTitle("Hello World!")
vindu.resize(300, 250)
vindu.move(600, 300) # Begynner øverst i venstre hjørne (x, y)

vindu.show()


sys.exit(app.exec())    # ALLTID MED