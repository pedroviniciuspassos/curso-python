"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Pedro'
preco = 1000.95897643
variavel = '%s, o preço é de R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %08X' % (7000, 7000))