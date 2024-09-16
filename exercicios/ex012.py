preco=float(input('Preço do produto: R$ '))
novo = preco - (preco*5/100)
print('O valor do produto com desconto fica cai de R${:.2f} para R${:.2f}'.format(preco, novo))

