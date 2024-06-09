"""Módulos de importação"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Utilizando o Streamlit para criação dos gráficos


# Função para formatar valores em Real (BRL)
def formatar_brl(valor):
    """Função para formatar valores em Real (BRL)"""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Função para carregar os dados
@st.cache_data
def load_data():
    """Função para carregar os dados"""
    data = pd.read_csv("vendas.csv")
    data["Data"] = pd.to_datetime(data["Data"])
    return data


# Carregar os dados
data = load_data()

# Título da aplicação
st.title("Análise de Vendas de Produtos Brasileiros")

# Extrair dataset
st.subheader("Dados de Vendas")
st.write(data.head())

# Análise 1: Total de Vendas por Cidade
st.subheader("Total de Vendas por Cidade")
vendas_por_cidade = data.groupby("Cidade")["Valor Total"].sum().sort_values()
fig, ax = plt.subplots(figsize=(10, 6))
vendas_por_cidade.plot(kind="barh", color="skyblue", ax=ax)
ax.set_title("Total de Vendas por Cidade")
ax.set_xlabel("Valor Total (R$)")
ax.set_ylabel("Cidade")
ax.grid(axis="x")

# Adicionar valores formatados nos gráficos
for i in ax.patches:
    ax.text(
        i.get_width() + 0.1,
        i.get_y() + 0.5,
        formatar_brl(i.get_width()),
        ha="left",
        va="center",
    )

st.pyplot(fig)

# Análise 2: Total de Vendas por Categoria
st.subheader("Distribuição de Vendas por Categoria")
vendas_por_categoria = data.groupby("Categoria")["Valor Total"].sum()
fig, ax = plt.subplots(figsize=(8, 8))
vendas_por_categoria.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
    ax=ax,
)
ax.set_title("Distribuição de Vendas por Categoria")
ax.set_ylabel("")
st.pyplot(fig)

# Análise 3: Total de Vendas por Canal de Venda
st.subheader("Total de Vendas por Canal de Venda")
vendas_por_canal = data.groupby("Canal de Venda")["Valor Total"].sum()
fig, ax = plt.subplots(figsize=(8, 6))
vendas_por_canal.plot(kind="bar", color="coral", ax=ax)
ax.set_title("Total de Vendas por Canal de Venda")
ax.set_xlabel("Canal de Venda")
ax.set_ylabel("Valor Total (R$)")
ax.grid(axis="y")

# Adicionar valores formatados nos gráficos
for i in ax.patches:
    ax.text(
        i.get_x() + i.get_width() / 2,
        i.get_height() + 0.1,
        formatar_brl(i.get_height()),
        ha="center",
        va="bottom",
    )

ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
st.pyplot(fig)

# Análise 4: Vendas ao Longo do Tempo
st.subheader("Vendas ao Longo do Tempo")
vendas_mensais = data.groupby(data["Data"].dt.to_period("M"))["Valor Total"].sum()
fig, ax = plt.subplots(figsize=(12, 6))
vendas_mensais.plot(kind="line", marker="o", linestyle="-", color="blue", ax=ax)
ax.set_title("Vendas ao Longo do Tempo")
ax.set_xlabel("Mês")
ax.set_ylabel("Valor Total (R$)")
ax.grid(axis="both")
st.pyplot(fig)

# Análise 5: Top Produtos Vendidos
st.subheader("Top Produtos Vendidos")
top_produtos = (
    data.groupby("Produto")["Valor Total"].sum().sort_values(ascending=False).head(10)
)
fig, ax = plt.subplots(figsize=(10, 6))
top_produtos.plot(kind="bar", color="purple", ax=ax)
ax.set_title("Top 10 Produtos Vendidos")
ax.set_xlabel("Produto")
ax.set_ylabel("Valor Total (R$)")
ax.grid(axis="y")
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="right")
st.pyplot(fig)
