def criar_matriz():
    m=int(input(print("Sua matriz possui quantas linhas? ")))
    n=int(input(print("Sua matriz possui quantas colunas? ")))
    mat=[]
    for i in range(m):
        linha=[]
        for j in range(n):
            a = float(input(print("Qual o elemento da {0}° linha {1}° coluna? ".format(i,j))))
            lista.append(a)
        mat.append(linha)
    
    print("Sua matriz é")
    for f in range(len(mat)):
        print(mat[f])
        
    resp = input(print("Se sua matriz estiver certa, digite 1, se estiver errada, digite 2"))
    
    if resp == 1 :
        print("Tudo bem")
        sal = input(print("Digite 1 para salvar sua matriz ou digite 2 para retornar ao menu inicial. "))
        if sal == 1:
            salvarmatriz(mat):
            return menu()
        
        
    if resp == 2 :
        print("Tudo bem")          
        return menu()
        
def criar_identidade():
    n=int(input(print("Qual é a ordem da sua matriz identidade? ")))        
    ide =[]

    for i in range(n):
      linha=[]
      for j in range (n):
        if i == j:
          p = 1
        else:
          p = 0
        linha.append(p)
      ide.append(linha)

    for i in range (len(ide)):
        print(ide[i])










x = [7,7,[1,2,3],[4,5,6],[7,8,9]]

m = int(x[1])
n = int(x[2])
MAT = []
g = int(input(print('primeira coluna')))
if g<1 or g
f = int(input(print('segunda coluna')))
for i in range(n):
    linha=[]
    if i == (g-1):
        for j in range (n):
            if j == (f-1):
                p = 1
            else:
                p = 0
            linha.append(p)
            
    elif i == (f-1):
        for j in range (n):
            if j == (g-1):
                p = 1
            else:
                p = 0
            linha.append(p)
    else:
        for j in range (n):
            if j == i:
                p = 1
            else:
                p = 0
            linha.append(p)
    MAT.append(linha)

for i in range (len(MAT)):
    print(MAT[i])




x = ['2',2,4,[1,2,1,2],[2,1,2,1]]
y = ['1',4,2,[2,1,],[1,2],[2,1],[1,2]]

m = int(x[1])
n = int(y[2])
k = int(x[2])

MAT = []

for i in range (m):
    linha = []
    for j in range (n):
        soma=0
        for l in range(k):
            soma += int(x[i+3][l])*int(y[l+3][j])
        linha.append(soma)
    MAT.append(linha)


https://github.com/Igor-Torres/calculadora/blob/master/calculadora%20matricial.py