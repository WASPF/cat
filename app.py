from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

db = {"balance": 1000}

@app.route('/')
def index():
    return render_template('index.html', balance=db["balance"])

@app.route('/api/play', methods=['POST'])
def play():
    bet = 50
    if db["balance"] >= bet:
        db["balance"] -= bet
        is_win = random.random() < 0.2
        win_amount = random.choice([250, 500, 1000]) if is_win else 0
        db["balance"] += win_amount
        return jsonify({
            "status": "win" if is_win else "lose",
            "message": f"ВИГРАШ: {win_amount} 🐟" if is_win else "Спробуй ще!",
            "new_balance": db["balance"]
        })
    return jsonify({"status": "error", "message": "Мало коштів!"}), 400

if __name__ == '__main__':
    app.run()
