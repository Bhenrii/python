salario = float(input('Digite seu salário: R$'))

aumento = salario + (salario * 0.15)
print('Seu salário teve um aumento de 15%')
print('Salário atual: R${:.2f}'.format(aumento))