"""Kerangka dashboard. Nanti diganti halaman operator dan verifikator."""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class DashboardPage(QWidget):
    def __init__(self, username, role, on_logout):
        super().__init__()
        self.setStyleSheet("background-color: #090d16; color: #f8fafc;")
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        judul = "Operator Portal" if role == "operator" else "Verificator Portal"
        lbl = QLabel(f"{judul}\nSelamat datang, {username}")
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("font-size: 22px; font-weight: bold; color: #38bdf8;")

        btn = QPushButton("Logout")
        btn.setFixedWidth(160)
        btn.clicked.connect(on_logout)

        layout.addWidget(lbl)
        layout.addWidget(btn, alignment=Qt.AlignCenter)