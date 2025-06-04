import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QTextEdit, QFileDialog, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from fpdf import FPDF
from shared.speech_live import LiveRecognizer

class VoiceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎙️ Smart Voice-to-Text App")
        self.setGeometry(300, 150, 700, 500)
        self.setStyleSheet("background-color: #f0f2f5;")

        self.status_label = QLabel("Status: Not recording")
        self.status_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.status_label.setStyleSheet("color: #333; margin: 10px;")

        self.textbox = QTextEdit()
        self.textbox.setFont(QFont("Consolas", 11))
        self.textbox.setReadOnly(True)
        self.textbox.setStyleSheet("""
            background-color: white;
            border: 1px solid #ccc;
            padding: 10px;
        """)

        self.start_btn = QPushButton("🎙️ Start Recording")
        self.stop_btn = QPushButton("⏹ Stop")
        self.export_txt_btn = QPushButton("📄 Export as TXT")
        self.export_pdf_btn = QPushButton("📄 Export as PDF")

        for btn in [self.start_btn, self.stop_btn, self.export_txt_btn, self.export_pdf_btn]:
            btn.setFixedHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 8px;
                    font-size: 14px;
                }
                QPushButton:disabled {
                    background-color: #9E9E9E;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)

        self.stop_btn.setEnabled(False)

        self.start_btn.clicked.connect(self.start_recording)
        self.stop_btn.clicked.connect(self.stop_recording)
        self.export_txt_btn.clicked.connect(self.export_txt)
        self.export_pdf_btn.clicked.connect(self.export_pdf)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)

        export_layout = QHBoxLayout()
        export_layout.addWidget(self.export_txt_btn)
        export_layout.addWidget(self.export_pdf_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.textbox)
        layout.addLayout(btn_layout)
        layout.addLayout(export_layout)

        self.setLayout(layout)

        self.recognizer = LiveRecognizer(callback=self.update_textbox)

    def start_recording(self):
        self.textbox.clear()
        self.status_label.setText("Status: 🔴 Recording...")
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.recognizer.start()

    def stop_recording(self):
        self.recognizer.stop()
        self.status_label.setText("Status: ⏹ Stopped")
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def update_textbox(self, text):
        print("Recognized:", text)
        self.textbox.append(text)
        self.send_to_api(text)

    def send_to_api(self, text):
        try:
            requests.post("http://127.0.0.1:8000/transcribe/", json={"text": text})
        except Exception as e:
            print(f"API Error: {e}")

    def export_txt(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.textbox.toPlainText())

    def export_pdf(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PDF Files (*.pdf)")
        if path:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in self.textbox.toPlainText().split("\n"):
                pdf.cell(200, 10, txt=line, ln=True)
            pdf.output(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VoiceApp()
    win.show()
    sys.exit(app.exec_())
