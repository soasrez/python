salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario*15/100)

print('O salário de R${:.2f} com um aumento de 15% se torna um salário de R${:.2f}'.format(salario, novo))