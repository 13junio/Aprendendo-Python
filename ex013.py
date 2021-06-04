salario = float(input('Qual é o valor do salario? R$ '))
novo = salario + (salario * 15 / 100)
print('O salario atual R${} com o aumento  de 15%, você receberá R$ {:.2f}'.format(salario, novo))
