# save this as app.py
from flask import Flask ,render_template

app = Flask(__name__) #create our app


@app.route("/")
def hello():
    return render_template ("index.html")

@app.route("/samp")
def samp():
    return render_template ("samp.html")

@app.route("/news")
def news():
    return render_template ("news.html")

if __name__ == "__main__":
    app.run(debug=True, port=9000)
