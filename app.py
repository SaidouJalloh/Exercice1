from flask import Flask
import random
app= Flask(__name__)
quotes =[
    "Le code est poèsie."
    "Docker c'est la vie",
    "Pas de git,pas de chocolat"
]
@app.route("/")
def index():
    return random.choice(quotes)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)