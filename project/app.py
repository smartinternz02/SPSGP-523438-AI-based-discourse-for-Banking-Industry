from flask import Flask, render_template, request

app = Flask(__name__)
app.config["files"] = "."

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=4000, debug=True)
