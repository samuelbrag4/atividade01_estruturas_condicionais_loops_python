# ----- Objetivo 1 -----

# Criação de um programa que solicite ao usuário que insira um número, verificando se esse número é positivo, negativo ou zero. Exiba uma mensagem apropriada para cada caso.

# -- Código --

# Solicita ao usuário que ele insira um número
numero = float(input("Insira um numero:"))
# OBS: O float foi utilizado para que o usuário insira números inteiros ou decimais

# Verifica se o número é positivo
if numero > 0:
    print("O numero inserido é positivo.")
    
# Verifica se o número é negativo
elif numero < 0:
    print("O numero inserido é negativo.")
    
# Verifica se o número é zero
else :
    print("O numero inserido é zero.")
    
    
# ----- Objetivo 2 -----

# Desenvolvimento de um programa que faça uma contagem regressiva a patir de um número fornecido pelo usuário, de modo que a contagem termine em zero.

# -- Código --

# Solicita ao usuário que ele insira um número
numero_2 = int(input("Insira um numero:"))    
# OBS: O int foi utilizado para que o usuário insira somente números inteiros

# Realiação da contagem regressiva 
for i in range(numero_2, -1, -1):
    print(i)
    
# Explicações:

# 1. O range é uma função que faz uma sequência de números
# 2. O primeiro argumento é o número inicial da sequência
# 3. O segundo argumento é o número final da sequência
# 4. O terceiro argumento é o passo da sequência
# 5. O -1 no terceiro argumento faz com que a sequência seja decrescente
# 6. O -1 no segundo argumento faz com que a sequência vá até o número 0
# 7. O print(i) exibe cada número da sequência

# ----- Objetivo 3 -----

# Criação de um loop que solicita que o usuário insira vários números
# O loop deve ser interrompido quando o usuário inserir um número negativo, fornecendo a quantidade de tentativas ao final

# -- Código --

# Solicitação do número 
numero_3 = int(input("Insira um numero:"))
# OBS: O int foi utilizado para que o usuário insira somente números inteiros

# Contador de tentativas
contador_tentativas = 1

# Loop que solicita que o usuário insira vários números
while numero_3 >= 0:
    numero_3 = int(input("Insira um numero novamente:"))
    contador_tentativas += 1
# OBS: O contador_tentativas += 1 funciona de modo que o "+" adiciona, o "=" atribui o valor e o "1" é o valor atribuido

# Exibição da quantidade de tentativas
print(f"Quantidade de tentativas: {contador_tentativas}")
# OBS: O "f" foi utilizado para qye a variável "contador_tentativas" seja exibida na string (essa é a função do "f" em uma string)