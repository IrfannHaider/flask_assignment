from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/greet/irfan")
def greet(name):
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5006)
    app.run(debug=True)

