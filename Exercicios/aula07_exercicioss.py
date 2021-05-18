# Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) e imprime o 
# menor dos dois. Se eles forem iguais, imprima que são valores idênticos.

# def numeros(a,b):
#     num = [a,b]
#     if a != b:
#         print(min(num))
#     else:
#         print('Os valores idênticos')



# a = float(input('Digite o primeiro numero: '))
# b = float(input('Digite o segundo numero: '))
# numeros(a,b)

#-----------------------------------------------------------------------------------------------

# Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como parâmetro e 
# retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

# def numeros(a,b,limite):
#     if a + b > limite:
#         print('True.')


# a = float(input('Digite o primeiro numero: '))
# b = float(input('Digite o segundo numero: '))

# numeros(a,b,96)


#--------------------------------------------------------------------------------------------------

# Exercício Treino 3 - Crie uma função que receba uma string como argumento e retorne a 
# mesma string em letras maiúsculas. Faça uma chamada à função, passando como parâmetro 
# uma string.

# def letras(a):
#     print(a)



# a = input('Digite uma palavra ou frase: ').upper()
# letras(a)

#---------------------------------------------------------------------------------------------------

# Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como 
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma 
# pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse 
# exercício, pesquise sobre a função date da biblioteca Datetime.

# from datetime import date
# def voto(d):
#   if d >= 18:
#     print('OBRIGATORIO.')
#   elif 16 <= d < 18:
#     print('OPCIONAL.')
#   elif d < 16:
#     print('NEGADO.')
  



# d = int(input('Digite a data de nascimento: '))
# data_atual = date.today()
# data_atual = data_atual.year
# d = (data_atual - d)
# voto(d)


#-----------------------------------------------------------------------------------------------

# Exercício 5 - Faça um programa que tenha uma função chamada ficha(), que receba dois 
# parâmetros: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha 
# sido informado corretamente.

# def ficha(nome, gols):
#     print(f'Jogador {nome}.')
#     print(f'Marcou {gols} gols.')




# nome = input('Digite seu nome: ')
# gols = input('Digite a quantidade de gols marcados: ')
# ficha(nome, gols)

#----------------------------------------------------------------------------------------------------

# Exercício 6 
# Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as 
# duas notas mais altas para calcular a média.
# Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 
# provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))
# notas = [nota1, nota2, nota3]
# media = (nota1 + nota2 + nota3) / 3
# mediaalta = ((nota1 + nota2 + nota3) - min(notas)) / 2
# print(f'A media de todas as notas é:{media}')
# print(f'A média das duas notas mais altas é: {((nota1 + nota2 + nota3) - min(notas)) / 2}')
# print(f'Sua nota mais alta foi: {max(notas)}')
# print(f'Sua nota mais baixaa foi: {min(notas)}')

#-------------------------------------------------------------------------------------------------------


# PROJETO: Gastos com viagem - Escrever uma aplicação utilizando funções que calcule os 
# gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma 
# determinada cidade.
# Hospedagem
# 1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 
# 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.
# Passagem
# 2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da 
# passagem de avião, sendo que passagem para:
# - São Paulo custa R$ 312,00;
# - Porto Alegre custa R$ 447,00;
# - Recife custa R$ 831,00;
# - Manaus custa R$ 986,00.
# Aluguel de Carro
# 3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
# - Calcule o custo do aluguel do carro sendo que:
# - A cada dia o carro custa R$ 40,00;
# - Alugando 7 dias ou +: R$ 50,00 de desconto;
# - Alugando 3 dias ou +: R$ 20,00 de desconto;
# - Você pode receber apenas um desconto;
# - Retorne o custo.
# Cálculo Total
# 4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade 
# de dias e retorne o custo total da viagem.
# - Reutilize as funções já criadas.
# - Exiba o total da viagem chamando apenas a nova função declarada!
# Gastos Extras
# 5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e 
# some esse valor ao total da viagem.
# Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 
# adicionais

# def custo_hotel(noites):    
#     noites = noites * 140
#     print(f'O custo total do hotel é R$ {noites},00')


# def custo_aviao(cidade):
#     if cidade == 'SAO PAULO':
#         print('A passagem custa R$ 312,00. ')
#     elif cidade == 'PORTO ALEGRE':
#         print('A passagem para custa R$ 447,00. ')
#     elif cidade == 'RECIFE':
#         print('A passagem para custa R$ 831,00. ')
#     elif cidade == 'MANAUS':
#         print('A passagem custa R$ 986,00. ')
#     else:
#         print('Não temos passagems para essa cidade.')



# def custo_carro(dias):
#     dias1 = dias * 40.00
#     if dias >= 7:
#         dias1 = dias1 - 50.00
#     elif 3 <= dias < 7:
#         dias1 = dias1 - 20.00
#     print(f'O valor do aluguel do carro é R${dias1}.')



#4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade 
# de dias e retorne o custo total da viagem.
# - Reutilize as funções já criadas.
# - Exiba o total da viagem chamando apenas a nova função declarada!
# Gastos Extras

def total(noites,cidade,dias):
    a = noites
    b = 0
    c = 0
    def custo_hotel(noites):
        noites = noites * 140
        print(f'O custo total do hotel é R$ {noites},00')
        a = noites


    def custo_aviao(cidade):
        if cidade == 'SAO PAULO':
            b = 312.00
            print('A passagem custa R$ 312,00. ')
        elif cidade == 'PORTO ALEGRE':
            b = 447.00
            print('A passagem para custa R$ 447,00. ')
        elif cidade == 'RECIFE':
            b = 831.00
            print('A passagem para custa R$ 831,00. ')
        elif cidade == 'MANAUS':
            b = 986.00
            print('A passagem custa R$ 986,00. ')
        else:
            print('Não temos passagems para essa cidade.')



    def custo_carro(dias):
        dias1 = dias * 40.00
        if dias >= 7:
            dias1 = dias1 - 50.00
            c = dias1
        elif 3 <= dias < 7:
            dias1 = dias1 - 20.00
        c = dias1
        print(f'O valor do aluguel do carro é R$ {dias1}.')
    
    custo_hotel(noites)
    custo_aviao(cidade)
    custo_carro(dias)

    



noites = int(input('Digite o periodo hospedado em noites: '))
cidade = str(input('Digite a cidade de destino: ').upper())
dias = int(input('Digite o periodo de utilização do carro: '))






# custo_hotel(noites)
# custo_aviao(cidade)
# custo_carro(dias)
total(noites,cidade,dias)