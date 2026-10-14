from flask import Flask, jsonify, request
from flask_cors import CORS
from generator import make_puzzle, DIFFICULTY

app = Flask(__name__)
CORS(app)


@app.route("/api/puzzle")
def get_puzzle():
    difficulty = request.args.get("difficulty", "medium")

    if difficulty not in DIFFICULTY:
        difficulty = "medium"

    puzzle, solution = make_puzzle(difficulty)
    return jsonify({"puzzle": puzzle, "solution": solution})


if __name__ == "__main__":
    app.run(debug=True)