from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([]) # Forventer liste med argumenter

vindu = QWidget()
vindu.setWindowTitle("Hello World!")
vindu.resize(300, 250)
vindu.move(600, 300) # Begynner øverst i venstre hjørne (x, y)

vindu.show()
app.exec()