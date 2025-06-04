# 🎙️ Voice-to-Text Transcriber (PyQt5 + FastAPI + Google AI)

A fully functional and visually modern **Windows desktop application** built using **Python** to convert **spoken voice into real-time transcriptions**.  
It uses the **Google Speech Recognition API (AI)** for highly accurate recognition, supports live transcription, and allows you to **export** to `.txt` and `.pdf` files.

---

## ✨ Features

✅ Voice-to-text conversion  
✅ User-friendly GUI with PyQt5  
✅ Google Web Speech API for highly accurate transcription  
✅ Start/Stop control with visual feedback  
✅ Export transcripts as `.txt` or `.pdf`  
✅ Transcripts are stored via REST API (FastAPI)  
✅ Clean and professional UI design  

---

## 🧠 Technologies Used

| Layer         | Technology                          |
|---------------|--------------------------------------|
| Frontend GUI  | [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) |
| Backend API   | [FastAPI](https://fastapi.tiangolo.com/) |
| Speech Engine | [speech_recognition](https://pypi.org/project/SpeechRecognition/) (Google Web Speech API) |
| Export        | [FPDF](https://pyfpdf.github.io/) (PDF generation) |
| Language      | Python 3.8+ |
| Others        | Threading, HTTP (requests), REST API |

---


---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/voice-to-text-transcriber.git
cd voice-to-text-transcriber
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Required Packages

```bash
pip install PyQt5 fastapi uvicorn speechrecognition fpdf requests
```

