
"""Interando strings com while"""


nome = 'Pedro Vinícius'
novo_nome = ''

indice = 0
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'*{letra}'
    indice += 1
    
print(novo_nome)
