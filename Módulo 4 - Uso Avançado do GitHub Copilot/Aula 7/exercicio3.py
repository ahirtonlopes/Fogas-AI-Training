import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Versão 1: Análise básica de dados (Sem GitHub Copilot)
data = {
    'Produto': ['GLP 13kg', 'GLP 45kg', 'GLP 20kg', 'GLP 13kg', 'GLP 45kg'],
    'Quantidade': [10, 5, 7, 12, 6],
    'Valor_Unitario': [100, 400, 200, 100, 400],
    'Data': pd.date_range(start='2024-01-01', periods=5, freq='D')
}
df = pd.DataFrame(data)

# Cálculo de valor total
df['Valor_Total'] = df['Quantidade'] * df['Valor_Unitario']

# Estatísticas básicas
print(df.describe())

# Gráfico básico
plt.plot(df['Data'], df['Valor_Total'])
plt.xlabel('Data')
plt.ylabel('Valor Total')
plt.title('Vendas por Dia')
plt.show()

'''
# Versão 2: Código otimizado via GitHub Copilot
def analisar_dados(df):
    """Função otimizada para análise e visualização avançada."""
    df['Valor_Total'] = df['Quantidade'] * df['Valor_Unitario']
    
    # Estatísticas detalhadas
    resumo = df.groupby('Produto').agg(
        Total_Vendido=('Quantidade', 'sum'),
        Receita_Total=('Valor_Total', 'sum'),
        Média_Vendas=('Quantidade', 'mean'),
        Máx_Vendas=('Quantidade', 'max')
    ).reset_index()
    
    # Gráfico avançado
    plt.figure(figsize=(10, 5))
    for produto in df['Produto'].unique():
        subset = df[df['Produto'] == produto]
        plt.plot(subset['Data'], subset['Valor_Total'], label=produto)
    
    plt.xlabel('Data')
    plt.ylabel('Valor Total')
    plt.title('Vendas por Dia e Produto')
    plt.legend()
    plt.grid()
    plt.show()
    
    return resumo

resumo_otimizado = analisar_dados(df)
print(resumo_otimizado)
'''