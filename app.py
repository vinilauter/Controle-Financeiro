import pandas as pd
import streamlit as st
import plotly.express as px
from src.etl import load_data
from src.controller import income_outcome_sum, category_group, monthly_expenses

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

# balance display

col_entradas, col_saidas, col_saldo = st.columns(3)

col_entradas.metric(label="Entradas", value=f"R$ {receitas_totais:.2f}")

col_saidas.metric(label="Saídas", value=f"R$ {despesas_totais:.2f}")

col_saldo.metric(label="Saldo", value=f"R$ {saldo_total:.2f}")

# income and outcome sheet display

with st.expander("Ver Tabela Detalhada"):

    # exibition cleaning

    dataframe_exibicao = dataframe[["Data", "Valor", "Operação", "Meio", "Categoria"]]

    dataframe_exibicao["Data"] = dataframe_exibicao["Data"].dt.strftime("%d/%m/%Y")

    # dataframe display
    st.dataframe(dataframe_exibicao, width="stretch", hide_index=True, column_config={
        "Valor": st.column_config.NumberColumn(format="R$ %.2f")
    })

# outcomes pie chart by categories

grafico_despesas = px.pie(
    depesas_categorizadas,
    names="Categoria",
    values="Valor",
    title="Despesas por Categoria"
)

grafico_despesas.update_traces(
    textposition='inside',
    textinfo='percent+label', 
    hovertemplate='%{label}: <br>R$ %{value:.2f}' 
)

# incomes pie chart by categories

grafico_receitas = px.pie(
    receitas_categorizadas,
    names="Categoria",
    values="Valor",
    title="Receitas por Categoria"
)

grafico_receitas.update_traces(
    textposition='inside',
    textinfo='percent+label', 
    hovertemplate='%{label}: <br>R$ %{value:.2f}' 
)

# pie chart display

col_pie_despesas, col_pie_receitas = st.columns(2)

col_pie_despesas.plotly_chart(grafico_despesas, use_container_width=True)

col_pie_receitas.plotly_chart(grafico_receitas, use_container_width=True)

# monthly expenses evolution

despesa_mensal = monthly_expenses(dataframe)

# bar chart display

grafico_mensal = px.bar(
    despesa_mensal,
    x="Mês",
    y="Valor",
    title="Evolução Mensal de Despesas",
    labels={"Data": "Mês", "Valor": "Valor Gasto"}
)

grafico_mensal.update_layout(xaxis_type='category')

grafico_mensal.update_traces(
    hovertemplate='Mês: %{x} <br>Total: R$ %{y:.2f}'
)

st.plotly_chart(grafico_mensal, use_container_width=True)