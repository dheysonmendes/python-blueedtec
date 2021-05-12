def numeros(num1=0,num2=0):
    if num1 < num2:
        print('O primeiro numero é menor!')
    else:
        if num2 < num1:
            print('O segundo numero é menor!')
        else:
            print('Os numero são iguais!')



num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
numeros(num1,num2)

