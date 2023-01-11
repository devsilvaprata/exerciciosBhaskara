'''
11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta.
'''

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print('não tem raiz de numero negativo')

else:
    x1 = (- b + delta ** (1 / 2)) // (2 * a)
    x2 = (- b - delta ** (1 / 2)) // (2 * a)

print(f' x1 é: {x1} e x2 é: {x2}')
