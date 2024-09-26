import math

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))

hi = math.sqrt(pow(co, 2) + pow(ca, 2))

print('O valor da hipotenusa é {:.2f}'.format(hi))