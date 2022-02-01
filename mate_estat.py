"""
math.prod - retorna o produto de um container numérico
"""
import math

nv1: list = [2, 3, 4]
nv2: tuple = (2, 3, 4)
nv3: set = {2, 3, 4}

# print(math.prod(nv1))
# print(math.prod(nv2))
# print(math.prod(nv3))

# math.isqrt - Raiz quadrada retornando um valor inteiro, vou utilizar o aplicativo

# print(math.isqrt(9)) # Não arrendona valores
# print(math.sqrt(9))
# print(math.isqrt(17)) # Não arrendona valores
# print(math.sqrt(17))

#math.dist - Retorna a distancia euclidiana entre dois pontos, 3d ou 2d
# Pontos 3D
#
p3d1: tuple = (12, 40, 50)
p3d2: tuple = (6, 7, 13)
#
# # Pontos 2D
#
p2d1: list = [12, 50]
p2d2: list = [6, 7]
#
# print(math.dist(p3d1, p3d2))
# print(math.dist(p2d1, p2d2))

# math.hypot - reporta a hipotenusa, ou norma euclisiana

# O '*' antes é para remove os valores do containers
# print(math.hypot(*p3d1))
# print(math.hypot(*p2d1))

# Estatistica
import statistics
# statistics.fmean - calcula a média de numéros reais, vamos usar no aplicativo.

valores_reais: list = [1.89, 2.89, 8.56, 0.25]
valores_inteiros: list = [1, 6, 89, 50]
#
# print(statistics.fmean(valores_reais))
# print(statistics.fmean(valores_inteiros))

# stattistics.geometric_mean
# print(statistics.geometric_mean(valores_reais))
# print(statistics.geometric_mean(valores_inteiros))

# statistics.multimode - retorna o valor mais frequente em uma sequencia - vamos usar no aplicativo


seq1: str = "Gustavo Oliveira Cardozo"
seq2: list = [1, 2, 9, 3, 2, 6, 3]
seq3: list = [1, 2, 8, 6, 8, 1, 1]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
