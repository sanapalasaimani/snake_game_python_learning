from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
# Logic: Key beats Value
beats = {'Snake': 'Water', 'Water': 'Gun', 'Gun': 'Snake'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'rounds' not in session:
        session['user_score'] = 0
        session['comp_score'] = 0
        session['rounds'] = 0
        session['history'] = []

    if request.method == 'POST':
        # Don't allow more plays if game is over
        if session['rounds'] >= 3:
            return redirect(url_for('index'))

        user_input = request.form.get('choice')
        if user_input in choices:
            user_choice = choices[user_input]
            comp_choice = random.choice(list(choices.values()))
            
            result = ""
            if user_choice == comp_choice:
                result = "Tie"
            elif beats[user_choice] == comp_choice:
                result = "Win"
                session['user_score'] += 1
            else:
                result = "Lose"
                session['comp_score'] += 1
            
            session['rounds'] += 1
            session['history'].append({
                'round': session['rounds'],
                'user': user_choice,
                'comp': comp_choice,
                'result': result
            })
            session.modified = True

    game_over = session.get('rounds', 0) >= 3
    final_result = ""
    if game_over:
        if session['user_score'] > session['comp_score']:
            final_result = "🏆 Congratulations! You won the match!"
        elif session['comp_score'] > session['user_score']:
            final_result = "🤖 Game Over! Computer won the match!"
        else:
            final_result = "🤝 The overall match is a Draw!"

    return render_template('index.html', 
                           user_score=session.get('user_score', 0),
                           comp_score=session.get('comp_score', 0),
                           rounds=session.get('rounds', 0),
                           history=session.get('history', []),
                           game_over=game_over,
                           final_result=final_result)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
