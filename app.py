# Required libraries:
# pip install streamlit

import streamlit as st
import time

# --- ИНИЦИАЛИЗАЦИЯ СОСТОЯНИЯ (Имитация базы данных) ---
if 'balance' not in st.session_state:
    st.session_state.balance = 1000
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = "user" # user или admin

def apply_styles():
    """Кастомный неоновый стиль Slot Cat"""
    st.markdown("""
        <style>
        .stApp { background-color: #0f0c29; color: #f0f0f0; }
        h1, h2 { color: #ff00ff !important; text-shadow: 2px 2px 10px #ff00ff; }
        .balance-box {
            background: rgba(0, 210, 255, 0.1);
            border: 1px solid #00d2ff;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            color: #00d2ff;
        }
        div.stButton > button {
            background: linear-gradient(90deg, #ff00ff, #00d2ff);
            color: white; border-radius: 20px; border: none; width: 100%;
        }
        .admin-section {
            border: 2px dashed #ffce00;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def login_form():
    """Простая форма входа"""
    st.sidebar.subheader("Авторизация")
    user = st.sidebar.text_input("Логин", value="AdminCat")
    pwd = st.sidebar.text_input("Пароль", type="password")
    if st.sidebar.button("Войти"):
        st.session_state.is_logged_in = True
        if user == "AdminCat" and pwd == "777":
            st.session_state.user_role = "admin"
            st.sidebar.success("Вход как Админ!")
        else:
            st.session_state.user_role = "user"
            st.sidebar.success("Успешный вход!")
        st.rerun()

def admin_panel():
    """Функционал админ-панели"""
    st.markdown('<div class="admin-section">', unsafe_allow_html=True)
    st.header("⚙️ Админ-панель (Управление сайтом)")
    
    col1, col2 = st.columns(2)
    with col1:
        new_balance = st.number_input("Изменить баланс игрока", value=st.session_state.balance)
        if st.button("Обновить баланс"):
            st.session_state.balance = new_balance
            st.success("Баланс изменен!")
            
    with col2:
        st.write("Статистика сайта")
        st.info("Активных игроков: 124")
        st.warning("Запросов на вывод: 3")
    
    st.markdown('</div>', unsafe_allow_html=True)

def game_hall():
    """Игровой зал"""
    st.title("🐾 SLOT CAT - REAL PLAY")
    
    # Отображение баланса
    st.markdown(f'<div class="balance-box">Ваш баланс: {st.session_state.balance} 🐟</div>', unsafe_allow_html=True)
    
    st.write("### Выберите слот для игры")
    cols = st.columns(3)
    
    slots = ["Neon Kitty", "Cyber Claw", "Ultra Purr"]
    for i, slot in enumerate(slots):
        with cols[i]:
            st.image(f"https://via.placeholder.com/200x120/1b1464/ff00ff?text={slot}")
            if st.button(f"Ставка 10 🐟", key=f"slot_{i}"):
                if st.session_state.balance >= 10:
                    st.session_state.balance -= 10
                    with st.spinner('Вращаем...'):
                        time.sleep(1)
                    st.balloons()
                    st.success("Вы выиграли 50 🐟!")
                    st.session_state.balance += 50
                    st.rerun()
                else:
                    st.error("Недостаточно рыбов!")

def main():
    apply_styles()
    
    # Навигация в сайдбаре
    st.sidebar.title("Slot Cat Menu")
    
    if not st.session_state.is_logged_in:
        login_form()
        st.warning("Пожалуйста, войдите, чтобы начать игру.")
    else:
        page = st.sidebar.radio("Перейти:", ["🎰 Игровой зал", "💳 Касса", "👤 Профиль"])
        
        if st.session_state.user_role == "admin":
            if st.sidebar.checkbox("🔓 Открыть Админку"):
                page = "Админ-панель"

        if st.sidebar.button("Выход"):
            st.session_state.is_logged_in = False
            st.rerun()

        # Логика страниц
        if page == "🎰 Игровой зал":
            game_hall()
        elif page == "Админ-панель":
            admin_panel()
        elif page == "💳 Касса":
            st.header("Пополнение баланса")
            amount = st.number_input("Сумма пополнения (🐟)", min_value=10)
            if st.button("Оплатить"):
                st.session_state.balance += amount
                st.success(f"Баланс пополнен на {amount}!")
        elif page == "👤 Профиль":
            st.header("Ваш профиль")
            st.write(f"Статус: {st.session_state.user_role}")
            st.write(f"Всего выигрышей: 12,400 🐟")

if __name__ == "__main__":
    main()
