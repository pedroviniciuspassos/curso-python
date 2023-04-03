"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")

# verifica se o valor digitado é um número inteiro
if numero.isdigit():
  numero = int(numero)
  
  # verifica se o número é par ou ímpar
  if numero % 2 == 0:
    print(numero, "é um número par")
  else:
    print(numero, "é um número ímpar")
else:
  print(numero, "não é um número inteiro")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Digite a hora (formato 24 horas): ")

# verifica se a hora digitada é um número inteiro
if entrada.isdigit():
  hora = int(entrada)
  
  # verifica o horário e exibe a saudação apropriada
  if hora >= 0 and hora <= 11:
    print("Bom dia!")
  elif hora >= 12 and hora <= 17:
    print("Boa tarde!")
  elif hora >= 18 and hora <= 23:
    print("Boa noite!")
  else:
    print("Hora inválida!")
else:
  print("Hora inválida!")

    


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite o seu primeiro nome: ")

# verifica o tamanho do nome e exibe a mensagem apropriada
if len(nome) <= 4:
  print("Seu nome é curto.")
elif len(nome) >= 5 and len(nome) <= 6:
  print("Seu nome é normal.")
else:
  print("Seu nome é muito grande.")
