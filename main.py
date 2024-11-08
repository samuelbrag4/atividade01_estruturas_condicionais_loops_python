# ----- Objetivo 1 -----

# Criação de um programa que solicite ao usuário que insira um número, verificando se esse número é positivo, negativo ou zero. Exiba uma mensagem apropriada para cada caso.

# -- Código --

# Solicita ao usuário que ele insira um número
numero = float(input("Insira um numero:"))
# OBS: O float foi utilizada para que o usuário insira somente números decimais

# Verifica se o número é positivo
if numero > 0:
    print("O numero inserido é positivo.")
    
# Verifica se o número é negativo
elif numero < 0:
    print("O numero inserido é negativo.")
    
# Verifica se o número é zero
else :
    print("O numero inserido é zero.")