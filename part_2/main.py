from flask import Flask
from utils import *

app = Flask(__name__)

@app.route("/")
def load_():
    candidates_list = get_candidates("candidates.json")
    return candidates_list
