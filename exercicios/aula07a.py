n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1+n2
mul = n1*n2
sub = n1-n2
d = n1/n2
di = n1//n2

print('A soma vale {}' .format(soma))
print('A multiplicação vale {}' .format(mul))
print('A subtração vale {}'.format(sub))
print('A divisao vale {:.3f}'.format(d))
print('A divisao inteira vale {}'.format(di))