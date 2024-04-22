import streamlit as st
import requests


st.header('Minhas Bicicletas', divider='rainbow')

response = requests.get('https://aps5-backend.onrender.com/bicicletas')

data = response.json()

st.table(response.json())