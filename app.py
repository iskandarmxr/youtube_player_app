from flask import Flask, render_template, request
import threading
import webview

app = Flask(__name__)
video_url = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global video_url
    if request.method == 'POST':
        yt_link = request.form['yt_link']
        if "watch?v=" in yt_link:
            video_url = yt_link.replace("watch?v=", "embed/")
        elif "youtu.be" in yt_link:
            video_id = yt_link.split("/")[-1]
            video_url = f"https://www.youtube.com/embed/{video_id}"
        else:
            video_url = None
    return render_template('index.html', video_url=video_url)

def start_flask():
    app.run(debug=False, port=5000)

if __name__ == '__main__':
    threading.Thread(target=start_flask).start()
    webview.create_window("YouTube Player", "http://127.0.0.1:5000")