import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

    "window": {
        "text": "You see yourself... standing outside.",
        "choices": []
    },

    "bed": {
        "text": "Something grabs your leg.",
        "choices": []
    },

    "off": {
        "text": "Silence... then breathing behind you.",
        "choices": []
    },

    "outside": {
        "text": "You escaped... or did you?",
        "choices": []
    }
}

@app.route('/')
def index():
    return redirect(url_for('game', scene='start'))

@app.route('/game')
def game():
    scene = request.args.get('scene', 'start')

    # Ending logic with randomness (AI feel)
    if scene in ["window", "bed", "off", "outside"]:
        endings = [
            "You survived... barely.",
            "Game Over. Something followed you.",
            "You wake up again. It never ends.",
            "You escaped. But at what cost?"
        ]
        text = story[scene]["text"] + " " + random.choice(endings)
        return render_template("index.html", data={"text": text, "choices": []})

    return render_template("index.html", data=story[scene])

# ✅ IMPORTANT: This starts your Flask server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)