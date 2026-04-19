from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Story structure
story = {
    "start": {
        "text": "You wake up in a dark forest. You hear strange sounds...",
        "choices": [
            {"text": "Follow the light", "next": "light_path"},
            {"text": "Hide behind a tree", "next": "hide_path"}
        ]
    },
    "light_path": {
        "text": "You follow the light and find a mysterious stranger.",
        "choices": [
            {"text": "Talk to him", "next": "talk"},
            {"text": "Run away", "next": "run"}
        ]
    },
    "hide_path": {
        "text": "You hide. Something passes by... it's gone now.",
        "choices": [
            {"text": "Keep hiding", "next": "end_hide"},
            {"text": "Come out", "next": "light_path"}
        ]
    },
    "talk": {
        "text": "He gives you treasure. You win! 🎉",
        "choices": []
    },
    "run": {
        "text": "You fall into a trap. Game over 😢",
        "choices": []
    },
    "end_hide": {
        "text": "You stayed hidden forever... Game over.",
        "choices": []
    }
}

@app.route('/')
def index():
    return redirect(url_for('game', scene='start'))

@app.route('/game')
def game():
    scene = request.args.get('scene', 'start')
    data = story.get(scene)
    return render_template('index.html', data=data, scene=scene)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)