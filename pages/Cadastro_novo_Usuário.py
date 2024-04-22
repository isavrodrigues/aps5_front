import streamlit as st
import requests
import json

url = "https://aps5-backend.onrender.com/"
def novo_usuario():
    st.header('Novo Usuário', divider='rainbow')
    name = st.text_input("Nome")
    cpf = st.text_input("CPF")
    data_nascimento = st.text_input("Data de nascimento")
    if st.button("Cadastrar"):
        # else:
            # st.error("Dados incorretos")

        myurl = f"{url}usuarios"

        payload = json.dumps({
            "nome": name,
            "cpf": cpf,
            "data_nascimento": data_nascimento
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", myurl, headers=headers, data=payload)

        print(response)


novo_usuario()


