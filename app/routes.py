from flask import Blueprint, render_template, request
from app.scoring import score_symptoms

main = Blueprint('main', __name__)

@main.route('/') #this is my home screen
def index():
    return render_template('index.html') #show this html template

@main.route('/screen', methods=['POST']) #screening page... POST is SEND ANSWERS FROM SCREENING TO DATABASE
def screen():
    client_text = request.form['symptoms'] 
    return render_template('screening.html', client_text=client_text)

@main.route('/results', methods=['POST'])
def results():
    client_text = request.form['client_text']

    answers = [
        request.form.get('q1') == 'yes',
        request.form.get('q2') == 'yes',
        request.form.get('q3') == "yes",
        request.form.get('q4') == 'yes'
    ]

    if any(answers):
        from app.scoring import get_db
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        questions = [
            'pregnancy',
            'recent_injury',
            'blood clots',
            'hypertension'
        ]

        triggered = questions[[i for i, a in enumerate(answers) if a][0]]

        cursor.execute(
            "SELECT block_message FROM safety_question WHERE topic = %s", (triggered,)
        )
        row=cursor.fetchone()
        cursor.close()
        conn.close()

        return render_template('blocked.html',
            block_message=row['block_message'])
    
    result = score_symptoms(client_text)

    if result is None:
        return render_template('results.html',
            result=None,
            message="We couldn't match your symptoms. Please try describing them in a different way." \
            )
    
    return render_template('results.html', result=result)
    