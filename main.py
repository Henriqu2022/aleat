'''#1694
#Sub programa
def ehPrimo(num):
    candidatoDivisorMinimo = 2
    candidatoDivisorMaximo = int(num**0.5)#num // 2
    qtdDivisores = 2
    for divisor in range(candidatoDivisorMinimo, candidatoDivisorMaximo + 1):
        print(divisor)
        if num % divisor == 0:
            print('Achei um divisor:',divisor)
            return False
            qtdDivisores = qtdDivisores + 1
    #print('Quantidade de divisores: ',qtdDivisores)
    return num > 1  and qtdDivisores == 2

#Programa Principal
numeroLido = int(input())
if ehPrimo(numeroLido) :
    print(numeroLido,'é primo')
else:
    print(numeroLido,'não é primo!!!')
'''

































'''
#2291
#Sub programa
def divisoresNum():
    divisores = []
    num = int(input())
    for denominador in range(1,num+1):
        if num % denominador == 0:
            divisores.append(denominador)
    return divisores
def achaNumeroDivino(divisores,posNumDiv):
    somaDivisores = 0
    for i in range(posNumDiv):
        somaDivisores += divisores[i]
        #if divisores[i]
    #numeroDivino
    return somaDivisores
#Principal
posicaoNumeroDivino = int(input())
divisores = divisoresNum()
while posicaoNumeroDivino > 0:
    numeroDivino = achaNumeroDivino(divisores,posicaoNumeroDivino)
    posicaoNumeroDivino = int(input())
return numeroDivino
'''


























'''
#2516
#Sub programa



#Principal
S,va,vb = map(int,input().split(' '))
'''































'''
#2674
#Sub programa
def ehPrimo(num):
    candidatoDivisorMinimo = 2
    candidatoDivisorMaximo = int(num**0.5)#num // 2
    qtdDivisores = 2
    for divisor in range(candidatoDivisorMinimo, candidatoDivisorMaximo + 1):
        #print(divisor)
        if num % divisor == 0:
            #print('Achei um divisor:',divisor)
            return False
            qtdDivisores = qtdDivisores + 1
    #print('Quantidade de divisores: ',qtdDivisores)
    return num > 1  and qtdDivisores == 2

def superPrimo(numLid):
    n
    return None
#Programa Principal
numeroLido = int(input())
'''




















#2680
#Sub programa
def adicionandoMatriculasFuncionarios(qtdFunc):
    matriculas = []
    for i in range(qtdFunc):
        matricula = int(input())
        matriculas.append(matricula)
    return matriculas
def divisoresNumeroMatricula(matriculas):
    divisores = []
    for denominador in range()
    return divisores

#Principal
quantidadeFuncionarios = int(input())
matriculasFuncionarios = adicionandoMatriculasFuncionarios(quantidadeFuncionarios)