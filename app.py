# Required libraries:
# pip install flask

from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Имитация базы данных (в реальном проекте используйте SQL)
user_data = {
    "balance": 5000,
    "wins": 0
}

@app.route('/')
def index():
    """Главная страница сайта"""
    return render_template('index.html', balance=user_data["balance"])

@app.route('/play', methods=['POST'])
def play():
    """Логика игры: обработка ставки и рандом"""
    bet = 50
    if user_data["balance"] >= bet:
        user_data["balance"] -= bet
        
        # Шанс выигрыша
        win_chance = random.randint(1, 10)
        if win_chance > 7:  # 30% шанс на победу
            win_amount = random.choice([100, 200, 500, 1000])
            user_data["balance"] += win_amount
            result = {"status": "win", "amount": win_amount, "new_balance": user_data["balance"]}
        else:
            result = {"status": "lose", "amount": 0, "new_balance": user_data["balance"]}
            
        return jsonify(result)
    else:
        return jsonify({"status": "error", "message": "Недостатньо коштів!"}), 400

if __name__ == '__main__':
    # Запуск сервера
    app.run(debug=True, port=5000)
