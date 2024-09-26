import math
p = float(input('Digite o valor da peça em mm: '))
f = int(input('Digite a quantidade furações: '))

if f > 3:
    r1 = p / (f + 1)
    print('Se sua peça tem o valor de {:.1f}mm e você deseja fazer {} furações'.format(p, f))
    print('A cada {:.2f}mm você irá realizar uma furação, até realizar suas {} furações'.format(r1, f))

elif f <= 2:
    e = (p / 2) / f
print('Se sua peça tem o valor de {:.1f}mm e você deseja fazer {} furações'.format(p, f))
print('A cada {:.2f}mm você irá realizar uma furação, até realizar suas {} furações'.format(e, f))


