# Exercícios
# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a 
# soma desses três argumentos.
def soma(a, b, c):
    soma = a + b + c
    print(f'A soma é {soma}.')




a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))


soma(a,b,c)

#---------------------------------------------------------------------------------------------

# 2. Faça um programa, com uma função que necessite de um argumento. A função retorna 
# o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for 
# negativo e ‘0’ se for 0

def valor(a):
    if a > 0:
        print('P')
    elif a < 0:
        print('N')
    else:
        print('0')



a= int(input('Digite um numero: '))
valor(a)

#---------------------------------------------------------------------------------------------

# 3. Faça um programa com uma função chamada somaImposto. A função possui dois 
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em 
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o 
# valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
t = float(input('Digite a taxa de imposto: '))
c = float(input('Digite o custo: '))
print('Valor com imposto:', somaImposto(t,c))

#---------------------------------------------------------------------------------------------

# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário 
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha 
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

#Duvida no valor pago por horas trabalhadas.

#---------------------------------------------------------------------------------------------

# 5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 
# 1,68 e pese 75kg.

def imc(peso, altura):
    imc = peso / altura**2
    print(f'Sua de massa corporal é: {imc:.1f}')



peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc(peso,altura)

#---------------------------------------------------------------------------------------------

# 6. Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota Conceito
# >=9.0 A
# >=8.0 B
# >=7.0 C
# >=6.0 D
# # <=4.0 F

def nota(n):
    if n >= 9.0:
        print('Sua nota foi A')
    if n < 9 and n >= 8.0:
        print('Sua nota foi B')
    if n < 8 and n >= 7.0:
        print('Sua nota foi C')
    if n < 7 and n >= 6.0:
        print('Sua nota foi D')
    if n < 6:
        print('Sua nota foi F')



n = float(input('Digite sua nota: '))
nota(n)

#---------------------------------------------------------------------------------------------  
    
# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles 
# # forem iguais, imprima que eles são iguais.
def maiormenor(a,b):
    if a > b:
        print('O primeiro é maior.')
    elif b > a:
        print('O segundo é maior.')
    else:
        print('Os numeros são iguais.')



a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
maiormenor(a,b)

#---------------------------------------------------------------------------------------------

# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no 
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que 
# Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro 
# terá 29 dias

def datas(dia,mes,ano):
    meses = ('zero', 'Janeiro',' Fevereiro', 'Marco',' Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 
        'Setembro', 'Outubro', 'Novembro', 'Dezembro')
           
    print(f'Você digitou a data de {dia} de {meses[mes]} de {ano}.') 




dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

datas(dia,mes,ano)   
        
    
      


