import streamlit as st
import requests
import pandas as pd

st.header('Meus Empréstimos', divider='rainbow')

response = requests.get('https://aps5-backend.onrender.com/emprestimos')

data = response.json()["emprestimos"]

df = pd.DataFrame(data)
st.table(df)
