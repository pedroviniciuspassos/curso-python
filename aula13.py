nome = 'Pedro Vinícius'
altura = 1.90
peso = 98
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
 # .2f são quantas casas decimais vai aparecer
linha_2 = f'pesa {peso} quilos, e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)