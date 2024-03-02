import pandas as pd
import numpy as np
import streamlit as st

dados = 'dados_atualizados.csv'
df = pd.read_csv(dados, delimiter=',')
df = pd.DataFrame(df)

background = f"""
<style>
[data-testid = "stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/7135121/pexels-photo-7135121.jpeg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid = "stHeader"] {{
background: rgba(0,0,0,0)
}}
</style>
"""

st.markdown(background, unsafe_allow_html=True)

st.sidebar.header("Vendas de Biodiesel 2017 - 2024")
st.sidebar.caption("Vendas de biodiesel Petrobrás entre 01/2017 a 01/2024")

df['Ano'] = pd.to_datetime(df['Mês/Ano']).dt.year

soma_vendas_por_ano = df.groupby('Ano')['Vendas de Biodiesel'].sum()

st.dataframe(df)
st.subheader("Gráfico de Barras - Soma de Vendas por Ano")
st.bar_chart(soma_vendas_por_ano)
