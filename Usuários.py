import streamlit as st
import requests
import pandas as pd

# tela não funcional, visto que não era obrigatório

st.header('Usuários', divider='rainbow')

response = requests.get('https://aps5-backend.onrender.com/usuarios')

data = response.json()["usuarios"]


df = pd.DataFrame(data)
st.table(df)

