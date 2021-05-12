def numeros(a=0,b=0,limite=0):

    if (a + b) > limite:
        print('True')
    else:
        print('Digite novamente!')


a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
limite = float(input('Digite um numero limite: '))
numeros(a,b,limite)


