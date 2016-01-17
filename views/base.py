from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import render_template
from flask import abort
from flask import redirect

import services.questions

base_app = Blueprint('base_app', __name__)

@base_app.route("/")
def index():
    variables = {
        "questions": services.questions.get_questions()
    }

    return render_template("index.html", **variables)

@base_app.route("/start")
def start():
    questions = services.questions.get_questions()

    if not questions:
        abort(404)

    return redirect("/question/{qid}".format(qid=questions[0]))

@base_app.route("/question/<qid>", methods=['GET'])
def ask_question(qid=None):
    question = services.questions.get_question(qid)

    if question is None:
        abort(404)

    variables = question.to_primitive()
    variables.update({
        "qid": qid,
        "index": services.questions.get_index(qid) + 1
    })

    return render_template("question.html", **variables)

@base_app.route("/question/<qid>", methods=['POST'])
def set_choice(qid=None):
    question = services.questions.get_question(qid)

    if question is None:
        abort(404)

    selected_choice_id = request.form.get('choices')

    if selected_choice_id is None:
        return redirect("/question/{qid}".format(qid=qid))

    selected_choice = services.questions.get_selected_choice(selected_choice_id, question)

    if selected_choice is None:
        return redirect("/question/{qid}".format(qid=qid))

    services.questions.set_choice(qid, selected_choice)

    try:
        next_qid = services.questions.get_next_question(qid)
    except IndexError:
        return redirect("/done")
    except ValueError:
        abort(404)

    return redirect("/question/{qid}".format(qid=next_qid))

@base_app.route("/done")
def done():
    return render_template("done.html")
