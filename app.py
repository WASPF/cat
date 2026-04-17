# Libraries: pip install flask
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# В реальности данные должны быть в базе данных (SQL)
user_stats = {
    "balance": 1000.0,
    "last_win": 0
}

@app.route('/')
def index():
    """Главная страница сайта."""
    return render_template('index.html', balance=user_stats["balance"])

@app.route('/api/spin', methods=['POST'])
def spin():
    """Логика генерации результата (Backend-side)."""
    bet = 20.0
    if user_stats["balance"] < bet:
        return jsonify({"error": "Insufficient funds"}), 400

    user_stats["balance"] -= bet
    
    # Генерируем символы (например: 7, BAR, Cherry, Lemon, Grape)
    symbols = ['7', 'BAR', 'CHERRY', 'LEMON', 'GRAPE']
    reels = [random.choice(symbols) for _ in range(3)]
    
    win_amount = 0
    # Логика выигрыша
    if reels[0] == reels[1] == reels[2]:
        if reels[0] == '7': win_amount = bet * 10
        elif reels[0] == 'BAR': win_amount = bet * 5
        else: win_amount = bet * 2
    
    user_stats["balance"] += win_amount
    user_stats["last_win"] = win_amount
    
    return jsonify({
        "reels": reels,
        "win": win_amount,
        "new_balance": user_stats["balance"]
    })

if __name__ == '__main__':
    app.run(debug=True)
