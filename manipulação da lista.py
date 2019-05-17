#--NÃO FAÇO IDEIA DE COMO CONTRUIR ESSE MENU, SÓ FIZ O PRINT E ALGUMAS FUNÇÕES DAS OPÕES NELE, TIPO A IDENTIDADE E A CRIAR MATRIZ----
def list_matriz():
    print("+","-"*19,"Lista de Matrizes","-"*20,"+")  
    print("|                                                            |")
    print("|  1 – Imprimir Matriz da Lista.                             |")
    print("|  2 – Inserir uma Nova Matriz                               |")
    print("|  3 – Inserir uma Matriz Identidade                         |")
    print("|  4 – Alterar ou Remover Matrizes da Lista.                 |")
    print("|  5 – Apresentar a Lista de Matrizes                        |")
    print("|  6 – Gravar a Lista com um Nome Diferente (backup).        |")
    print("|  7 – Acrescentar Nova Lista de Matrizes a Lista Existente. |")
    print("|  8 – Substituir a Lista de Matriz Existente                |")
    print("|  9 – Zerar a Lista de Matrizes Existente.                  |")
    print("|                                                            |")
    print("+","-"*58,"+")
    

#-----------------------------NÃO CRIEI PORQUE NÃO SEI MANUPULAR A LISTA---------------------------------------
def printmatriz(): 

    
#-----------------------------BOTA NOVA MATRIZ DO TECLADO------------------------------------------------
def criar_matriz():
    m=int(input(print("Sua matriz possui quantas linhas? ")))
    n=int(input(print("Sua matriz possui quantas colunas? ")))
    mat=[]
    for i in range(m):
        linha=[]
        for j in range(n):
            a = float(input(print("Qual o elemento da {0}° linha, {1}° coluna? ".format(i,j))))
            lista.append(a)
        mat.append(linha)
    
    print("Sua matriz é")
    print()
    print("+-"," "*(7*len(mat[0])-2),"-+")
    for i in range (len(mat)):
        print("| ",end="")
        for j in range (len(mat[0])):
            print(" {0:^5} ".format(x[i][j]),end="")

        print(" |")
    print("+-"," "*(7*len(mat[0])-2),"-+")
    
    resp = input(print("Digite 1 para salvar o resultado \nDigite 2 para criar a matriz novamente ou \nDigite 3 para retornar ao menu inicial. "))
    while resp!=1 and resp!=2 and resp!=3:# aqui é pra garantir que digite uma opção valida
        print("Essa opção não é valida, tenta de novo ai")
        resp = int(input(print("Digite 1 para salvar o resultado \nDigite 2 para criar a matriz novamente ou \nDigite 3 para retornar ao menu inicial. ")))
    if resp == 1 :
        print("Tudo bem")
        salvarmatriz(mat)
        return menu()
                
    if resp == 2 :
        print("Tudo bem")
        return criar_matriz()
    
    else:
        return menu()

#---------------------------------------------CRIA A MATRIZ IDENTIDADE NxN--------------------------------------------
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

    print("Sua matriz é")
    print()
    print("+-"," "*(7*len(ide[0])-2),"-+")
    for i in range (len(ide)):
        print("| ",end="")
        for j in range (len(ide[0])):
            print(" {0:^5} ".format(x[i][j]),end="")

        print(" |")
    print("+-"," "*(7*len(ide[0])-2),"-+")
    
    resp = input(print("Digite 1 para salvar o resultado \nDigite 2 para criar a matriz novamente ou \nDigite 3 para retornar ao menu inicial. "))
    while resp!=1 and resp!=2 and resp!=3:# aqui é pra garantir que digite uma opção valida
        print("Essa opção não é valida, tenta de novo ai")
        resp = int(input(print("Digite 1 para salvar o resultado \nDigite 2 para criar a matriz novamente ou \nDigite 3 para retornar ao menu inicial. ")))
    if resp == 1 :
        print("Tudo bem")
        salvarmatriz(ide):
        return menu()
                
    if resp == 2 :
        print("Tudo bem")
        return criar_identidade()  
        
    else:
        return menu()
 
#--------DAQUI PRA BAIXO TAMBÉM NÃO FIZ PORRA NENHUMA PORQUE EU NÃO SEI MANIPULAR A LISTA, PORÉM SERIAM AS FUNÇÕES 4,5,6,7,8,9--------





