from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "secret_key"
import random

@app.route("/")
def index():
    if 'scores' not in session:
        session['scores'] = {"user":0, "computer":0}
    return render_template("game.html")

@app.route("/play", methods=['POST'])
def create():
    #0 =rock, 1=paper, 2= scissors
    if "scores" not in session:
        session["scores"] = {"user": 0, "computer":0}
    ROCK = 0
    PAPER = 1
    SCISSOR = 2
    player_choice = int(request.form["choice"])
    computer_choice = random.randint(0,3)
    print player_choice, computer_choice

    if computer_choice == ROCK:#rock
        if player_choice == SCISSOR:
            session["scores"]['computer'] +=1
        elif player_choice == PAPER:
            session["scores"]['user'] +=1
    elif computer_choice == PAPER:#paper
        if player_choice == ROCK:
            session["scores"]['computer'] +=1
        elif player_choice == SCISSOR:
            session["scores"]['user'] +=1
    elif computer_choice == SCISSOR:#paper
        if player_choice == PAPER:
            session["scores"]['computer'] +=1
        elif player_choice == ROCK:
            session["scores"]['user'] +=1
    session["last_user"] = player_choice
    session["last_computer"] = computer_choice
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
