# Required libraries:
# pip install streamlit

import streamlit as st
import random

def main():
    # Полная настройка страницы
    st.set_page_config(
        page_title="Slot Cat - Мурррчащий Выигрыш",
        page_icon="🐾",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Инициализация игровых данных в сессии
    if 'balance' not in st.session_state:
        st.session_state.balance = 1000
    if 'wins' not in st.session_state:
        st.session_state.wins = 0

    # CSS для ПОЛНОГО перекрытия интерфейса Streamlit
    st.markdown("""
        <style>
        /* Скрываем мусор Streamlit */
        header, footer, .stDeployButton, [data-testid="stHeader"] { display: none !important; }
        .block-container { padding: 0 !important; }
        
        /* Главный контейнер сайта */
        .main-site {
            background-color: #050508;
            color: white;
            min-height: 100vh;
            font-family: 'Arial', sans-serif;
        }

        /* Хедер */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 50px;
            background: #0d0e12;
            border-bottom: 2px solid #ff00ff;
        }

        .logo { font-size: 26px; font-weight: bold; color: #ff00ff; text-shadow: 0 0 10px #ff00ff; }
        
        .balance-display {
            background: #1a2029;
            padding: 8px 20px;
            border-radius: 20px;
            border: 1px solid #00d2ff;
            color: #00d2ff;
            font-weight: bold;
        }

        /* Сетка игр */
        .container { padding: 40px 50px; }
        
        .slot-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 25px;
        }

        /* Карточка игры */
        .game-card {
            background: #161a21;
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #333;
            transition: 0.3s;
            text-align: center;
            padding-bottom: 15px;
        }

        .game-card:hover {
            border-color: #ff00ff;
            transform: scale(1.02);
            box-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
        }

        .game-preview {
            height: 150px;
            background: linear-gradient(45deg, #1a1464, #ff00ff);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 50px;
        }

        .game-title { margin: 15px 0; font-weight: bold; font-size: 18px; }

        /* Реальная кнопка внутри Streamlit через кастомный стиль */
        div.stButton > button {
            background: #22c55d !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            width: 80% !important;
            font-weight: bold !important;
            margin: 0 auto !important;
            display: block !important;
        }
        
        div.stButton > button:hover {
            background: #1fb355 !important;
            box-shadow: 0 0 10px #22c55d !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # ВЕРХНЯЯ ПАНЕЛЬ
    st.markdown(f"""
        <div class="navbar">
            <div class="logo">🐾 SLOT CAT</div>
            <div class="balance-display">БАЛАНС: {st.session_state.balance} 🐟</div>
        </div>
    """, unsafe_allow_html=True)

    # БАННЕР
    st.markdown("""
        <div style="background: linear-gradient(90deg, #1b1464, #4b0082); padding: 60px; text-align: center; margin-bottom: 20px;">
            <h1 style="color: white; font-size: 45px; margin: 0;">МЯУ-ДЖЕКПОТ</h1>
            <p style="color: #00d2ff; font-size: 20px;">Грай та вигравай разом з котом!</p>
        </div>
    """, unsafe_allow_html=True)

    # ИГРОВАЯ ЗОНА
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #ffce00;'>🎰 Ігровий зал</h2>", unsafe_allow_html=True)

    cols = st.columns(4)
    games = [
        {"name": "Neon Meow", "icon": "🐱"},
        {"name": "Lucky Paw", "icon": "🐾"},
        {"name": "Fish Gold", "icon": "🐠"},
        {"name": "Night Hunter", "icon": "🐈‍⬛"},
        {"name": "Cyber Slot", "icon": "🦾"},
        {"name": "Mouse Trap", "icon": "🧀"},
        {"name": "Cat Empire", "icon": "👑"},
        {"name": "Purr Spin", "icon": "🌀"}
    ]

    for i, game in enumerate(games):
        with cols[i % 4]:
            # Сама карточка (визуал)
            st.markdown(f"""
                <div class="game-card">
                    <div class="game-preview">{game['icon']}</div>
                    <div class="game-title">{game['name']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Реально работающая кнопка Streamlit
            if st.button(f"ГРАТИ", key=f"btn_{i}"):
                # ЛОГИКА ИГРЫ (Реальная работа)
                if st.session_state.balance >= 50:
                    st.session_state.balance -= 50 # Ставка
                    win_amount = random.choice([0, 0, 100, 200, 0, 500]) # Рандомный выигрыш
                    
                    if win_amount > 0:
                        st.session_state.balance += win_amount
                        st.session_state.wins += 1
                        st.balloons()
                        st.success(f"ВИГРАШ: {win_amount} 🐟!")
                    else:
                        st.error("Спробуй ще раз!")
                    
                    # Принудительное обновление для моментального отображения баланса
                    st.rerun()
                else:
                    st.warning("Недостатньо рибов для ставки!")

    st.markdown('</div>', unsafe_allow_html=True)

    # АДМИНКА (Встроена прямо в сайт, но скрыта внизу)
    with st.expander("🛠 Управління Слотами (Адмін)"):
        st.subheader("Налаштування казино")
        new_bal = st.number_input("Змінити баланс гравця", value=st.session_state.balance)
        if st.button("Оновити"):
            st.session_state.balance = new_bal
            st.rerun()

    # ФУТЕР
    st.markdown("""
        <div style="background: #0d0e12; padding: 40px; text-align: center; border-top: 1px solid #333; margin-top: 40px;">
            <p style="color: #666;">Slot Cat Casino © 2024. Ліцензія КРАЇЛ №777. Грайте відповідально.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
