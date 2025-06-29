# 🎬 YouTube Video Player Flask Desktop App

A simple Python desktop application that allows users to paste a YouTube link and automatically play the video inside the app. This project uses **Flask** for the backend and **pywebview** to provide a desktop GUI experience.

---

## 📦 Features

- Paste any YouTube video URL
- Automatically converts the link to embeddable format
- Video plays directly in the app window
- Lightweight and easy to run
- Works as a desktop application using `pywebview`

---

## 🛠️ Technologies Used

- Python 3.13.1
- Flask
- HTML5 (Jinja2 templating)
- PyWebView

---

## 📁 Project Structure
```
youtube_player_app/
│
├── app.py # Main application file
└── templates/
└── index.html # HTML template for UI
```

---

## ⚙️ Installation & Running

### 1. Clone this repository:
```bash
git clone https://github.com/yourusername/youtube-player-flask-app.git
cd youtube-player-flask-app
```
### 2. Install dependencies:
```bash
pip install flask pywebview
```
### Run the application:
```bash
python app.py
```

## 📌 Notes
This app uses YouTube's embed functionality — no video downloading is involved.

Ensure the YouTube link format is valid. Example:

https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ

Make sure your internet connection is active to stream videos.
