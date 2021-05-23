#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela.
#    #  Se não, mostre que a multiplicação não foi maior que 40.


num1 = float(input('Primeiro Numero: '))
num2 = float(input('Segundo Numero: '))
print(f'A soma dos numeros {num1} e {num2} é {num1 + num2}.')
print(f'A multiplicação dos numeros {num1} e {num2} é {num1 * num2}.')
print(f'A divisão inteira dos numeros {num1} e {num2} é {num1 // num2}.')
if num1 > num2:
   print(f'O maior numero entre {num1} e {num2} é {num1}.')
else:
   print(f'O maior numero entre {num1} e {num2} é {num2}.')
if num1 + num2 % 2 == 0:
   print(f'O resultado da soma entre {num1} e {num2} é Par.')
else:
   print(f'O resultado da soma entre {num1} e {num2} é Impar.')
if num1 * num2 > 40:
   print(f'Se pegarmos a multiplicação de {num1} e {num2} e dividirmos pela divisão inteira entre eles o resultado é :{(num1 * num2) / (num1 // num2)}')
else:
   print(f'A multiplicação entre {num1} e {num2} não é maior que 40.')





#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada
#  pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma 
# vogal.

frase = input('Frase : ').lower()
lista = list(frase)
a = 0
e = 0
i = 0
o = 0
u = 0
for x in frase:
   if x == 'a':
      a =  a + 1
   elif x == 'e':
      e =  e + 1
   elif x == 'i':
      i =  i + 1
   elif x == 'o':
       o =  o + 1
   elif x == 'u':
      u =  u + 1
print(f'Temos {a} letras a.')
print(f'Temos {e} letras e.')
print(f'Temos {i} letras i.')
print(f'Temos {o} letras o.')
print(f'Temos {u} letras u.')
frase = frase.replace('a', '_')
frase = frase.replace('e', '_')
frase = frase.replace('i', '_')
frase = frase.replace('o', '_')
frase = frase.replace('u', '_')
print(f'A frase sem vogais é: {frase}.')   


#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para 
# iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê
#  boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em 
# um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada 
# palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou,
#  no final mostre quantos palpites foram necessários para vencer.


from random import randint #importação
codigo = 'blueedtech' #variavel que contem a senha para validar acesso
senha = str(input('Digite a senha para login: ')).strip() #validação da senha retirando os espaços
palpites = 1 #variavel para armazenar a quantidade de palpites
numero = int(randint(0,10)) #numero gerado pelo computador
while senha != codigo: #condição pra poder continuar o programa validando a senha
   print('ERRO! TENTE NOVAMENTE!') # msg de erro com senha errada
   senha =str(input('Digite a senha para login: ')).strip() #repetição de validação da senha retirando os espaços
nome = str(input('Qual seu nome: ')) # pede o nome do usuario
print(f'SEJA BEM VINDO {nome.upper()}!') # print's 
print('VAMOS JOGAR?')# print's 
print('ESSE É O JOGO DE ADIVINHAÇÃO DE DEVS!')# print's 
print('EU IREI PENSAR EM UM NUMERO E VOCÊ SÓ PRECISA DESCOBRI QUAL FOI ELE!')# print's 
print('VAMOS LÁ!')# print's 
print('PRONTO, PENSEI!')# print's 
jogador = int(input('VOCÊ CONSEGUE ADIVINHAR QUAL NUMERO EU PENSEI? ')) #palpite do jogador
while jogador != numero:
   if jogador < numero:
      print('Ops, Eu pensei em um numero maior do que esse!')
      jogador = int(input('Tenta de novo: '))
      palpites = palpites + 1
   elif jogador > numero:
      print('Não, não! Eu pensei em um numero menor do que esse!')
      jogador = int(input('Tenta de novo: '))
      palpites = palpites + 1
   elif jogador == numero:
      break
print(f'PARABENS, bem na mosca, eu realmente pensei no numero {numero}!')
print(f'Você precisou de {palpites} chance(s) para vencer!')


#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne
#  'data inválida' caso a data seja inválida.

def data(a,b,c):
   meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro'
    ]
   if mes == 1:
      print(f'A data é:{dia} de {meses[0]} de {ano} ')
   elif mes == 2:
      print(f'A data é:{dia} de {meses[1]} de {ano} ')
   elif mes == 3:
      print(f'A data é: {dia} de {meses[2]} de {ano} ')
   elif mes == 4:
      print(f'A data é: {dia} de {meses[3]} de {ano} ')
   elif mes == 5:
      print(f'A data é: {dia} de {meses[4]} de {ano} ')
   elif mes == 6:
      print(f'A data é: {dia} de {meses[5]} de {ano} ') 
   elif mes == 7:
      print(f'A data é: {dia} de {meses[6]} de {ano} ')
   elif mes == 8:
      print(f'A data é: {dia} de {meses[7]} de {ano} ')
   elif mes == 9:
      print(f'A data é: {dia} de {meses[8]} de {ano} ')
   elif mes == 10:
      print(f'A data é: {dia} de {meses[9]} de {ano} ')
   elif mes == 11:
      print(f'A data é: {dia} de {meses[10]} de {ano} ')
   elif mes == 12:
      print(f'A data é: {dia} de {meses[11]} de {ano} ')
print('Digeite uma data!')
dia = int(input('Dia:'))
while dia > 31:
   if dia > 31:
      print('Data invalida, tente novamente.')
      dia = int(input('Dia: '))
   elif dia <= 12:
      break
mes = int(input('Mês: '))
while mes == 2:
   if dia > 28:
      print('Data invalida, tente novamente.')
      dia = int(input('Dia: '))
   elif dia <= 28:
      break
while mes > 12:
   if mes > 12:
      print('Data invalida, tente novamente.')
      mes = int(input('Mês: '))
   elif mes <=12:
      break
ano = int(input('Ano: '))
while ano > 2021:
   if ano > 2021:
      print('Data invalida, tente novamente.')
      ano = int(input('Ano: '))
   elif mes <=12:
      break

data(dia,mes,ano)       


#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e 
# retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da 
# frase original.

def frasenova(frase):
   a = 0
   e = 0
   i = 0
   o = 0
   u = 0
   for x in frase:
      if x == 'a':
         a =  a + 1
      elif x == 'e':
         e =  e + 1
      elif x == 'i':
         i =  i + 1
      elif x == 'o':
         o =  o + 1
      elif x == 'u':
         u =  u + 1
   print(f'Temos {a} letras a.')
   print(f'Temos {e} letras e.')
   print(f'Temos {i} letras i.')
   print(f'Temos {o} letras o.')
   print(f'Temos {u} letras u.')
   frase = frase.replace('a', '_')
   frase = frase.replace('e', '_')
   frase = frase.replace('i', '_')
   frase = frase.replace('o', '_')
   frase = frase.replace('u', '_')
   frase = frase.replace('é', '_')
   frase = frase.replace('á', '_')
   frase = frase.replace('ã', '_')
   frase = frase.replace('ê', '_')
   frase = frase.replace('õ', '_')
   print(f'A frase sem vogais é: {frase}.')
   numero = frase.count('_')
   print(f'Foram retiradas {numero} letras.')
   lista = list(frase)  

frase = input('Frase : ').lower()
frasenova(frase)



#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".
 
   
suspeito = str(input('Nome: ').upper())
perguntas = ['Telefonou para a vitima?', 'Esteve no local do crime?', 'Mora perto da vitima?', 'Devia para a vitima?','Já trabalhou com a vitima?']
contagem = 0
resultado = 0
print('Responda as questões a seguir com SIM ou NÃO.')
for x in perguntas:
   resposta = str(input(f'{x}: ').lower().strip().replace('ã','a'))
   if resposta != 'sim' and resposta != 'nao':
      print('REPOSTA INCORRETA, COMECE NOVAMENTE.')
      resposta = str(input(f'{x}: ').lower().strip())
   if resposta == 'sim':
      contagem = contagem +1
if resultado == 2:
   print(f'{suspeito} é clasificado(a) como Suspeito(a).')
elif contagem >= 3 and contagem <=4:
   print(f'{suspeito} é clasificado(a) como Cumplice(a).')
elif contagem == 5:
   print(f'{suspeito} é clasificado(a) como Assassino(a).')
else:
   print(f'{suspeito} é clasificado(a) como Inocente.')

#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
#  única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares 
# em ordem crescente.

listaPar = []
listaImpar = []
listaGeral = [listaPar, listaImpar]
print('Digite 7 numeros aleatorios.')
for x in range(7):
   num = int(input('Numero: '))
   if num % 2 == 0:
      listaPar.append(num)
   else:
      listaImpar.append(num)
listaPar.sort()
listaImpar.sort()
print(listaGeral)

#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também 
# o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa
#  vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.


from datetime import date
dic = {}
data_atual = date.today() 
anoAtual = data_atual.year
dic['Nome'] = str(input('Nome: ')).upper().strip()
nascimento  = int(input('Ano de Nascimento: '))
while nascimento > 2021 or nascimento < 1900: # valida o ano de nascimento
   if nascimento > 2021 or nascimento < 1900:
      print('DATA INVALIDA, TENTE NOVAMENTE.')
      nascimento  = int(input('Ano de Nascimento: '))
ctps = int(input('CTPS: '))
idade = anoAtual - nascimento
dic['Nascimento'] = nascimento
dic['Ctps'] = ctps
dic['Idade'] = idade
dic['Idade de Aposentadoria'] = idade + 35
if ctps != 0: #valida a ctps
   anoContratacao = int(input('Ano de contratação: '))
   while anoContratacao > 2021 or anoContratacao <1900: #validação do ano de contratação
      if anoContratacao > 2021 or anoContratacao < 1900:
         print('DATA INVALIDA, TENTE NOVAMENTE.')
         anoContratacao  = int(input('Ano de Contratação: '))
   dic['Ano de Contratacão'] = anoContratacao
   dic['salario'] = float(input('Salário: R$ '))
   tempoServido = anoAtual - anoContratacao
   idadeAposentadoria = (idade + 35) - tempoServido
   if idadeAposentadoria < 0: #validação do valor da idade de aposentadoria
      idadeAposentadoria = 'Já Aposentado ou Falecido!'
   dic['Idade de Aposentadoria'] = idadeAposentadoria
   

print('*' * 65) 
print('Segue abaixo os dados e o resultado do cadastro realizado: ')
print()
print('*' * 100)
print(dic)
print('*' * 100)

