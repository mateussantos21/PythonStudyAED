Lista 9
#Fun��es recursivas
#Fatorial
#dados: x � inteiro
def fatorial(x):
    if x==0:
        return(1)
    else:
        return x*fatorial(x-1)
#somatorio
#dados: n � inteiro
def somatorio(n):
    if n==1:
        return(1)
    return n+somatorio(n-1)
#contar algarismos
#dados: n � inteiro
def qtddealgarismos(n):
    if n//10==0:
        return(1)
    return 1+qtddealgarismos(n//10)
#fibonacci
#i � real
def fibonacci(i):
    if i==0:
        return(1)
    if i==1:
        return(-1/2)
    return fibonacci(i-1)+fibonacci(i-2)
#y^x
#y,x s�o reais
def exponencial(y,x):
    if x==0:
        return(1)
    if x==1:
        return(y)
    return y*exponencial(y,x-1)
#mdc
#x, y s�o inteiros
def mdc(x,y):
    if x>y:
        if y==0:
            return(x)
        else:
            return mdc(y,x%y)
    else:
        if x==0:
            retunr(y)
        else:
            return mdc(x,y%x)
