Quanto à manipulação com a Lista de Matrizes, o programa deverá permitir, via menu:

1 – Imprimir uma, ou mais, matrizes da lista.
2 – Inserir uma nova matriz lida do teclado ou de um arquivo que contenha somente uma matriz.
3 – Inserir uma matriz identidade n x n.
4 – Alterar ou remover uma, ou mais matrizes da lista.
5 –  Apresentar a lista de matrizes com a identificação por um nome dado pelo usuário quando de sua criação.
6 – Gravar a lista com um nome diferente (backup).
7 – Ler uma outra lista de matrizes, acrescentando à lista existente, ou a substituindo.
8 – Zerar a lista de matrizes.


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
