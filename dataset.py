import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Gerar datas aleatórias
def gerar_datas(inicio, fim, n):
    dias = (fim - inicio).days
    return [inicio + timedelta(days=random.randint(0, dias)) for _ in range(n)]

# Mapas de cidades e estados corretos
cidades_estados = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Belo Horizonte': 'MG',
    'Porto Alegre': 'RS',
    'Curitiba': 'PR',
    'Salvador': 'BA',
    'Fortaleza': 'CE',
    'Brasília': 'DF'
}
produtos = ['Arroz', 'Feijão', 'Café', 'Açúcar', 'Leite', 'Óleo', 'Farinha', 'Pão', 'Carne', 'Frango']
categorias = ['Alimentos', 'Bebidas', 'Limpeza', 'Higiene']
canais = ['Online', 'Loja Física']

# Gerar dados
n = 1000
datas = gerar_datas(datetime(2023, 1, 1), datetime(2023, 12, 31), n)
produtos_aleatorios = [random.choice(produtos) for _ in range(n)]
categorias_aleatorias = [random.choice(categorias) for _ in range(n)]
quantidades = np.random.randint(1, 20, size=n)
precos_unitarios = np.round(np.random.uniform(2.0, 50.0, size=n), 2)
valores_totais = quantidades * precos_unitarios
cidades_aleatorias = [random.choice(list(cidades_estados.keys())) for _ in range(n)]
estados_aleatorios = [cidades_estados[cidade] for cidade in cidades_aleatorias]
canais_aleatorios = [random.choice(canais) for _ in range(n)]

# Criar DataFrame
df = pd.DataFrame({
    'Data': datas,
    'Produto': produtos_aleatorios,
    'Categoria': categorias_aleatorias,
    'Quantidade': quantidades,
    'Preço Unitário': precos_unitarios,
    'Valor Total': valores_totais,
    'Cidade': cidades_aleatorias,
    'Estado': estados_aleatorios,
    'Canal de Venda': canais_aleatorios
})

# Salvar em um arquivo CSV
df.to_csv('vendas.csv', index=False, encoding='utf-8-sig')

print("Dataset de vendas gerado com sucesso!")

