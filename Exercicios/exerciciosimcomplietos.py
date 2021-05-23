#01 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares 
# e ímpares em ordem crescente.
pares = []
impares = []
numeros = [pares, impares]
for x in range(7):
   num = int(input('Digite um numero: '))
   if num % 2 == 0:
      pares.append(num)      
   else:
      impares.append(num)        
numeros.sort()
print(f'Esses são os numeros pares {pares}.')
print(f'Esses são os numeros impares {impares}.')
print(f'A lista em ordem crescente é: {numeros}.')


#02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com essa formatação:
# """ 
# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# # [  7  ][  8  ][  9  ] 
matriz = [[],[],[]]
for l in range(0,3):
   for c in range(0,3):
      matriz[l][c] = int(input('Digite um valor: '))
for l in range(0,3):
   for c in range(0,3):
      print(f'[{matriz[l][c]:^5}]', end='')
   print()


# #03 - Aprimore o desafio anterior, mostrando no final:
#    # A) A soma de todos os valores pares digitados.
#    # B) A soma dos valores da terceira coluna. 
#    # C) O maior valor da segunda linha.



matriz = [[],[],[]]
somaPar = SomaCol = maior = 0
for l in range(0,3):
   for c in range(0,3):
      matriz[l][c] = int(input('Digite um valor: '))
for l in range(0,3):
   for c in range(0,3):
      print(f'[{matriz[l][c]:^5}]', end='')
   print()
