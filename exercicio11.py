'''
11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta.
'''

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

delta = float((b ** 2) - 4 * a * c)

print(f'o Delta é:{delta}')

squareDelta = float(delta) ** 0.5

print(f'A raiz quadrada de Delta é: {squareDelta}')

x1 = (-b + squareDelta) / 2 . a

print(f'O x1 é: {x1}')
