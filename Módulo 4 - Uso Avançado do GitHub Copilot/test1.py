# 1. Revisão e Explicação de Código (Code Explain)

def calc_total(qty, price_per_unit, discount, tax):
    subtotal = qty * price_per_unit
    total_discount = subtotal * discount
    total_tax = (subtotal - total_discount) * tax
    total = subtotal - total_discount + total_tax
    return total

# Uso

print(calc_total(100, 50, 0.1, 0.05))