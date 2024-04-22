import streamlit as st
import requests
import json

url = "https://aps5-backend.onrender.com/"
def novo_emprestimo():
    st.header('Novo Empréstimo', divider='rainbow')
    id_usuario = st.text_input("Insira o ID do usuário")
    id_bicicleta = st.text_input("Insira o ID da bicicleta")
    data_emprestimo = st.text_input("Data do Emprestimo")
    if st.button("Cadastrar"):
        # else:
            # st.error("Dados incorretos")

        myurl = f"{url}emprestimos/usuarios/<id_usuario>/bicicletas/<id_bike>"

        payload = json.dumps({
            "id_usuario": id_usuario,
            "id_bicicleta": id_bicicleta,
            "data_emprestimo": data_emprestimo,
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", myurl, headers=headers, data=payload)

        print(response)


novo_emprestimo()


