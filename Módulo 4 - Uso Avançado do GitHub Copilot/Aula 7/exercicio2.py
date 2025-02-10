import pandas as pd
import numpy as np

# Criando um DataFrame fictício com dados de vendas
data = {
    'Produto': ['GLP 13kg', 'GLP 45kg', 'GLP 13kg', 'GLP 20kg', 'GLP 45kg', 'GLP 20kg'],
    'Quantidade': [10, 5, 8, 7, 6, 9],
    'Valor_Unitario': [100, 400, 100, 200, 400, 200],
    'Data': pd.date_range(start='2024-01-01', periods=6, freq='D')
}
df = pd.DataFrame(data)

# Versão 1: Manipulação básica de dados (Sem GitHub Copilot)
df['Valor_Total'] = df['Quantidade'] * df['Valor_Unitario']
resumo_basico = df.groupby('Produto').agg({'Quantidade': 'sum', 'Valor_Total': 'sum'}).reset_index()
print("Resumo Básico:")
print(resumo_basico)


'''
# Versão 2: Manipulação otimizada com GitHub Copilot
def processar_dados(df):
    """Gera estatísticas avançadas de vendas."""
    df['Valor_Total'] = df['Quantidade'] * df['Valor_Unitario']
    resumo = df.groupby('Produto').agg({
        'Quantidade': ['sum', 'mean', 'max'],
        'Valor_Total': ['sum', 'mean']
    }).reset_index()
    resumo.columns = ['Produto', 'Total_Vendido', 'Média_Vendas', 'Máx_Vendas', 'Receita_Total', 'Média_Receita']
    return resumo

resumo_otimizado = processar_dados(df)
print("Resumo Otimizado:")
print(resumo_otimizado)
'''
'''
# Versão 3: Manipulação otimizada com GitHub Copilot e Analise Temporal
def processar_dados(df):
    """Gera estatísticas avançadas de vendas e inclui análise temporal."""
    df['Valor_Total'] = df['Quantidade'] * df['Valor_Unitario']
    
    # Agregação otimizada
    resumo = df.groupby('Produto').agg(
        Total_Vendido=('Quantidade', 'sum'),
        Média_Vendas=('Quantidade', 'mean'),
        Máx_Vendas=('Quantidade', 'max'),
        Receita_Total=('Valor_Total', 'sum'),
        Média_Receita=('Valor_Total', 'mean')
    ).reset_index()
    
    # Adicionando análise temporal
    df['Ano_Mês'] = df['Data'].dt.to_period('M')
    tendencia_vendas = df.groupby(['Ano_Mês', 'Produto'])['Quantidade'].sum().unstack()
    
    return resumo, tendencia_vendas

resumo_otimizado, tendencia_vendas = processar_dados(df)
print("Resumo Otimizado:")
print(resumo_otimizado)
print("Tendência de Vendas por Mês:")
print(tendencia_vendas)
'''
