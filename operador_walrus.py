"""
Operador Walrus
"""

# Antes
#
# nome = "Gustavo"
# print(nome)
#
# # Com o Walrius
#
# print(nome := "Gustavo")


# Python 3.7
# cesta = []
# fruta = input("Informe a fruta: ")
# while fruta != "jaca":
#     cesta.append(fruta)
#     fruta = input("Informe a fruta: ")


# Python 3.8 com Walrus
cesta = []
while (fruta := input("Informe a fruta: ")) != "jaca":
    cesta.append(fruta)
