import  streamlit as st
import pandas as pd

st.write("Olá, mundo")

nome = "Thalita"
idade = 17

st.write(nome, idade)

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})

st.title("Meu primeiro dash")
st.subheader("Thalita")

st.write(df)