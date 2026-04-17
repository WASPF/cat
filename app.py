# Required libraries:
# pip install flask

from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Храним баланс в памяти (сбросится при перезагрузке сервера)
user_data = {
    "balance": 1000
}

@app.route('/')
def index():
    """Главная страница сайта"""
    return render_template('index.html', balance=user_data["balance"])

@app.route('/spin', methods=['POST'])
def spin():
    """Логика игры: ставка 50, шанс выигрыша 25%"""
    bet = 50
    if user_data["balance"] >= bet:
        user_data["balance"] -= bet
        
        # Генерация выигрыша
        win_roll = random.random() # от 0 до 1
        win_amount = 0
        
        if win_roll < 0.25: # 25% шанс
            win_amount = random.choice([150, 300, 500])
            user_data["balance"] += win_amount
            result = "win"
        else:
            result = "lose"
            
        return jsonify({
            "status": result,
            "win_amount": win_amount,
            "new_balance": user_data["balance"]
        })
    else:
        return jsonify({"status": "error", "message": "Недостатньо коштів!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
