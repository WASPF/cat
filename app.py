# Required libraries:
# pip install streamlit

import streamlit as st

def apply_custom_styles():
    """
    Применяет стилизацию в стиле 'Slot Cat' (неоновые кошачьи цвета).
    """
    st.markdown(
        """
        <style>
        /* Основной фон - глубокий темно-фиолетовый */
        .stApp {
            background-color: #0f0c29;
            color: #f0f0f0;
        }
        
        /* Боковая панель */
        section[data-testid="stSidebar"] {
            background-color: #1b1464;
        }

        /* Заголовки с неоновым свечением */
        h1, h2, h3 {
            color: #ff00ff !important; /* Розовый неон */
            text-shadow: 2px 2px 10px #ff00ff;
            font-family: 'Lexend', sans-serif;
        }

        /* Карточки слотов в стиле Cat */
        .cat-slot-card {
            background: linear-gradient(145deg, #1b1464, #302b63);
            border-radius: 20px;
            padding: 15px;
            text-align: center;
            border: 2px solid #00d2ff; /* Голубой неон */
            box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
            transition: 0.4s;
            margin-bottom: 20px;
        }
        .cat-slot-card:hover {
            transform: translateY(-10px) rotate(2deg);
            border-color: #ff00ff;
            box-shadow: 0 10px 25px rgba(255, 0, 255, 0.5);
        }
        
        .cat-icon {
            font-size: 50px;
            margin-bottom: 10px;
        }

        /* Кнопки */
        div.stButton > button {
            background: linear-gradient(90deg, #ff00ff, #00d2ff);
            color: white;
            border: none;
            border-radius: 50px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            width: 100%;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            filter: brightness(1.2);
            color: white;
            border: none;
        }

        /* Футер */
        .cat-footer {
            text-align: center;
            padding: 30px;
            font-size: 14px;
            color: #00d2ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def render_header():
    """
    Верхняя часть сайта.
    """
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("# 🐾 SLOT CAT")
        st.markdown("*Мурррчащие выигрыши здесь!*")
    with col2:
        st.button("Вход 🐱")

def render_game_hall():
    """
    Игровой зал с кошачьими слотами.
    """
    st.subheader("😺 Твои любимые игры")
    
    # Список игр в стиле кошек
    games = [
        {"name": "Neon Meow", "icon": "🐱", "desc": "Классика жанра"},
        {"name": "Cat of Ra", "icon": "🐈‍⬛", "desc": "Древний Египет"},
        {"name": "Cyber Kitty", "icon": "🤖", "desc": "Будущее наступило"},
        {"name": "Lucky Paw", "icon": "🐾", "desc": "Удача в лапах"},
        {"name": "Fish Hunter", "icon": "🐟", "desc": "Поймай свою рыбку"},
        {"name": "Moonlight Cat", "icon": "🌙", "desc": "Ночные спины"}
    ]
    
    # Сетка игр
    for i in range(0, len(games), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(games):
                game = games[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                        <div class="cat-slot-card">
                            <div class="cat-icon">{game['icon']}</div>
                            <div style="font-size: 18px; font-weight: bold; color: #fff;">{game['name']}</div>
                            <div style="font-size: 12px; color: #00d2ff; margin-bottom: 10px;">{game['desc']}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    if st.button(f"Играть", key=f"play_{i+j}"):
                        st.balloons()
                        st.success(f"Загрузка {game['name']}... Мяу!")

def render_sidebar():
    """
    Навигация.
    """
    st.sidebar.image("https://img.icons8.com/neon/96/cat.png", width=100)
    st.sidebar.title("Кошачье Меню")
    st.sidebar.markdown("---")
    st.sidebar.radio("Перейти в:", ["🏠 Главная лапа", "🎁 Кошачьи бонусы", "🏆 Битва котов", "💎 VIP Клуб"])
    st.sidebar.info("Твой баланс: 5000 🐟")

def main():
    """
    Точка входа.
    """
    st.set_page_config(
        page_title="Slot Cat - Мурррчащее Казино",
        page_icon="🐾",
        layout="wide"
    )
    
    apply_custom_styles()
    render_sidebar()
    render_header()
    
    st.markdown("---")
    
    # Промо-баннер
    st.warning("⚡️ АКЦИЯ: Пополни счет на 100 🐟 и получи 50 фриспинов в игре 'Neon Meow'!")

    render_game_hall()
    
    # Футер
    st.markdown(
        """
        <div class="cat-footer">
            <p>© 2024 Slot Cat Casino. Играй ответственно. 21+</p>
            <p>Лицензия выдана Кот-Контролем №777-МЯУ</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()