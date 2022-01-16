from PyQt5.QtCore import QDate, QTime


class Task():
    def __init__(self, date: QDate, time: QTime, name: str, dis: str):
        self.date = date
        self.time = time
        self.name = name
        self.dis = dis
