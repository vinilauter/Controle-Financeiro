import pandas as pd
import streamlit as st
import plotly.express as px
from src.load_data import load_data
from src.controller import income_outcome_sum, category_group

# dataframe load
dataframe = load_data()

# globals

receitas_totais, despesas_totais, saldo_total = income_outcome_sum(dataframe)

depesas_categorizadas, receitas_categorizadas = category_group(dataframe)

# page config
st.set_page_config (
    page_title="Dashboard Financeiro",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="auto"
)

# title set

st.title("Dashboard Financeiro")

# dataframe display
st.dataframe(dataframe, width="stretch")

# outcomes pie chart by categories

grafico_despesas = px.pie(
    depesas_categorizadas,
    names="Categoria",
    values="Valor",
)

st.plotly_chart(grafico_despesas, use_container_width=True)

# incomes pie chart by categories

grafico_receitas = px.pie(
    receitas_categorizadas,
    names="Categoria",
    values="Valor",
)

st.plotly_chart(grafico_receitas, use_container_width=True)

# balance columns set

col1, col2, col3 = st.columns(3)

col1.metric(label="Entradas", value=f"R$ {receitas_totais:.2f}")

col2.metric(label="Saídas", value=f"R$ {despesas_totais:.2f}")

col3.metric(label="Saldo", value=f"R$ {saldo_total:.2f}")