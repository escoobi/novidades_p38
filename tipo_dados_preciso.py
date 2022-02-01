"""
Tipos de dados Precisos

def dobro(valor: int) -> int:
    return valor * 2


print(dobro(8))
print(dobro(42))

--------------------------
Literal type
Union
Final
Typed dictionaries
Protocols

"""

# Literal type

from typing import Literal


def pegar_status(usuario: str) -> Literal["Conectado", "Desconectado"]:
    pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        raise ValueError(f"Operação inválida. {operacao!r}")


def calcula_v2(operacao: Literal["+", "-"], num1: int, num2: int) -> None:
    if operacao == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        raise ValueError(f"Operação inválida. {operacao!r}")


# calcula_v2("+", 6, 4)
# calcula_v2("-", 10, 2)
# calcula_v2("*", 10, 5)

# Union

from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2
    if resultado > 50:
        return f"0 valor {resultado} é muito grande."
    else:
        return resultado
# Final

# from typing import Final
#
# nome: Final = "Gustavo"
# print(nome)
# nome = "Cardozo"
# print(nome)


# from typing import final
#
#
# @final
# class Pessoa:
#     pass
#
#
# class Estudade(Pessoa):
#     pass
#
#     @final
#     def estudar(self):
#         print("Estudando.")
#
#
# class Estagiario(Estudade):
#     pass
#
#     def estudar(self):
#         print("Estudante estudando.")


# Typed Dictionaries
#
# from typing import  TypedDict
#
#
# class CursoPython(TypedDict):
#     versao: str
#     atualizacao: int
#
#
# agora = CursoPython(versao="3.8.9", atualizacao=2021)
# print(agora)
#
# outro = CursoPython(algo="alho", bebo=True)
# print(outro)


# Protocols

from typing import Protocol


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f"Estudando {valor.titulo}")

class Venda:
    pass

v1 = Venda()

estudar(v1)