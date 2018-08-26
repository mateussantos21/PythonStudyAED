#Lista de Exercícios 8: Comparação do tempo de ordenação de algoritmos de ordenação com 4 métodos diferentes.
#1: definindo as funções para cada método:
import random;    #importando função para emparalhar os vetores posteriormente
import time;    #importando funções para medir os tempos posteriormente
#definindo função para o método bolha
def bolha(vet):
    n = len(vet)
    y=0
    while y<(n-1):
        trocou=False
        x=0
        i=0
        while x<(n-y-1):
            if vet[x]>vet[x+1]:
                trocou=True
                vet[x],vet[x+1]=vet[x+1],vet[x]
            x=x+1
        if trocou==False:
            n=1
        y=y+1
    return(vet)
#definindo função para método ruinzão
def ruinzao(vet):   
    n=len(vet)
    i=0
    while i<(n-1):
        j=i+1
        while j<n:
            if vet[i]>vet[j]:
                vet[i],vet[j]=vet[j],vet[i]
            j=j+1
        i=i+1
    return(vet)
#definindo função para método da seleção
def selecao(vet):
    n=len(vet)
    i=0
    while i<n:
        menor=vet[i]
        posmenor=i
        j=i
        while j<n:
            if vet[j]<menor:
                menor=vet[j]
                posmenor=j
            j=j+1
        aux=vet[i]
        vet[i]=menor
        vet[posmenor]=aux
        i=i+1
    return(vet)
                
                
        
#definindo função para o método do intervalo
def intervalo(vet):
    n=len(vet)
    gap=n//2
    endgap=False
    while endgap==False:
        if gap>1:
            i=0
            while i<gap:
                x=i+gap
                if vet[i]>vet[x]:
                    vet[i],vet[x]=vet[x],vet[i]
                i=i+1
            gap=gap//2
        else:
            endgap=True
    y=0
    while y<(n-1):
        trocou=False
        x=0
        i=0
        while x<(n-y-1):
            if vet[x]>vet[x+1]:
                trocou=True
                vet[x],vet[x+1]=vet[x+1],vet[x]
                x=x+1
            else:
                x=x+1
        if trocou==False:
            n=1
        y=y+1
    return(vet)

#criando os 3 vetores a serem usados nas comparações:
#Dados:n é real, vetor1, vetor2, vetor3 são vetores, i é contador

#vetor de 10000
n=10000
vetor1=[]
i=1
while i<=n:
    vetor1.append(float(i))
    i=i+1
random.shuffle(vetor1)
#vetor de 20000
n=20000
vetor2=[]
i=1
while i<=n:
    vetor2.append(float(i))
    i=i+1
random.shuffle(vetor2)
#vetor de 40000
n=40000
vetor3=[]
i=1
while i<=n:
    vetor3.append(float(i))
    i=i+1
random.shuffle(vetor3)

#exercício 2: comparando os tempos
#Dados: t1, t2, tempos 1,2,3,4,5,6,7,8,9 são reais. Vetores 1,2 e 3 são vetores de reais.
#medindo tempos da função bolha:

t1=time.time()
bolha(vetor1)
t2=time.time()
tempo1=t2-t1


t1=time.time()
bolha(vetor2)
t2=time.time()
tempo2=t2-t1


t1=time.time()
bolha(vetor3)
t2=time.time()
tempo3=t2-t1


#medindo tempos da funçao ruinzao:

t1=time.time()
ruinzao(vetor1)
t2=time.time()
tempo10=t2-t1


t1=time.time()
ruinzao(vetor2)
t2=time.time()
tempo11=t2-t1


t1=time.time()
ruinzao(vetor3)
t2=time.time()
tempo12=t2-t1


#medindo tempos da função seleção:
t1=time.time()
selecao(vetor1)
t2=time.time()
tempo4=t2-t1


t1=time.time()
selecao(vetor2)
t2=time.time()
tempo5=t2-t1


t1=time.time()
selecao(vetor3)
t2=time.time()
tempo6=t2-t1


#medindo tempos da função intervalo:
t1=time.time()
intervalo(vetor1)
t2=time.time()
tempo7=t2-t1

t1=time.time()
intervalo(vetor2)
t2=time.time()
tempo8=t2-t1

t1=time.time()
intervalo(vetor3)
t2=time.time()
tempo9=t2-t1

#exercicio 3: mostrando os tempos obtidos e tirando conclusões:

print("Vetor de 10000 números reais;")
print("Método bolha: %.3f"%tempo1)
print("Método ruinzão: %.3f"%tempo10)
print("Método seleção: %.3f"%tempo4)
print("Método intervalo: %.3f"%tempo7)
print("Vetor de 20000 números reais;")
print("Método bolha: %.3f"%tempo2)
print("Método ruinzão: %.3f"%tempo11)
print("Método seleção: %.3f"%tempo5)
print("Método intervalo: %.3f"%tempo8)
print("Vetor de 40000 números reais;")
print("Método bolha: %.3f"%tempo3)
print("Método ruinzão: %.3f"%tempo12)
print("Método seleção: %.3f"%tempo6)
print("Método intervalo: %.3f"%tempo9)
print("Pode-se perceber que o método mais lento é o da bolha, o método ruinzão e de seleção obtiveram tempos bem próximos, e o mais rápido foi o do intervalo, executando a ordenação dos tres vetores em frações de segundo.")
