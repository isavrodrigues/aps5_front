import streamlit as st
import requests
import json

url = "https://aps5-backend.onrender.com/"
def nova_bicicleta():
    st.header('Nova Bicicleta', divider='rainbow')
    marca = st.text_input("Marca")
    modelo = st.text_input("modelo")
    cidade = st.text_input("Cidade")
    status = st.text_input("Status")
    if st.button("Cadastrar"):
        # else:
            # st.error("Dados incorretos")

        myurl = f"{url}bicicletas"

        payload = json.dumps({
            "marca": marca,
            "modelo": modelo,
            "cidade": cidade,
            "status" : status
        })

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", myurl, headers=headers, data=payload)

        print(response)


nova_bicicleta()


