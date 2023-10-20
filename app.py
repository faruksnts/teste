import streamlit as st
import webbrowser

def main():
    st.title("Oi, amiga!")
    st.write("Aceita ser minha pessoa favorita para sempre?")

    resposta = st.button("Sim")
    if resposta:
        st.write("Sabia que você aceitaria! 😊")
        # Altere o URL abaixo para o endereço da música que você deseja compartilhar.
        webbrowser.open('https://youtu.be/238I_qBI4Rs?si=8PD797DQ_sA5U8i7')

if __name__ == "__main__":
    main()



