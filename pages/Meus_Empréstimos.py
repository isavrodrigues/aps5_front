import streamlit as st
import requests


st.header('Meus Empréstimos', divider='rainbow')

response = requests.get('https://aps5-backend.onrender.com/emprestimos')

data = response.json()

st.table(response.json())