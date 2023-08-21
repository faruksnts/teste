import streamlit as st

def pergunta_resposta(pergunta, opcoes, resposta_correta):
    st.write(pergunta)
    resposta = st.radio("", opcoes)
    if resposta == resposta_correta:
        return 1
    else:
        return 0

def jogo_namoro():
    st.title(" O Jogo ")
    st.write("Responda às seguintes perguntas para desbloquear uma pergunta especial:")

    pontos = 0
    objetivo = 3
    perguntas = [("Se você fosse um legume, qual seria?", ["Batata", "Abobrinha", "Pimentão", "Abóbora irresistível"], "Abóbora irresistível"),
                 ("Se eu fosse um super-herói e você estivesse em perigo, qual seria o meu superpoder?", ["Voar", "Invisibilidade", "Fazer você se apaixonar por mim", "Superforça"], "Fazer você se apaixonar por mim"),
                 ("Qual é o meu truque de mágica favorito?", ["Fazer objetos desaparecerem", "Ler mentes", "Fazer você sorrir", "Levitação"], "Fazer você sorrir"),
                 ("Qual é o meu tipo de café favorito?", ["Espresso", "Cappuccino", "Latte", "O que tem você nele"], "O que tem você nele")]

    for pergunta, opcoes, resposta_correta in perguntas:
        pontos += pergunta_resposta(pergunta, opcoes, resposta_correta)

    if pontos >= objetivo:
        st.write(f"Parabéns! Você alcançou {pontos} pontos.")
        st.write("Aqui está a pergunta especial:")
        st.write("Você quer sair comigo?")
        resposta_final = st.text_input("Sua resposta:")
        if st.button("Enviar resposta"):
            if resposta_final.lower() in ['sim', 'claro', 'com certeza']:
                st.write("vlw :)")
            else:
                st.write("Tudo bem, respeito a sua decisão -'- ")
    else:
        st.write(f"Infelizmente, você não alcançou os {objetivo} pontos necessários. Tente novamente.")

if __name__ == '__main__':
    jogo_namoro()

