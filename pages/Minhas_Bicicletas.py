import streamlit as st
import requests
import pandas as pd

st.header('Minhas Bicicletas', divider='rainbow')

response = requests.get('https://aps5-backend.onrender.com/bicicletas')

data = response.json()['bicicletas']
df = pd.DataFrame(data)
st.table(df)
