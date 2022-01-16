from PyQt5.QtWidgets import QMessageBox


# Error message box because I don't like standard one XD
def error(dis):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(dis)
    msg.setWindowTitle("Error")
    msg.exec_()
