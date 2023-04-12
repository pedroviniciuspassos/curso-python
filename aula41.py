""" while/else """
string = 'Valor qualquer'


i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        print('aqui está o espaço')
        break

    print(letra)
    i += 1
else:
    print('Não enconteri um espaço na string')
print('Fora do while.')