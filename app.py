# Required libraries:
# pip install streamlit

import streamlit as st

def main():
    # Настройка страницы (Title и Favicon)
    st.set_page_config(
        page_title="Slot Cat Casino",
        page_icon="🐾",
        layout="wide",
        initial_sidebar_state="collapsed" # Прячем боковую панель для вида сайта
    )

    # Внедряем мощный CSS, чтобы убить стандартный вид Streamlit
    st.markdown("""
        <style>
        /* Прячем стандартные элементы Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Фон всего сайта */
        .stApp {
            background: radial-gradient(circle, #1a0b2e 0%, #050508 100%);
            color: #ffffff;
        }

        /* Навигация */
        .nav-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 5%;
            background: rgba(0, 0, 0, 0.8);
            border-bottom: 2px solid #ff00ff;
            position: sticky;
            top: 0;
            z-index: 999;
        }

        .logo {
            font-size: 28px;
            font-weight: bold;
            color: #ff00ff;
            text-shadow: 0 0 10px #ff00ff;
            text-transform: uppercase;
        }

        /* Кнопки входа/регистрации */
        .auth-buttons .btn {
            padding: 10px 25px;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            margin-left: 10px;
            border: none;
        }
        .btn-login { background: transparent; color: white; border: 1px solid #fff !important; }
        .btn-reg { background: linear-gradient(180deg, #ff00ff 0%, #800080 100%); color: white; }

        /* Баннер (Hero section) */
        .hero {
            text-align: center;
            padding: 60px 20px;
            background: url('https://img.freepik.com/free-vector/abstract-neon-lights-background-design_23-2148404249.jpg');
            background-size: cover;
            border-radius: 20px;
            margin: 20px 5%;
        }

        /* Сетка игровых карточек */
        .game-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 25px;
            padding: 40px 5%;
        }

        .game-card {
            position: relative;
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #333;
            transition: 0.3s;
            background: #111;
        }
        
        .game-card:hover {
            transform: scale(1.05);
            border-color: #00d2ff;
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.5);
        }

        .game-img {
            width: 100%;
            height: 250px;
            background: linear-gradient(45deg, #111, #222);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 50px;
        }

        .play-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.6);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: 0.3s;
        }
        .game-card:hover .play-overlay { opacity: 1; }

        .btn-play {
            background: #22c55d;
            color: white;
            padding: 12px 30px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
        }

        /* Кастомный сайдбар для админки (скрытый) */
        .admin-trigger {
            position: fixed;
            bottom: 10px;
            right: 10px;
            opacity: 0.1;
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. HEADER
    st.markdown("""
        <div class="nav-bar">
            <div class="logo">🐾 SLOT CAT</div>
            <div class="auth-buttons">
                <button class="btn btn-login">Вход</button>
                <button class="btn btn-reg">Регистрация</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. HERO BANNER
    st.markdown("""
        <div class="hero">
            <h1 style="font-size: 50px; margin-bottom: 10px;">МЯУ-БОНУС ЖДЕТ!</h1>
            <p style="font-size: 20px;">+200% к первому депозиту и 500 фриспинов в Neon Meow</p>
        </div>
    """, unsafe_allow_html=True)

    # 3. GAME SECTION
    st.markdown("<h2 style='padding-left: 5%;'>🔥 Популярные слоты</h2>", unsafe_allow_html=True)
    
    # Мы используем контейнеры Streamlit только как обертку для нашего HTML
    cols = st.columns(4)
    games = [
        {"name": "Neon Cat", "emoji": "🐱", "color": "#ff00ff"},
        {"name": "Lucky Paw", "emoji": "🐾", "color": "#00d2ff"},
        {"name": "Fish Gold", "emoji": "🐟", "color": "#ffce00"},
        {"name": "Moon Kitty", "emoji": "🌙", "color": "#800080"},
    ]

    for idx, game in enumerate(games):
        with cols[idx % 4]:
            st.markdown(f"""
                <div class="game-card">
                    <div class="game-img" style="color: {game['color']}">{game['emoji']}</div>
                    <div style="padding: 15px; text-align: center;">
                        <div style="font-weight: bold; margin-bottom: 10px;">{game['name']}</div>
                    </div>
                    <div class="play-overlay">
                        <a href="#" class="btn-play">ИГРАТЬ</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            # Невидимая кнопка для логики Streamlit (если нужно)
            if st.button(f"Запуск {idx}", key=f"logic_{idx}", help="Нажми чтобы играть"):
                st.toast(f"Запуск игры {game['name']}...")

    # 4. ADMIN PANEL (Скрытая область внизу)
    with st.expander("⚙️ Система управления (Админка)"):
        st.subheader("Настройки сайта")
        col_adm1, col_adm2 = st.columns(2)
        with col_adm1:
            st.text_input("Название сайта", value="Slot Cat")
            st.color_picker("Основной цвет неона", value="#ff00ff")
        with col_adm2:
            st.number_input("RTP игрока (%)", value=95)
            st.button("Сохранить изменения")

    # 5. FOOTER
    st.markdown("""
        <div style="text-align: center; padding: 50px; color: #444; border-top: 1px solid #222; margin-top: 50px;">
            <p>Slot Cat Casino © 2024. Все права защищены. 18+</p>
            <p style="font-size: 10px;">Этот сайт создан для демонстрации интерфейса на Streamlit.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
