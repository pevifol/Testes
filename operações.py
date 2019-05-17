 def soma_subt(x,y,z):
        m = int(len(x))
        n = int(len(x[0]))
        mat = []
            for i in range (m):                          
                linha=[]
                for j in range (n):  
                    if z == 1:
                        som = float(x[i][j]) + float(y[i][j])
                        linha.append(som)
                    if z == 2:
                        som = float(x[i][j]) - float(y[i][j])
                        linha.append(som)
                mat.append(linha)
        
        return resultado(mat)             
----------------------------------------------------------------------------------------------------------------
def multi_mat(x,y):
    m = int(len(x))
    n = int(len(y[0]))
    k = int(len(y))
    mat = []
    for i in range (m):
        linha=[]
        for j in range (n):
            elem = 0
            for l in range(k):
                elem += float(x[i][l])*float(y[l][j])
                linha.append(elem)
        mat.append(linha)    
    
    return resultado(mat)
---------------------------------------------------------------------------------------------------------------
def som_lin_col(x,y):
        m = int(len(x))
        n = m
        per = []
        if y == 4:
            pa = 'linha'
        else:
            pa = 'coluna'
            
        l1 = int(input(print('Digite o numero da {} que em que o resultado permanecera. '.format(pa))))
        l2 = int(input(print('Digite o numero da {} que você somara a linha escolhida a cima. '.format(pa))))
        for i in range(n):
            linha=[]
            if i == (l1-1):
                for j in range (n):
                    if j == (l1-1) or j == (l2-1):
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
            per.append(linha)
           
        if y == 4:
            return multi_mat(per,x)
        else:
            return multi_mat(x,per)
--------------------------------------------------------------------------------------------------------------------
def per_lin_col(x,y):
        per = []
        if y == 6:
            pa = 'linha'
            m = int(len(x))
            n = m
        else:
            pa = 'coluna'
            m = int(len(x[0]))
            n = m
            
        l1 = int(input(print('Digite o numero de uma das {}s que você quer permutar. '.format(pa))))
        l2 = int(input(print('Digite o numero da outra {} que você quer permutar. '.format(pa))))
        for i in range(n):
            linha=[]
            if i == (l1-1):
                for j in range (n):
                    if j == (l2-1):
                        p = 1
                    else:
                        p = 0
                    linha.append(p)
            
            elif i == (l2-1):
                for j in range (n):
                    if j == (l1-1):
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
            per.append(linha)
           
        if y == 6:
            return multi_mat(per,x)
        else:
            return multi_mat(x,per) 
----------------------------------------------------------------------------------------------------------------
def transpor(x):
    m = int(len(x[0]))
    n = int(len(x))                   
    mat = []
    
    for i in range (m):                          
        linha=[]
        for j in range (n):
            troc = x[j][i]
            linha.append(troc)
        mat.append(troc)
        
   return resultado(mat)
---------------------------------------------------------------------------------------------------------------
def multi_esc(x):
    k=int(input('Digite o valor pelo qual deseja que a matriz seja multiplicada. '))
    m = int(len(x))
    n = int(len(x[0]))                   
    mat = []
    
    for i in range (m):                          
        linha=[]
        for j in range (n):
            multi = x[i][j]*k
            linha.append(multi)
        mat.append(linha)
        
   return resultado(mat)
----------------------------------------------------------------------------------------------------------------
def multi_lin_col_esc(x,y):
    mat = []
    if y == 10:
        pa = 'linha'
        m = int(len(x))
        n = m
    else:
        pa = 'coluna'
        m = int(len(x[0]))
        n = m
    k=int(input('Digite o valor pelo qual deseja que a {} da matriz seja multiplicada. '.format(pa)))
    l1 = int(input(print('Digite o numero da {0} que você quer multiplicar por {1}. '.format(pa,k))))
    for i in range(n):
        linha=[]
        if i == (l1-1):
            for j in range (n):
                if i == j:
                    p = k
                else:
                    p = 0
        else: 
            for j in range (n):
                if j == i:
                    p = 1
                else:
                    p = 0
            linha.append(p)   
        mat.append(linha)
    
    if y == 6:
        return multi_lin_col_esc(mat,x)
    else:
        return multi_lin_col_esc(x,mat) 
-----------------------------------------------------------------------------------------------------------------
def inversão(x):


