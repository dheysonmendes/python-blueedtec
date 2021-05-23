# Exercícios – Dicionários


# Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
# (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.​
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  ​

# dic = {1 : 1**2, 4 : 4**2, 5 : 5**2, 6 : 6**2, 7 : 7**2, 9 : 9**2 }
# lista = [dic]
# print(lista)


# Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] 
# e cada valor associado é o número ao quadrado.​
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# dicionario = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# lista = [dicionario]
# print('Os valores das chaves solicitadas são: ')
# for x in lista:
#     for c in x.values():       
#         print(c, end = ' ')
    



# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar
#  entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

# dic = {}
# list = []

# dic['nome'] = input('Nome: ')
# dic['media'] = float(input('Media: '))
# if dic['media'] >= 7 and dic['media'] <=10:
#     dic['situação'] = 'Aprovado'
#     print(dic)
# elif dic['media'] >= 5 and dic['media'] <=6.9:
#     dic['situação'] = 'Recuperação'
#     print(dic)
# else:
#     dic['situação'] = 'Reprovado'
#     print(dic)



# Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios.
#  Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado. Dicas: procure sobre a função randint(), 
# sleep() e itemgetter da bliblioteca operator.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jog1' : randint(1,6),'jog2' : randint(1,6),'jog3' : randint(1,6),'jog4' : randint(1,6)}
rank = {}

# print('Valores sorteados: ')
# for k , v in jogo.items():
#     print(f'{k} tirou {v}.')

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True )


print('Ranking de vencedores: ')
for d, g in enumerate(rank):
    print(f'{d + 1}° lugar é o {g[0]} com o numero {g[1]}.')



# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
#  Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente ,
#  além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.​​

dados = {}
dados['nome'] = input('Nome: ')
dados['nascimento'] = int(input('Data de nascimento: '))
dados['ctps'] = int(input('Numero CTPS: '))
if 'ctps' != 0:
    dados['anos'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Valor do salario: '))









# DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:​
# A) Quantas pessoas estão cadastradas.​
# B) A média da idade.​
# C) Uma lista com as mulheres.​
# D) Uma lista com as idades que estão acima da média.​
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.​
