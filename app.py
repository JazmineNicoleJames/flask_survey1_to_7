from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY']= 'key'
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.debug = True

response_session = "responses"

@app.route('/')
def show_survey_title(methods="GET"):
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    print(satisfaction_survey.questions[0])
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/sessions_form', methods=['POST'])
def sessions_form():
    session[response_session] = []
    return redirect("/questions/0")


@app.route('/answers', methods=['POST'])
def redirect_to_next_question():
    responses = session[response_session]
    answer = request.form['response']
    responses.append(answer)
    session[response_session] = responses
    print("*****************")
    print(session[response_session])
    return redirect(f"/questions/{len(responses)}")


@app.route('/questions/<int:id>')
def question_0(id, methods='GET'):
    responses = session.get(response_session)
    print(len(session['response']))

    if(len(responses) != id):
        flash(f"Sorry, Invalid id!")
        return redirect(f"/questions/{len(responses)}")

    if(len(responses) == len(satisfaction_survey.questions)):
        return f"You've completed the survey, thank you!"

    else:
        question = satisfaction_survey.questions[id]
        return render_template('questions.html', question=question)


    

