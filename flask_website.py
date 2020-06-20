from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/video')
def video():
    return render_template("video.html")

if __name__=="__main__":
    app.run(host='0.0.0.0')
#    app.run(Debug=True)
#    app.run(host='0.0.0.0', port=8080)