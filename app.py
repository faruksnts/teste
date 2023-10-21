import streamlit as st
import random

def main():
    st.title("Pedra, Papel e Tesoura!")
    st.write("Vamos jogar!")

    opcoes = ["Pedra", "Papel", "Tesoura"]
    selecao = st.selectbox("Escolha sua jogada:", opcoes)

    if st.button("Jogar!"):
        jogada_computador = random.choice(opcoes)
        st.write(f"Computador escolheu: {jogada_computador}")

        if selecao == jogada_computador:
            st.write("Empate!")
        elif (selecao == "Pedra" and jogada_computador == "Tesoura") or \
             (selecao == "Papel" and jogada_computador == "Pedra") or \
             (selecao == "Tesoura" and jogada_computador == "Papel"):
            st.write("Você ganhou!")
        else:
            st.write("Você perdeu!")

if __name__ == "__main__":
    main()





