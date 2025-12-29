import pandas as pd
import streamlit as st
from src.etl import load_data
from src.utils import METAS

# dataframe load
dataframe = load_data()

# income and outcome sum function

def income_outcome_sum(dataframe):

    # income sum

    serie_receita = dataframe[dataframe["Operação"] == "Receita"]

    receitas_totais = serie_receita["Valor"].sum()

    # outcome sum

    serie_despesa = dataframe[dataframe["Operação"] == "Despesa"]

    despesas_totais = serie_despesa["Valor"].sum()

    # total sum

    saldo_total = receitas_totais - despesas_totais

    return receitas_totais, despesas_totais, saldo_total

# category group by function

def category_group(dataframe):

    depesas_categorizadas = dataframe[dataframe["Operação"] == "Despesa"].groupby("Categoria").sum(["Valor"]).reset_index()

    receitas_categorizadas = dataframe[dataframe["Operação"] == "Receita"].groupby("Categoria").sum(["Valor"]).reset_index()

    return depesas_categorizadas, receitas_categorizadas

# monthly expenses evolution

def monthly_expenses(dataframe):
    
    dataframe_mensal = dataframe.copy()

    dataframe_mensal["Mês"] = dataframe_mensal["Data"].dt.strftime("%Y-%m")

    despesa_mensal = dataframe_mensal[dataframe_mensal["Operação"] == "Despesa"].groupby("Mês").sum(["Valor"]).reset_index()

    return despesa_mensal

# budget calculus functions

def total_budget_calculus(dataframe):
    
    df_total_mensal = dataframe[dataframe["Operação"] == "Despesa"]

    total_mensal = df_total_mensal["Valor"].sum()

    porcentagem_mensal = total_mensal / METAS["Total"]

    return float(porcentagem_mensal)

def category_budget_calculus(dataframe):

    results = []

    df_despesas = dataframe[dataframe["Operação"] == "Despesa"] 

    gastos_por_cat = df_despesas.groupby("Categoria")["Valor"].sum()

    for categoria, meta_valor in METAS["Categorias"].items():
        
        gasto_real = gastos_por_cat.get(categoria, 0.0)
        
        if meta_valor > 0:
            percentual = float(gasto_real / meta_valor)
        else:
            percentual = 0.0
            
        results.append({
            "categoria": categoria,
            "gasto": gasto_real,
            "meta": meta_valor,
            "percentual": percentual
        })
        
    return results


