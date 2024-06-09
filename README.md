
# Análise de Vendas de Produtos Brasileiros

Este projeto faz parte do desafio do curso Formação Python Developer da [DIO](https://www.dio.me/). O objetivo deste projeto é realizar uma análise de vendas de produtos brasileiros utilizando Python e a biblioteca Streamlit para criação de gráficos interativos.

## Funcionalidades

- Carregamento e visualização de dados de vendas
- Análise e visualização de:
  - Total de vendas por cidade
  - Distribuição de vendas por categoria
  - Total de vendas por canal de venda
  - Vendas ao longo do tempo
  - Top 10 produtos vendidos

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Streamlit
- NumPy

## Pré-requisitos

Certifique-se de ter o Python instalado na versão 3.10 ou superior.

## Configuração do Ambiente

1. Clone o repositório para o seu ambiente local:

   ```sh
   git clone https://github.com/seu_usuario/analise-de-vendas.git
   cd analise-de-vendas
   ```

2. Crie e ative um ambiente virtual:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Coloque o arquivo `vendas.csv` na raiz do projeto (ou use seus próprios dados de vendas).

## Executando a Aplicação

Para executar a aplicação, utilize o comando:

```sh
streamlit run app.py
```

Isso abrirá a aplicação no navegador padrão, onde você poderá visualizar os gráficos interativos da análise de vendas.

## Autor

Rod

Este projeto faz parte do curso Formação Python Developer da [DIO](https://www.dio.me/).

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
