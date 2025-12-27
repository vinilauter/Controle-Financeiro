import gspread 
import pandas as pd
import streamlit as st

@st.cache_data

def load_data():

    # client auth
    cliente = gspread.service_account(filename = './service_account.json')

    # open sheet
    sheet = cliente.open("Controle Financeiro  (respostas)")

    # open worksheet
    worksheet = sheet.sheet1

    # get data
    brute_data = worksheet.get_all_records()

    # create dataframe
    dataframe = pd.DataFrame(brute_data)

    print(dataframe.columns)

    # rename columns for better coding
    dataframe = dataframe.rename(columns={"Carimbo de data/hora": "Data Atual", "Natureza da Operação": "Operacao", "Forma de Pagamento": "Meio", "Data": "Data Manual"})

    # money types cast
    dataframe["Valor"] = dataframe["Valor"].astype(str).str.replace(',', '.')
    dataframe["Valor"] = pd.to_numeric(dataframe["Valor"], downcast='float', errors='coerce')

    # date types cast
    dataframe["Data Atual"] = pd.to_datetime(dataframe["Data Atual"], dayfirst=True, errors="coerce")
    dataframe["Data Manual"] = pd.to_datetime(dataframe["Data Manual"], dayfirst=True, errors="coerce")

    # final date logic
    dataframe["Data Final"] = dataframe["Data Manual"].fillna(dataframe["Data Atual"])

    # incomes and outcomes logic

    return dataframe
