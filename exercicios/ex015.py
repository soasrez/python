dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

precoDia = dia * 60
precoKm = km * 0.15

pago = (dia*60) + (km*0.15)

print('O total a pagar é de R${:.2f}'.format(pago))