#Exercicio 1, a-Como criar uma matriz com nl linhas e nc colunas, preenchida com algum valor?
#Dados: mat � matriz, linha � vetor, nl, nc, x, i e j s�o inteiros
#bloco:
mat=[]
nl=int(input("digite o n�mero de linhas da matriz:"))
nc=int(input("digite o n�mero de colunas da matriz:"))
x=int(input("digite o valor com o qual a matriz sera preenchida:"))
def criamatriz(nl, nc, x, mat):
    i=0
    j=0
    while i<nl:
        linha=[]
        while j<nc:
            linha.append(x)
            j=j+1
        mat.append(linha)
        i=i+1
        j=0
    return(mat)
criamatriz(nl, nc, x, mat)
print(mat)

#Exerc�cio 1, b-Como criar matriz identidade com n linhas e n colunas
#Dados: mati � matriz, linha � vetor, n, i e j s�o inteiros
#bloco:
mati=[]
n=int(input("digite o numero de linhas e colunas da matriz identidade:"))
def criamatrizidentidade(n,mati):
    i=0
    j=0
    while i<n:
        linha=[]
        while j<n:
            if i==j:
                linha.append(1)
            else:
                linha.append(0)
            j=j+1
        mati.append(linha)
        i=i+1
        j=0
    return(mati)
criamatrizidentidade(n,mati)
print(mati)

#Exercicio 2-Mostrando matriz na tela na forma de matriz
#Dados: mati � matriz
#bloco:
def mostra(mati):
    i=0
    while i<len(mati):
        print(mati[i])
        i=i+1
mostra(mati)

#Exercicio 3-Calculando a m�dia dos elementos de uma matriz
#Dados:mat � matriz, vet � vetor, i, soma, j, s, mlin, med s�o inteiros
#bloco:
def media(mat):
    i=0
    soma=0
    while i<len(mat):
        j=0
        s=0
        vet=mat[i]
        while j<len(vet):
            s=s+vet[j]
            j=j+1
        mlin=s/len(vet)
        soma=soma+mlin
        i=i+1
    med=soma/len(mat)
    return(med)
media(mat)
print(media) #deu errado, n�o consegui achar o erro, tentei varias coisas, mas n�o deu.

#Exercicio 5, a-Somando duas matrizes
#Dados: m1,m2,matriz_soma s�o matrizes
#bloco:
def somar(m1, m2):
    matriz_soma=[]
    quant_linhas=len(m1)
    quant_colunas=len(m1[0])
    i=0
        while i<quant_linhas:
            matriz_soma.append([])
            j=0
            while j<quant_colunas:
                soma = m1[i][j] + m2[i][j]
                matriz_soma[i].append(soma)
                j=j+1
    return matriz_soma