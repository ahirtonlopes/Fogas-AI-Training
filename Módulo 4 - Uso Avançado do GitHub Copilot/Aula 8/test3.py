# 3. Documentação

def calcular_frete(distancia, peso):
    if distancia <= 100:
        frete = 50
    else:
        frete = 50 + (distancia - 100) * 0.5
    if peso > 50:
        frete += (peso - 50) * 0.2
    return frete

# Usando o Copilot para gerar uma docstring que descreva a função, seus parâmetros e o valor de retorno;
# Adicionar exemplos de uso na docstring;