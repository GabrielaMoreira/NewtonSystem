import numpy

def chutesQueDivergem():
    i = 0
    while (i < 25):
        j = 0
        while (j < 25):
            chute[0] = i
            chute[1] = j
            if (newton(chute,0.00001,1000) is None):
                print "Diverge: " + str(chute)
            j = j + 0.25
        i = i + 0.25

def chutesParaSol1():

    sol1 = numpy.zeros(2)
    if(p == 9):
        sol1[0] = 0.16
        sol1[1] = 1.31
    elif(p == 21):
        sol1[0] = 0.15
        sol1[1] = 1.32

    i = 0
    while (i < 25):
        j = 0
        while (j < 25):
            chute[0] = i
            chute[1] = j
            resultado = newton(chute,0.00001,5,nFixo=True)
            if(resultado is not None and (numpy.linalg.norm(resultado - sol1,numpy.inf) < 0.01)):
                print "Converge para a solucao " + str(sol1) + ": " + str(chute)
            j = j + 0.25
        i = i + 0.25

def chutesParaSol2():

    sol2 = numpy.zeros(2)
    if(p == 9):
        sol2[0] = 0.7
        sol2[1] = 6.14
    elif(p == 21):
        sol2[0] = 0.38
        sol2[1] = 6.13

    i = 0
    while (i < 25):
        j = 0
        while (j < 25):
            chute[0] = i
            chute[1] = j
            resultado = newton(chute,0.00001,5,nFixo=True)
            if(resultado is not None and (numpy.linalg.norm(resultado - sol2,numpy.inf) < 0.01)):
                print "Converge para a solucao " + str(sol2) + ": " + str(chute)
            j = j + 0.25
        i = i + 0.25

def F(X):
    ret = numpy.zeros(2)

    ret[0] = numpy.exp(-X[0]) + numpy.exp(X[1]) - pow(X[0],2) - 2*pow(X[1],3)
    ret[1] = numpy.cos(X[0] + p*X[1]) + p*X[0] - X[1] - 1

    return ret


def JF(X):
    ret = numpy.zeros((2,2))

    ret[0,0] = -2*X[0] - numpy.exp(-X[0])
    ret[0,1] = numpy.exp(X[1]) - 6*pow(X[1],2)
    ret[1,0] = p - numpy.sin(X[0] + p*X[1])
    ret[1,1] = -p * numpy.sin(X[0] + p*X[1]) - 1

    return ret


def newton(X,tol,n,verboso=False,nFixo=False):

    k = 0;
    if(verboso):
        print "k\t  X(k)\t\tEABS"
        print " ".join([str(k),"("+format(X[0],'6.6f')+", "+format(X[1],'6.6f')+")",format(0,'6.6f')])

    while (k < n):

        k = k + 1
        delta = numpy.dot((-numpy.linalg.inv(JF(X))),F(X))

        if(numpy.isnan(numpy.sum(delta))):
            break

        X = X + delta
        eabs = numpy.linalg.norm(delta,numpy.inf)

        if(verboso):
            print " ".join([str(k),"("+format(X[0],'6.6f')+", "+format(X[1],'6.6f')+")",format(eabs,'6.6f')])

        if (eabs < tol):
            if(k==n):
                return X
            if not (nFixo):
                return X
            else:
                return None

    return None

chute = numpy.zeros(2)

p = 9
print("p = 9")
print("Converge para solucao 1")
chute[0] = 0
chute[1] = 1
newton(chute,0.00001,5,verboso=True)
print ""

print("Converge para solucao 2")
chute[0] = 5
chute[1] = 6
newton(chute,0.00001,5,verboso=True)
print ""

print(">1000 iteracoes")
chute[0] = 0
chute[1] = 0
newton(chute,0.00001,5,verboso=True)
print ""

p = 21
print("p = 21")
print("Converge para solucao 1")
chute[0] = 0.5
chute[1] = 1.5
newton(chute,0.00001,5,verboso=True)
print ""

print("Converge para solucao 2")
chute[0] = 8
chute[1] = 2
newton(chute,0.00001,5,verboso=True)
print ""

print(">1000 iteracoes")
chute[0] = 2
chute[1] = 0.5
newton(chute,0.00001,5,verboso=True)
print ""

'''
Descomente isso para ver os testes feitos para encontrar chutes
Escolha um p:
p = 9 # Gabriela
p = 21 # Luiz
chutesParaSol1()
print "--------------------------------------------"
chutesParaSol2()
print "--------------------------------------------"
chutesQueDivergem()
'''
