# Required libraries:
# pip install streamlit

import streamlit as st

def main():
    # Настройка страницы: убираем отступы и ставим темную тему
    st.set_page_config(
        page_title="Slot Cat Casino",
        page_icon="🐾",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # ПОЛНЫЙ ИНЖЕКТ CSS ДЛЯ УДАЛЕНИЯ СЛЕДОВ STREAMLIT
    st.markdown("""
        <style>
        /* Прячем стандартный интерфейс Streamlit */
        header, footer, [data-testid="stSidebarNav"], .stDeployButton {
            display: none !important;
        }
        
        /* Убираем отступы контейнеров */
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }

        /* Общий фон сайта */
        .stApp {
            background-color: #050508;
            color: #eeeff0;
            font-family: 'Inter', sans-serif;
        }

        /* КАСТОМНЫЙ ХЕДЕР (Верхняя панель) */
        .custom-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 40px;
            background: rgba(13, 14, 18, 0.95);
            border-bottom: 1px solid #22c55d;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .logo {
            font-size: 24px;
            font-weight: 800;
            color: #ffce00;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .auth-btns {
            display: flex;
            gap: 15px;
        }

        .btn-entry {
            background: transparent;
            color: white;
            border: 1px solid #30353b;
            padding: 8px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
        }

        .btn-reg {
            background: #22c55d;
            color: #050508;
            border: none;
            padding: 8px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 700;
        }

        /* ГЛАВНЫЙ БАННЕР */
        .hero-banner {
            width: 100%;
            height: 350px;
            background: linear-gradient(90deg, #1a1464 0%, #ff00ff 100%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            margin-bottom: 30px;
        }

        .hero-title {
            font-size: 48px;
            font-weight: 900;
            margin: 0;
            color: white;
            text-shadow: 0 4px 10px rgba(0,0,0,0.5);
        }

        /* СЕТКА ИГР (СЛОТЫ) */
        .game-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px 40px;
        }

        .game-card {
            background: #1a2029;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #30353b;
            transition: transform 0.3s, border-color 0.3s;
            cursor: pointer;
        }

        .game-card:hover {
            transform: translateY(-5px);
            border-color: #ffce00;
        }

        .game-thumb {
            width: 100%;
            height: 180px;
            background: #000;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 60px;
        }

        .game-info {
            padding: 12px;
            text-align: center;
        }

        .play-btn {
            background: #22c55d;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }

        /* ФУТЕР */
        .footer {
            background: #0b0d11;
            padding: 40px;
            text-align: center;
            margin-top: 50px;
            border-top: 1px solid #1a2029;
            font-size: 14px;
            color: #8e949c;
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. ШАПКА САЙТА
    st.markdown("""
        <div class="custom-header">
            <div class="logo">🐾 SLOT CAT</div>
            <div class="auth-btns">
                <button class="btn-entry">Увійти</button>
                <button class="btn-reg">Реєстрація</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. ГЕРОЙ-БАННЕР
    st.markdown("""
        <div class="hero-banner">
            <p style="color: #ffce00; font-weight: bold; letter-spacing: 2px;">ВІТАЛЬНИЙ ПАКЕТ</p>
            <h1 class="hero-title">200 000 ₴ + 500 FS</h1>
            <button class="btn-reg" style="margin-top: 20px; padding: 15px 40px; font-size: 18px;">ЗАБРАТИ БОНУС</button>
        </div>
    """, unsafe_allow_html=True)

    # 3. ОСНОВНОЙ КОНТЕНТ
    st.markdown("<h2 style='margin-left: 40px; color: #ffce00;'>🎰 Популярні ігри</h2>", unsafe_allow_html=True)

    # Создаем сетку через стандартные колонки, но внутри кастомный HTML
    cols = st.columns(4)
    games = [
        {"name": "Cat of Olympus", "emoji": "⚡"},
        {"name": "Sweet Kitty", "emoji": "🍬"},
        {"name": "Fish Hunter", "emoji": "🐟"},
        {"name": "Meow Party", "emoji": "🎉"},
        {"name": "Wild Cat", "emoji": "🦁"},
        {"name": "Cyber Paw", "emoji": "🦾"},
        {"name": "Golden Tail", "emoji": "📀"},
        {"name": "Night Hunter", "emoji": "🌙"}
    ]

    for i, game in enumerate(games):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="game-card">
                    <div class="game-thumb">{game['emoji']}</div>
                    <div class="game-info">
                        <div style="margin-bottom: 10px; font-weight: 600;">{game['name']}</div>
                        <button class="play-btn">ГРАТИ</button>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            # Добавляем невидимую кнопку Streamlit поверх для функционала, если нужно
            if st.button(f"Play {i}", key=f"p_{i}", help=f"Натисніть для гри в {game['name']}", use_container_width=True):
                st.toast(f"Запуск {game['name']}...")

    # 4. АДМИН-ПАНЕЛЬ (Скрыта в самом низу)
    with st.expander("🛠️ Налаштування сайту (Адмін)"):
        st.write("Тут можна керувати шансом виграшу та бонусами")
        rtp = st.slider("RTP (%)", 0, 100, 95)
        st.button("Зберегти зміни")

    # 5. ФУТЕР
    st.markdown("""
        <div class="footer">
            <p>© 2024 Slot Cat - Казино України. Всі права захищені.</p>
            <p>Участь в азартних іграх може викликати ігрову залежність. 21+</p>
            <div style="margin-top: 20px;">
                <span style="border: 1px solid #8e949c; padding: 2px 5px; border-radius: 4px;">18+</span>
                <span style="margin-left: 15px;">Ліцензія КРАЇЛ №777</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
