"""
Argumentos somente posicionais
"""


# def cumprimenta_v1(nome: str) -> str:
#     return f"Olá, {nome}"
#
#
# print(cumprimenta_v1("Gustavo"))
# print(cumprimenta_v1(nome="Gustavo"))

# def cumprimenta_v2(nome: str, /) -> str:
#     return f"Olá, {nome}"
#
#
# print(cumprimenta_v2("Gustavo"))
# print(cumprimenta_v2(nome="Gustavo"))

# def cumprimenta_v4(nome: str, mensagem: str, /) -> str:
#     return f"Olá, {nome}, {mensagem}"
#
#
# print(cumprimenta_v4("Gustavo", "correr"))
# print(cumprimenta_v4("Gustavo", "sdsd"))

# def cumprimenta_v5(*, nome: str, mensagem: str) -> str:
#     return f"Olá, {nome}, {mensagem}"
#
#
# print(cumprimenta_v5(nome="Gustavo", mensagem="correr"))
# print(cumprimenta_v5("Gustavo", "sdsd"))

def cumprimenta_v6(nome: str, /, mensagem: str = "Olá", *, msn: str) -> str:
    return f"{nome} {mensagem} {msn}"


print(cumprimenta_v6("g", mensagem="asdasd", msn="ddddddddd"))
