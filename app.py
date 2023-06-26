from flask import Flask, render_template, request, redirect, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, Survey, satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY']= 'key'
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.debug = True

responses = []



@app.route('/')
def show_survey_title(methods="GET"):
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    print(satisfaction_survey.questions[0])
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/<int:id>')
def question_0(id, methods='GET'):
  
    print(len(responses))
    print(len(satisfaction_survey.questions))
    if(len(responses) != id):
        flash(f"Sorry, Invalid id!")
        return redirect(f"/questions/{len(responses)}")

    if(len(responses) == len(satisfaction_survey.questions)):
        return f"You've completed the survey, thank you!"
    else:
        question = satisfaction_survey.questions[id]
        return render_template('questions.html', question=question)

@app.route('/answers', methods=['POST'])
def redirect_to_next_question():
    print("hi",request.form['response'])
    answer = request.form['response']
    responses.append(answer)
    print(responses)
    return redirect(f"/questions/{len(responses)}")
    

