# get page
# test HTML

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.run(host="0.0.0.0", debug=True, port=5007)
