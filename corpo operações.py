def escolher(x):
    if x > 0 and x < 4:
        a = int(input(print("Digite 1 para escolher matriz 1 da memoria ou\n digite 2 para digitar matriz 1. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para escolher matriz 1 da memoria ou\n digite 2 para digitar matriz 1. ")))
        if a == 1:
            mat1 = lermatriz()
        else:
            mat1 = matriz_criar()

        a = int(input(print("Digite 1 para escolher matriz 2 da memoria ou\n digite 2 para digitar matriz 2. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
            print("Essa opção não é valida, tenta de novo ai")
            a = int(input(print("Digite 1 para escolher matriz 2 da memoria ou\n digite 2 para digitar matriz 2. ")))
        if a == 1:
            mat2 = lermatriz()
        else:
            mat2 = matriz_criar()

        if x == 1 or x == 2:
            if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
                print('Impossível realizar operação, pois suas matrizes não possuem o mesmo número de linhas ou colunas.')
                a = input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = [mat1,mat2]

        else:
            if len(mat1[0])!=len(mat2):
                print('Impossível realizar operação,pois a matriz 1 não possui o\n numero de colunas igual ao numero de linhas da matriz 2.')
                a = input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outras matrizes ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = [mat1,mat2]
                
        return (final)

    elif x > 3 and x < 8:
        a = int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        if a == 1:
            mat1 = lermatriz()
        else:
            mat1 = matriz_criar()

        if x == 4 or x == 6:
            if len(mat1) < 2:
                print('Impossível realizar operação, pois suas matriz não possui linhas suficientes. ')
                a = input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = mat1

        else:
            if len(mat1[0]) < 2:
                print('Impossível realizar operação, pois suas matriz não possui colunas suficientes. ')
                a = input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. "))
                while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida ( é o unico jeito que eu sei )
                    print("Essa opção não é valida, tenta de novo ai")
                    a = int(input(print("Digite 1 para escolher outra matriz ou digite 2 para retornar ao menu inicial. ")))
                if a == 1:
                    final = escolhe(x)
                else:
                    return menu()
            else:
                final = mat1
                
        return (final)

    else:
        a = int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para escolher matriz da memoria ou\n digite 2 para digitar matriz. ")))
        if a == 1:
            mat1 = lermatriz()
        else:
            mat1 = matriz_criar()

        return (final)

----------------------------------------------------------------------------------------------------------------------------
def resultado(x):
    
    print("O resultado é\n")
    print("+-"," "*(7*len(x[0])-2),"-+")
    for i in range (len(x)):
        print("| ",end="")
        for j in range (len(x[0])):
            print(" {0:^5} ".format(x[i][j]),end="")

        print(" |")
    print("+-"," "*(7*len(x[0])-2),"-+")

    sal = input(print("Digite 1 para salvar o resultado \nDigite 2 para retornar ao menu de operações ou \nDigite 3 para retornar ao menu inicial. "))
        while sal!=1 and sal!=2 and sal!=3:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            sal = int(input(print("Digite 1 para salvar o resultado \nDigite 2 para retornar ao menu de operações ou \nDigite 3 para retornar ao menu inicial. ")))
    if sal == 1:
        salvarmatriz(x):
        return menu()
    
    elif sal == 2:
        return operações()
    else:
        return menu()

---------------------------------------------------------------------------------------------------------------------------

def operações():
    print("+","-"*39,"+")  
    print("|  1 – Soma Matricial                     |")
    print("|  2 – Subtração Matricial                |")
    print("|  3 – Multiplicação Matricial            |")
    print("|  4 – Somar Linhas da Matriz             |")
    print("|  5 – Somar Colunas da Matriz            |")
    print("|  6 – Permutar Linhas                    |")
    print("|  7 – Permutar Colunas                   |")
    print("|  8 – Transposição de Matriz             |")
    print("|  9 – Multiplicação por Escalar          |")
    print("| 10 – Multiplicar Linha por Escalar      |")
    print("| 11 – Multiplicar Coluna por Escalar     |")
    print("| 12 – Inversão de matrizes quadradas 2x2 |")
    print("+","-"*39,"+")

    opção = int(input(print("Digite o numero da operação que você deseja realizar. ")))
    if opção < 1 or opção > 12: # serve para se a opção digitada não for valida
        print("Essa opção não é valida")
        a = input(print("Digite 1 para tentar escolher novamente ou digite 2 \n para voltar ao menu inicial. "))
        while a!=1 and a!=2:# aqui é pra garantir que digite uma opção valida
            print("Essa opção não é valida, tenta de novo ai")
            a= int(input(print("Digite 1 para tentar escolher novamente ou \ndigite 2 para voltar ao menu inicial. ")))
            
        if a == 1:
            return operações()
        else:
            return menu()
    else:# Aqui de acordo com a opção escolhida, o bagulho vai mandar pra uma função que
         # seleciona as matrizes da operação e depois vai devolver aqui pra operação rolar


        if opção == 1 or opção == 2:
            mz = escolher(opção)
            return soma_subt(mz[0],mz[1],opção)

        elif opção == 3:
            mz = escolher(opção)
            return multi_mat(mz[0],mz[1])

        elif opção == 4 or opção == 5:
            mz = escolher(opção)
            return som_lin_col(mz,opção)


        elif opção == 6 or opção == 7:
            mz = escolher(opção)
            return per_lin_col(mz,opção)


        elif opção == 8:
            mz = escolher(opção)
            return transpor(mz)

        elif opção == 9:
            mz = escolher(opção)
            return multi_esc(mz)

        elif opção == 10 or opção == 11:
            mz = escolher(opção)
            return multi_lin_col_esc(mz,opção)

        else:
            mz = escolher(opção)
            return inversão(mz)
