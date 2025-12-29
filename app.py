import pandas as pd
import streamlit as st
import plotly.express as px
from src.etl import load_data
from src.controller import income_outcome_sum, category_group, monthly_expenses, total_budget_calculus, category_budget_calculus
from src.utils import MESES, METAS

# dataframe load

dataframe = load_data()

# sidebar filter

st.sidebar.title("Filtros")

list_years = sorted(dataframe["Data"].dt.year.unique(), reverse=True) # extracts unique years and order from first to last 
selected_year = st.sidebar.selectbox("Selecione o Ano:", list_years)

df_year_filtered = dataframe[dataframe["Data"].dt.year == selected_year] # filter by year to show the months

list_months = sorted(df_year_filtered["Data"].dt.month.unique(), reverse=True) # extracts the months in the selected year

list_months.insert(0, 0) 

def format_month_name(option):
    if option == 0:
        return "Todos"
    return MESES[option]

selected_month = st.sidebar.selectbox(
    "Selecione o Mês:", 
    list_months, 
    format_func=format_month_name 
)

if selected_month != 0:
    df_filtered = df_year_filtered[df_year_filtered["Data"].dt.month == selected_month]
else:
    df_filtered = df_year_filtered


# globals

receitas_totais, despesas_totais, saldo_total = income_outcome_sum(df_filtered)

depesas_categorizadas, receitas_categorizadas = category_group(df_filtered)

# page config
st.set_page_config (
    page_title="Dashboard Financeiro",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="auto"
)

# title set

st.title("Dashboard Financeiro", text_alignment="center")

# balance display

col_entradas, col_saidas, col_saldo = st.columns(3)

col_entradas.metric(label="Entradas", value=f"R$ {receitas_totais:.2f}")

col_saidas.metric(label="Saídas", value=f"R$ {despesas_totais:.2f}")

col_saldo.metric(label="Saldo", value=f"R$ {saldo_total:.2f}")

# income and outcome sheet display

with st.expander("Ver Tabela Detalhada"):

    # exibition cleaning

    dataframe_exibicao = df_filtered[["Data", "Valor", "Operação", "Meio", "Categoria"]]

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

st.divider()

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

# budget display

st.divider()
st.subheader("Orçamento Mensal")

percentual_total = total_budget_calculus(df_filtered) 
val_total = min(1.0, percentual_total) # locks at 100%

st.caption(f"Meta Total: Gastou {(percentual_total*100):.1f}% do total disponível")
st.progress(val_total, text=f"Restam R$ {METAS['Total'] - despesas_totais:.2f}")

# budget by category

st.subheader("Orçamento por Categoria")
status_categorias = category_budget_calculus(df_filtered)

for i, item in enumerate(status_categorias):
    val_bar = min(1.0, item["percentual"])
    st.caption(f"**{item["categoria"]}**: Gastou {item["percentual"]*100:.1f}% do total disponível")
    st.progress(val_bar, text=f"Restam R$ {item["meta"] - item["gasto"]:.2f}")
    st.divider()