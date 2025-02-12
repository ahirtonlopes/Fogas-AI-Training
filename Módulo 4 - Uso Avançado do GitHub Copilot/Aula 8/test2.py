# 2. Refatoração de Código

def verificar_estoque(tipo_botijao):
    if tipo_botijao == "2kg":
        return "Disponível"
    elif tipo_botijao == "5kg":
        return "Disponível"
    elif tipo_botijao == "8kg":
        return "Indisponível"
    elif tipo_botijao == "13kg":
        return "Disponível"
    else:
        return "Tipo de botijão desconhecido"
    
# Refatorar o código de modo a torná-lo mais eficiente;
# Possivelmente utilizar um dicionário para mapear os tipos de botijão à sua disponibilidad;
# Adicionar tratamento para entradas inválidas ou desconhecidas.