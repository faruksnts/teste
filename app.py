import streamlit as st

def jogo_namoro():
    pontos = 0

    st.title("O jogo")
    st.write("Olá! Vamos jogar um pequeno jogo? Responda as perguntas a seguir:")

    resposta1 = st.text_input("1. Qual é a cor do céu durante o dia?")
    if resposta1.lower() == "azul":
        pontos += 1
        st.success("Correto!")
    elif resposta1:
        st.error("Errado! A resposta correta é 'azul'.")

    resposta2 = st.text_input("2. Quantas patas tem um cachorro?")
    if resposta2 == "4":
        pontos += 1
        st.success("Correto!")
    elif resposta2:
        st.error("Errado! A resposta correta é '4'.")

    resposta3 = st.text_input("3. quem é melhor selenators ou beliebers ?")
    if resposta3.lower() == "selenators":
        pontos += 1
        st.success("Correto!")
    elif resposta3:
        st.error("Errado! A resposta correta é 'selenators'.")

    if resposta1 and resposta2 and resposta3:
        if pontos == 3:
            st.success(f"Parabéns, você acertou todas as perguntas! Agora, a pergunta mais importante:")
            st.write("Você quer sair comigo?")
        else:
            st.error(f"Você acertou {pontos} de 3 perguntas. Mas a pergunta mais importante ainda está por vir:")
            st.write("Você quer sair comigo e mudar de opinião?")

jogo_namoro()
