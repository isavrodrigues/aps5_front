import streamlit as st
import requests


# tela não funcional, visto que não era obrigatório

st.header('Usuários', divider='rainbow')

response = requests.get('https://aps5-backend.onrender.com/usuarios')

data = response.json()
st.table(data=data)
