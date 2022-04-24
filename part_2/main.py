from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def all_candidates():
    candidates = load_candidates_from_json("candidates.json")
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def selected_candidate(candidate_id):
    candidate = candidate_selection_by_id(candidate_id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def candidates_by_name(candidate_name):
    list_by_name = candidate_selection_by_name(candidate_name)
    return render_template('search.html', list_by_name=list_by_name)


@app.route("/skill/<skill_name>")
def candidates_by_skill(skill_name):
    list_by_skill = candidate_selection_by_skill(skill_name)
    return render_template('skill.html', list_by_skill=list_by_skill, skill_name=skill_name.title())


app.run(debug=True, port=5005)
