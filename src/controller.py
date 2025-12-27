import pandas as pd
import streamlit as st
from src.load_data import load_data

# dataframe load
dataframe = load_data()

# income and outcome sum function

def income_outcome_sum(dataframe):

    # income sum

    serie_receita = dataframe[dataframe["Operacao"] == "Receita"]

    receitas_totais = serie_receita["Valor"].sum()

    # outcome sum

    serie_despesa = dataframe[dataframe["Operacao"] == "Despesa"]

    despesas_totais = serie_despesa["Valor"].sum()

    # total sum

    saldo_total = receitas_totais - despesas_totais

    return receitas_totais, despesas_totais, saldo_total

# category group by function

def category_group(dataframe):

    depesas_categorizadas = dataframe[dataframe["Operacao"] == "Despesa"].groupby("Categoria").sum(["Valor"]).reset_index()

    receitas_categorizadas = dataframe[dataframe["Operacao"] == "Receita"].groupby("Categoria").sum(["Valor"]).reset_index()

    return depesas_categorizadas, receitas_categorizadas