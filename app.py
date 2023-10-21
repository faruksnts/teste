import streamlit as st

def main():
    st.title("Oi, amor!")
    st.write("Lembra daquela vez que te ajudei ?? Então, será que você poderia pagar meu Uber hoje?")
    
    resposta = st.button("Claro! (ps: tu não tem escolha, pode clicar!")
    if resposta:
        st.write("Você é 10!")
        # Aqui, podemos colocar um link para uma música ou mensagem de agradecimento, por exemplo.
        url = 'https://www.instagram.com/reel/CvwxfEWOLIv/?igshid=MzRlODBiNWFlZA=='
        st.markdown(f"[Clique aqui! A pessoa mais linda da familia! 😊]({url})")

if __name__ == "__main__":
    main()





