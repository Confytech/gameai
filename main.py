import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

leaderboard = []

story = {
    "start": {
        "text": "You wake up at 3:00AM. Your phone lights up... UNKNOWN NUMBER is calling.",
        "choices": [
            {"text": "Answer the call", "next": "call"},
            {"text": "Ignore it", "next": "ignore"}
        ]
    },

    "call": {
        "text": "A whisper says: 'I can see you.' Your lights flicker.",
        "choices": [
            {"text": "Check the window", "next": "window"},
            {"text": "Hide under the bed", "next": "bed"}
        ]
    },

    "ignore": {
        "text": "Your phone rings again. Louder. Closer.",
        "choices": [
            {"text": "Turn off phone", "next": "off"},
            {"text": "Run outside", "next": "outside"}
        ]
    },

    "window": {"text": "You see yourself... standing outside.", "choices": []},
    "bed": {"text": "Something grabs your leg.", "choices": []},
    "off": {"text": "Silence... then breathing behind you.", "choices": []},
    "outside": {"text": "You escaped... or did you?", "choices": []}
}

@app.route('/')
def index():
    return render_template("start.html")

@app.route('/start', methods=['POST'])
def start():
    name = request.form.get("name")
    return redirect(url_for('game', scene='start', name=name))

@app.route('/game')
def game():
    scene = request.args.get('scene', 'start')
    name = request.args.get('name', 'Player')

    if scene in ["window", "bed", "off", "outside"]:
        endings = [
            "You survived... barely.",
            "Game Over. Something followed you.",
            "You wake up again. It never ends.",
            "You escaped. But at what cost?"
        ]

        score = random.randint(0, 100)
        leaderboard.append({"name": name, "score": score})
        leaderboard.sort(key=lambda x: x["score"], reverse=True)

        text = story[scene]["text"] + " " + random.choice(endings)

        return render_template("end.html", text=text, score=score, leaderboard=leaderboard[:5])

    return render_template("index.html", data=story[scene], name=name)

if __name__ == '__main__':
    app.run(debug=True)