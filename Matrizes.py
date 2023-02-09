import os
from math import cos, sin, radians as rad
from fractions import Fraction as frac
from random import choice
os.system('color 1')

versao = '3.0'
banco_de_matriz = []
banco_de_vetores = []
comandos = '''
(A) para adicionar matriz
(S) para substituir valor
(D) para calcular determinante
(G) para escalonar
(C) para somar
(M) para multiplicar
(R) para resolução de sistema
(T) para transposta
-----------------------------------
(B) para mostrar banco de matrizes
(L) para limpar banco
(V) para área de vetores
(E) para sair

Comando:'''
comandosV = '''
(A) para adicionar vetor
(Ro) para rotação
(Re) para reflexão
(T) para transposição
(P) para projeção
(C) para cisalhamento
-----------------------------------
(B) para mostrar banco de vetores
(L) para limpar banco
(M) para área de matrizes
(E) para sair

Comando:'''
intro = '--------------------\nSuper programa de peripércias com matrizes  V{}\n--------------------'.format(versao)
entry = ''
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
askV = '''
(2) Vetor 2D
(3) Vetor 3D

Input:'''
#Acabaram as variáveis

#To do
'''
Reduzir passos do método Gaussiano
'''

# Funções do 2048
def Show2048(x):
    print()
    lin, col = len(x), len(x[0])
    for i in range(lin):
        for j in range(col):
            value = x[i][j]
            space = (4-len(str(value)))*" "
            print(f"{space}{value}", end="|")
        print()

def VerifyFree(grid):
    free = []
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                free.append([i, j])
    return free
                
def Move(axis, direction):
    if axis == 'h':
        if direction in 'aA':
            x = -1
        if direction in 'dD':
            x = 0

        for i in range(grid_size):
            for k in range(grid_size):
                for j in range(grid_size-1):
                    if grid[i][j+(1+x)] == 0 and grid[i][j-x] != 0:
                        grid[i][j+(1+x)], grid[i][j-x] = grid[i][j-x], grid[i][j+(1+x)]

    if axis == 'v':
        if direction in 'wW':
            x = -1
        if direction in 'sS':
            x = 0

        for k in range(grid_size):
            for i in range(grid_size-1):
                for j in range(grid_size):
                    if grid[i+(1+x)][j] == 0 and grid[i-x][j] != 0:
                        grid[i+(1+x)][j], grid[i-x][j] = grid[i-x][j], grid[i+(1+x)][j]

def Fuse(axis, direction):
    if axis == 'h':
        if direction in 'aA':
            x = -1
        if direction in 'dD':
            x = 0

        for i in range(grid_size):
            for k in range(grid_size):
                for j in range(grid_size-1):
                    if grid[i][j+(1+x)] == grid[i][j-x]:
                        grid[i][j+(1+x)], grid[i][j-x] = grid[i][j-x]+grid[i][j+(1+x)], 0

    if axis == 'v':
        if direction in 'wW':
            x = -1
        if direction in 'sS':
            x = 0

        for k in range(grid_size):
            for i in range(grid_size-1):
                for j in range(grid_size):
                    if grid[i+(1+x)][j] == grid[i-x][j]:
                        grid[i+(1+x)][j], grid[i-x][j] = grid[i-x][j]+grid[i+(1+x)][j], 0

def Win(grid):
    for i in grid:
        if 2048 in i:
            return True
    return False

# Funções de utilidade
def Remove():
    return []

def Compare(ent,str):
    if ent == str or ent == str.lower():
        return True
    else:
        return False

def CompareSegment(ent,str):
    for i in str:
        if Compare(ent,i):
            return True
    return False

def SetIntro(string):
    os.system('cls')
    print(intro)
    if string != 0:
        print('\n{}\n------------------'.format(string))

def IsLadder(matriz):
    min_pivo = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #Achar o pivô
            if matriz[i][j] != 0:
                #Verificar o minimo para o pivô
                if j < min_pivo:
                    return False
                min_pivo = j+1
                #Verificar números se todos abaixo são 0
                for k in range(i+1, len(matriz)):
                    if matriz[k][j] != 0:
                        return False
                #Sair depois de encontrar pivô
                break
    #Se nada deu errado, ela é escada
    return True

def Purify(linha):
    for i in range(len(linha)):
        if linha[i] == -0:
            linha[i] = 0

def Aproximate(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]%1 == 0 or matriz[i][j]%1 == -0:
                matriz[i][j] = int(matriz[i][j])
            else:
                matriz[i][j] = round(matriz[i][j],3)
                if matriz[i][j]%1 == 0 or matriz[i][j]%1 == -0:
                    matriz[i][j] = int(matriz[i][j])

def CopyMatrix(matriz):
    copy = []
    for i in range(len(matriz)):
        copy.append([])
        for j in range(len(matriz[i])):
            copy[i].append(matriz[i][j])
    return copy

def Get(string):
    try:
        return int(input(string))
    except:
        print('Input inválido')
        return 'Error'

def ShowUnit(matriz):
    show, show_size = [], 1

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            check = len(str(matriz[i][j]))
            if check > show_size:
                show_size = check

    for linha in matriz:
        show.append(str(i) + (show_size-len(str(i)))*" " for i in linha)
    
    for linha in show:
        print('[' + ' '.join(map(str, linha)) + ']')

def GenSyst(matriz):
    equals = [0 for i in range(len(matriz[0]))]
    eqLine = [[] for i in range(len(matriz))]

    for i in range(len(eqLine)):
        for j in range(len(equals)):
            eqLine[i].append('{}{}'.format(matriz[i][j], letters[j]))

    for i in range(len(eqLine)):
        getting = True
        while getting:
            try:
                equals[i] = frac(str(input(' + '.join(eqLine[i]) + ' = ')))
                getting = False
            except:
                pass

    return equals

def SetColor(string):
    color_codes = ['1','2','3','4','5','6','7','8','d']
    color_names = ['blue','green','cian','red','purple','yellow','white','grey','pink']
    try:
        os.system(f'color {color_codes[color_names.index(string)]}')
    except:
        pass

def ShowBank(bank, element):
    for el in range(len(bank)):
        print(f'{element}:{el+1}')
        ShowUnit(bank[el])
        print()

def Find(n, format, element, bank):
    if n != 'Error':
        try:
            exit_code = bank[n-1]
            ShowUnit(bank[n-1])
            return True
        except:
            input(f'\n{element} não existe\n')
            SetIntro(f'{format}')
            return False

# Funcões de matrizes
def Sub(matriz, i, j, valor):
    matriz[i][j] = valor

def Adicionar(code,bank):
    if code == 0:
        while True:
            try:
                lin = int(input("Linhas da matriz: "))
                col = int(input("Colunas da matriz: "))
                if lin > 0 and col > 0:
                    break
                else:
                    print('\nLinhas e/ou colunas inválidas\n')
            except:
                print('\nLinhas e/ou colunas inválidas\n')
        matriz = [[] for i in range(lin)]
        for i in range(lin):
            j = 0
            while j < col:
                try:
                    matriz[i].append(frac(str(input("Termo {}x{}:".format(i+1, j+1)))))
                    j += 1
                except:
                    print('Valor inválido')
        SetIntro("Adicionar Matriz:")
        print('Matriz adicionada:\n')
        ShowUnit(matriz)
        bank.append(matriz)
    else:
        bank.append(code)

def Gauss(matriz_ref, code, typo, skip):
    matriz = CopyMatrix(matriz_ref)
    lin, col = len(matriz), len(matriz[0])
    z = 1

    if code == 'Det':
        z = -1
        if lin!=col:
            return "\nNão é possível calcular o determinante"
        elif lin == 1:
            return f'\nDeterminante = {matriz[0][0]}'
        elif lin == 2:
            p1, p2, f1, f2 = matriz[0][0], matriz[1][1], matriz[0][1], matriz[1][0]
            return f'\nDeterminante = {p1} * {p2} - {f1} * {f2} = {p1 * p2 - f1 * f2}'

    while(IsLadder(matriz) == False):
        for i in range(lin-1):
            for j in range(col):
                #Caso o valor embaixo seja 0:
                if matriz[i][j] == 0 and matriz[i+1][j] != 0:
                    matriz[i], matriz[i+1] = matriz[i+1], [z*n for n in matriz[i]]
                    Purify(matriz[i+1])
                    break
                #Caso não seja:
                elif matriz[i][j] != 0 and matriz[i+1][j] != 0:
                    a, b = matriz[i+1][j], matriz[i][j]
                    for k in range(col):
                        matriz[i+1][k] = frac(str(matriz[i+1][k]-(matriz[i][k]*a/b)))
                    Purify(matriz[i+1])
                    break

            #Verificar se ela chegou no formato escada
            if IsLadder(matriz):
                break
        
            if skip == False:
                ShowUnit(matriz)
                print()
                input('Próximo passo')
                SetIntro(typo)

    return matriz

def Multiplicar(X,Y):
    col = len(X[0])
    lin = len(Y)

    if col != lin :
        return "\nNão é possivel multiplicar!"
    
    line = len(X)
    column = len(Y[0])

    result =[[0 for x in range(column)] for y in range(line)]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result

def Solve(matriz_ref, syst):
    matriz = CopyMatrix(matriz_ref)
    for i in range(len(matriz)):
        matriz[i].append(syst[i])
    
    ShowUnit(matriz)
    select = input('\nEnter para passo a passo, (P) para pular: ')
    skip = False
    if select == 'P' or select == 'p':
        skip = True
    SetIntro('Resolver sistema:')
    matriz = Gauss(matriz, '', 'Resolver sistema:', skip)

    if skip == False:
        ShowUnit(matriz)
        input('\nProximo passo')
        SetIntro('Resolver sistema:')
    
    for i in range(len(matriz)):
        matriz[i] = [frac(str(n/matriz[i][i])) for n in matriz[i]]

    if skip == False:
        ShowUnit(matriz)
        input('\nProximo passo')
        SetIntro('Resolver sistema:')
    
    for i in range(1, len(matriz)):
        jmp = 1
        for j in range(i, 0, -1):
            cort = matriz[i-jmp][i]
            jmp += 1
            for k in range(i, len(matriz[0])):
                matriz[j-1][k] = matriz[j-1][k] - (matriz[i][k] * cort)
            if skip == False:
                ShowUnit(matriz)
                input('\nProximo passo')
                SetIntro('Resolver sistema:')
    
    return matriz

def Sum(X,Y):
    lin_X, lin_Y = len(X), len(Y)
    col_X, col_Y = len(X[0]), len(Y[0])

    if lin_X != lin_Y or col_X != col_Y:
        return '\nNão é possível somar'
    
    result = []
    for i in range(lin_X):
        result.append([])
        for j in range(col_X):
            result[i].append(X[i][j]+Y[i][j])
    return result

def Trans(matriz):
    lin, col = len(matriz), len(matriz[0])
    result = [[0 for j in range(lin)] for i in range(col)]
    
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matriz[j][i]
    
    return result

# Funções de vetores
def AddVector(dim):
    direct = ["x","y","z"]
    vector = [[] for i in range(dim)]
    i = 0
    while i < len(vector):
        try:
            new_value = frac(str(input("{}:".format(direct[i]))))
            if '/' in str(new_value):
                new_value = float(round(new_value,2))
            vector[i].append(new_value)
            i += 1
        except:
            print("Input inválido")
    SetIntro("Adicionar Vetor:")
    print('Vetor adicionado:\n')
    ShowUnit(vector)
    banco_de_vetores.append(vector)
    
def Rotate2D(vector,angle):
    sub_vector = CopyMatrix(vector)
    sub_vector.append([1])
    c = cos(rad(angle))+1-1
    s = sin(rad(angle))+1-1
    mult_vector = [[c,-s,0],[s,c,0],[0,0,1]]
    result_vector = Multiplicar(mult_vector,sub_vector)
    return result_vector[:2]

def Rotate3D(vector,angle,eixo):
    sub_vector = CopyMatrix(vector)
    sub_vector.append([1])
    c = cos(rad(angle))+1-1
    s = sin(rad(angle))+1-1
    if Compare(eixo,"X"):
        mult_vector = [[1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1]]
    elif Compare(eixo,"Y"):
        mult_vector = [[c,0,s,0],[0,1,0,0],[-s,0,c,0],[0,0,0,1]]
    elif Compare(eixo,"Z"):
        mult_vector = [[c,-s,0,0],[s,c,0,0],[0,0,1,0],[0,0,0,1]]
    
    result_vector = Multiplicar(mult_vector,sub_vector)
    return result_vector[:3]

def Translacao2D(vector,dx,dy):
        sub_vector = CopyMatrix(vector)
        sub_vector.append([1])
        idTranslacao = [[1,0,dx],[0,1,dy],[0,0,1]]
        translacao = [[],[],[]]

        somat=0
        for i in range(3):
            for k in range(3):
                somat+=idTranslacao[i][k]*sub_vector[k][0]
            translacao[i].append(somat)
            somat=0
                 
        return translacao[:2]

def Translacao3D(vector,dx,dy,dz):
        sub_vector = CopyMatrix(vector)
        sub_vector.append([1])
        idTranslacao = [[1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]]
        translacao = [[],[],[],[]]

        somat=0
        for i in range(4):
            for k in range(4):
                somat+=idTranslacao[i][k]*sub_vector[k][0]
            translacao[i].append(somat)
            somat=0

        return translacao[:3]

def Reflect2D(vector,axis):
    if Compare(axis,"X"):
        return [[vector[0][0]],[-vector[1][0]]]
    elif Compare(axis,"Y"):
        return [[-vector[0][0]],[vector[1][0]]]

def Reflect3D(vector,axis):
    if Compare(axis,"X"):
        return [[vector[0][0]],[-vector[1][0]],[-vector[2][0]]]
    elif Compare(axis,"Y"):
        return [[-vector[0][0]],[vector[1][0]],[-vector[2][0]]]
    elif Compare(axis,"Z"):
        return [[-vector[0][0]],[-vector[1][0]],[vector[2][0]]]

def Projection2D(vector,eixo):
    if Compare(eixo,"X"):
        return [[vector[0][0]],[0]]
    elif Compare(eixo,"Y"):
        return [[0],[vector[1][0]]]

def Projection3D(vector,eixo):
    if Compare(eixo,"X"):
        return [[vector[0][0]],[0],[0]]
    elif Compare(eixo,"Y"):
        return [[0],[vector[1][0]],[0]]
    elif Compare(eixo,"Z"):
        return [[0],[0],[vector[2][0]]]

def Cisilh2D(vector,eixo,k):
    sub_vector = CopyMatrix(vector)
    sub_vector.append([1])
    if Compare(eixo,"X"):
        mult_vector = [[1,k,0],[0,1,0],[0,0,1]]
    elif Compare(eixo,"Y"):
        mult_vector = [[1,0,0],[k,1,0],[0,0,1]]
    result_vector = Multiplicar(mult_vector,sub_vector)
    return result_vector[:2]
    

#Parte da interface para o usuário:
while not Compare(entry,"E"):
    print(intro)
    entry = input(comandos)
    SetIntro(0)

    #Acesso ao banco de matrizes
    if Compare(entry,"B"):
        print('\nBanco de Matrizes:\n------------------')
        if len(banco_de_matriz) == 0:
            print('Banco vazio')
            input('\nContinuar')
        else:
            ShowBank(banco_de_matriz,"Matriz")
            input('Enter para sair do banco')

    #Acesso à adição de matrizes no banco
    elif Compare(entry,"A"):
        print('\nAdicionar Matriz:\n------------------')
        Adicionar(0,banco_de_matriz)
        input('\nContinuar')
    
    #Acesso à substituição de valor
    elif Compare(entry,"S"):
        print('\nSubstituir valor:\n------------------')
        while True:
            k = Get('Número da matriz:')
            if k == 'Error':
                SetIntro("Substituir valor:")
            if Find(k,"Substituir valor:","Matriz",banco_de_matriz):
                break
        print()
        while True:
            i = Get('Linha:')
            j = Get('Coluna:')
            if i != 'Error' and j != 'Error':
                try:
                    exit_code = banco_de_matriz[k-1][i-1][j-1]
                    break
                except:
                    print('Número de linhas e/ou colunas não encontrado')
        while True:
            v = Get('Novo valor:')
            if v != 'Error':
                break
        Sub(banco_de_matriz[k-1], i-1, j-1, v)
        print('\nNova matriz:\n')
        ShowUnit(banco_de_matriz[k-1])
        input('\nContinuar')

    #Acesso à soma de matrizes
    elif Compare(entry,"C"):
        while True:
            print('\nSoma de matrizes:\n------------------')
            if len(banco_de_matriz) < 1:
                print('\nSem matrizes o suficiente para somar :(\n')
                input('Enter para continuar')
                break
            while True:
                k = Get('Matriz 1:')
                print()
                if k == 'Error':
                    SetIntro("Soma de matrizes:")
                if Find(k,"Soma de matrizes:","Matriz",banco_de_matriz):
                    break
            while True:
                j = Get('\nMatriz 2:')
                print()
                if j == 'Error':
                    SetIntro("Soma de matrizes:")
                if Find(j,"Soma de matrizes:","Matriz",banco_de_matriz):
                    break
                else:
                    print('Matriz 1:{}\n'.format(k))
                    ShowUnit(banco_de_matriz[k-1])
            
            while True:
                conf = input('\nConfirmar soma? (S) ou (N):')
                if conf == 'S' or conf == 's' or conf == 'N' or conf == 'n':
                    break

            if conf == 'S' or conf == 's':
                result = Sum(banco_de_matriz[k-1], banco_de_matriz[j-1])
                if type(result) == str:
                    print(result)
                else:
                    print('\nMatriz resultante:')
                    ShowUnit(result)
                if type(result) != str:
                    next = input('\n(A) para adicionar a matriz ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
                    if next == 'A' or next == 'a':
                        Adicionar(result,banco_de_matriz)
                        print('\nMatriz adiconada')
                    else:
                        print('\nMatriz não adicionada')
                input('\nContinuar')
                break
            else:
                SetIntro(0)

    #Acesso ao cálculo do determinante
    elif Compare(entry,"D"):
        while True:
            print('\nCalcular determinante:\n------------------')
            if len(banco_de_matriz) == 0:
                print('\nSem matrizes para calcular :(')
                break
            while True:
                k = Get('Número da matriz:')
                print()
                if k == 'Error':
                    SetIntro("Calcular determinante:")
                if Find(k,"Calcular determinante:","Matriz",banco_de_matriz):
                    break
            while True:
                conf = input('\nConfirmar matriz? (S) ou (N):')
                if conf == 'S' or conf == 's' or conf == 'N' or conf == 'n':
                    break
            if conf == 'S' or conf == 's':
                SetIntro("Calcular determinante:")
                ShowUnit(banco_de_matriz[k-1])
                select = input('\nEnter para passo a passo, (P) para pular: ')
                skip = False
                if select == 'P' or select == 'p':
                    skip = True
                SetIntro("Calcular determinante:")
                result = Gauss(banco_de_matriz[k-1], 'Det', 'Calcular determinante:', skip)
                if type(result) == str:
                    ShowUnit(banco_de_matriz[k-1])
                    print(result)
                    break
                else:
                    SetIntro('Calcular determinante:') 
                    ShowUnit(result)
                    det, ops = 1, []
                    for i in range(len(result)):
                        det *= result[i][i]
                        ops.append(str('({})'.format(result[i][i])))
                    print('\nDeterminante = {} = {}'.format(' * '.join(ops), det))
                    break
            else:
                SetIntro(0)
        input('\nEnter para continuar')

    #Acesso à multiplicação de matrizes
    elif Compare(entry,"M"):
        while True:
            print('\nMultiplicação de matrizes:\n------------------')
            if len(banco_de_matriz) < 1:
                print('\nSem matrizes o suficiente para multiplicar :(\n')
                input('Enter para continuar')
                break
            while True:
                k = Get('Matriz 1:')
                print()
                if k == 'Error':
                    SetIntro("Multiplicação de matrizes:")
                if Find(k,"Multiplicação de matrizes:","Matriz",banco_de_matriz):
                    break
            while True:
                j = Get('\nMatriz 2:')
                print()
                if j == 'Error':
                    SetIntro("Multiplicação de matrizes:")
                if Find(j,"Multiplicação de matrizes:","Matriz",banco_de_matriz):
                    break
                else:
                    print('Matriz 1:{}\n'.format(k))
                    ShowUnit(banco_de_matriz[k-1])
            
            while True:
                conf = input('\nConfirmar multiplicação? (S) ou (N):')
                if conf == 'S' or conf == 's' or conf == 'N' or conf == 'n':
                    break

            if conf == 'S' or conf == 's':
                result = Multiplicar(banco_de_matriz[k-1], banco_de_matriz[j-1])
                if type(result) == str:
                    print(result)
                else:
                    print('\nMatriz resultante:')
                    ShowUnit(result)
                if type(result) != str:
                    next = input('\n(A) para adicionar a matriz ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
                    if next == 'A' or next == 'a':
                        Adicionar(result,banco_de_matriz)
                        print('\nMatriz adiconada')
                    else:
                        print('\nMatriz não adicionada')
                input('\nContinuar')
                break
            else:
                SetIntro(0)

    #Acesso ao escalonamento
    elif Compare(entry,"G"):
        exit = False
        while True:
            print('\nMétodo Gaussiano:\n------------------')
            if len(banco_de_matriz) == 0:
                print('\nSem matrizes para calcular :(')
                exit = True
                break
            while True:
                k = Get('Número da matriz:')
                print()
                if k == 'Error':
                    SetIntro("Método Gaussiano:")
                if Find(k,"Método Gaussiano:","Matriz",banco_de_matriz):
                    break
            while True:
                conf = input('\nConfirmar matriz? (S) ou (N):')
                if conf == 'S' or conf == 's' or conf == 'N' or conf == 'n':
                    break
            if conf == 'S' or conf == 's':
                SetIntro("Método Gaussiano:")
                ShowUnit(banco_de_matriz[k-1])
                select = input('\nEnter para passo a passo, (P) para pular: ')
                skip = False
                if select == 'P' or select == 'p':
                    skip = True
                SetIntro("Método Gaussiano:")
                result = Gauss(banco_de_matriz[k-1], 'Escal', 'Método Gaussiano:', skip)
                ShowUnit(result)
                break
            else:
                SetIntro(0)

        if not exit:
            next = input('\n(A) para adicionar a matriz ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
            if next == 'A' or next == 'a':
                Adicionar(result,banco_de_matriz)
                print('\nMatriz adiconada')
            else:
                print('\nMatriz não adiconada')

        input('\nEnter para continuar')

    #Acesso ao sistema
    elif Compare(entry,"R"):
        while True:
            print('\nResolver sistema:\n------------------')
            while True:
                k = Get('Número da matriz:')
                print()
                if k == 'Error':
                    SetIntro("Resolver sistema:")
                if Find(k,"Resolver sistema:","Matriz",banco_de_matriz):
                    break
            while True:
                conf = input('\nConfirmar matriz? (S) ou (N):')
                if conf == 'S' or conf == 's' or conf == 'N' or conf == 'n':
                    break
            if conf == 'S' or conf == 's':
                while True:
                    SetIntro('Resolver sistema:')
                    syst = GenSyst(banco_de_matriz[k-1])
                    while True:
                        conf = input('\nConfirmar sistema? (S) ou (N):')
                        if conf == 'S' or conf == 's' or conf == 'N' or conf == 'n':
                            break
                    if conf == 'S' or conf == 's':
                        SetIntro('Resolver sistema:')
                        break
                
                try:
                    if len(banco_de_matriz[k-1]) != len(banco_de_matriz[k-1][0]):
                        exit_code = 1/0
                    solved = Solve(banco_de_matriz[k-1], syst)
                    ShowUnit(solved)
                    print('\nSolução:\n')
                    for i in range(len(solved)):
                        print('{} = {}'.format(letters[i], solved[i][-1]))
                except:
                    print('\nV{} só aceita matrizes quadradas no sistema :(\nAguarde mais atualizações'.format(versao))
                break

            else:
                SetIntro(0)
        input('\nEnter para continuar')

    #Acesso à transposta
    elif Compare(entry,"T"):
        exit = False
        while True:
            print('\nTransposta:\n------------------')
            if len(banco_de_matriz) == 0:
                print('\nSem matrizes para calcular :(')
                exit = True
                break
            while True:
                k = Get('Número da matriz:')
                print()
                if k == 'Error':
                    SetIntro("Transposta:")
                if Find(k,"Transposta:","Matriz",banco_de_matriz):
                    break
            while True:
                conf = input('\nConfirmar matriz? (S) ou (N):')
                if conf == 'S' or conf == 's' or conf == 'N' or conf == 'n':
                    break
            if conf == 'S' or conf == 's':
                result = Trans(banco_de_matriz[k-1])
                print('\nMatriz transposta:\n')
                ShowUnit(result)
                break
            else:
                SetIntro(0)

        if not exit:
            next = input('\n(A) para adicionar a matriz ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
            if next == 'A' or next == 'a':
                Adicionar(result,banco_de_matriz)
                print('\nMatriz adiconada')
            else:
                print('\nMatriz não adiconada')

        input('\nEnter para continuar')

    #Limpar o banco
    elif Compare(entry,"L"):
        banco_de_matriz = []

    #Acesso aos vetores
    elif Compare(entry,"V"):
        while True:
            SetIntro(0)
            entry = input(comandosV)
            SetIntro(0)

            #Acesso ao banco de vetores
            if Compare(entry,"B"):
                print('\nBanco de Vetores:\n------------------')
                if len(banco_de_vetores) == 0:
                    print('Banco vazio')
                    input('\nContinuar')
                else:
                    ShowBank(banco_de_vetores,"Vetor")
                    input('Enter para sair do banco')
            
            #Acesso à adição de vetores no banco
            elif Compare(entry,"A"):
                SetIntro("Adicionar Vetor:")
                while True:
                    dim = input(askV)
                    if dim == '3' or dim == '2':
                        break
                    else:
                        SetIntro("Adicionar Vetor:")
                SetIntro("Adicionar Vetor:")
                AddVector(int(dim))
                input("\nContinuar")
            
            #Acesso à rotação de vetores
            elif Compare(entry,"Ro"):
                while True:
                    SetIntro("Rotação de vetor:")
                    if len(banco_de_vetores):
                        while True:
                            k = Get('Número do vetor:')
                            print()
                            if k == "Error":
                                SetIntro("Rotação de vetor:")
                            if Find(k,"Rotação de vetor:","Vetor",banco_de_vetores):
                                break
                        while True:
                            conf = input('\nConfirmar vetor? (S) ou (N):')
                            if Compare(conf,"S") or Compare(conf,"N"):
                                break
                        if Compare(conf,"S"):
                            while True:
                                angle = Get("Ângulo da rotação (anti-horário): ")
                                if angle != "Error":
                                    break
                            if len(banco_de_vetores[k-1]) == 2:
                                new_vector = Rotate2D(banco_de_vetores[k-1],angle)
                            else:
                                while True:
                                    eixo = input("Eixo a ser rotacionado: ")
                                    if Compare(eixo,"X") or Compare(eixo,"Y") or Compare(eixo,"Z"):
                                        break
                                new_vector = Rotate3D(banco_de_vetores[k-1],angle,eixo)
                            Aproximate(new_vector)
                            print()
                            ShowUnit(new_vector)
                            next = input('\n(A) para adicionar vetor ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
                            if Compare(next,"A"):
                                Adicionar(new_vector,banco_de_vetores)
                                print('\nVetor adicionado')
                            else:
                                print('\nVetor não adicionado')
                            break
                        else:
                            SetIntro(0)
                    else:
                        print("\nSem vetores para calcular :(")
                        break
                input("\nEnter para continuar")

            #Acesso à transposição de vetores
            elif Compare(entry,"T"):
                area_name = "Transposição de vetor:"
                while True:
                    SetIntro(area_name)
                    if len(banco_de_vetores):
                        while True:
                            k = Get('Número do vetor:')
                            print()
                            if k == "Error":
                                SetIntro(area_name)
                            if Find(k,area_name,"Vetor",banco_de_vetores):
                                break
                        while True:
                            conf = input('\nConfirmar vetor? (S) ou (N):')
                            if Compare(conf,"S") or Compare(conf,"N"):
                                break
                        if Compare(conf,"S"):
                            SetIntro(area_name)
                            while True:
                                dx = Get("Dx:")
                                if dx!='Error':
                                    dy = Get("Dy:")
                                    if dy!='Error':
                                        if len(banco_de_vetores[k-1]) == 2:
                                            break
                                        else:
                                            dz = Get("Dz:")
                                            if dz!='Error':
                                                break
                                SetIntro(area_name)
                            if len(banco_de_vetores[k-1]) == 2:
                                new_vector = Translacao2D(banco_de_vetores[k-1],dx,dy)
                            else:
                                new_vector = Translacao3D(banco_de_vetores[k-1],dx,dy,dz)
                            print("\nVetor transposto:\n")
                            ShowUnit(new_vector)
                            next = input('\n(A) para adicionar vetor ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
                            if Compare(next,"A"):
                                Adicionar(new_vector,banco_de_vetores)
                                print('\nVetor adicionado')
                            else:
                                print('\nVetor não adicionado')
                            break
                        else:
                            SetIntro(area_name)
                    else:
                        print("\nSem vetores para calcular :(")
                        break
                input("\nEnter para continuar")

            #Acesso à reflexão de vetores
            elif Compare(entry,"Re"):
                area_name = "Reflexão de vetor:"
                while True:
                    SetIntro(area_name)
                    if len(banco_de_vetores):
                        while True:
                            k = Get('Número do vetor:')
                            print()
                            if k == "Error":
                                SetIntro(area_name)
                            if Find(k,area_name,"Vetor",banco_de_vetores):
                                break
                        while True:
                            conf = input('\nConfirmar vetor? (S) ou (N):')
                            if Compare(conf,"S") or Compare(conf,"N"):
                                break
                        if Compare(conf,"S"):
                            SetIntro(area_name)
                            ShowUnit(banco_de_vetores[k-1])
                            while True:
                                axis = input("\nEixo:")
                                if len(banco_de_vetores[k-1]) == 2:
                                    if CompareSegment(axis,"XY"):
                                        break
                                else:
                                    if CompareSegment(axis,"XYZ"):
                                        break
                                SetIntro(area_name)
                                ShowUnit(banco_de_vetores[k-1])
                            if len(banco_de_vetores[k-1]) == 2:
                                new_vector = Reflect2D(banco_de_vetores[k-1],axis)
                            else:
                                new_vector = Reflect3D(banco_de_vetores[k-1],axis)
                            print("\nVetor refletido no eixo {}:\n".format(axis))
                            ShowUnit(new_vector)
                            next = input('\n(A) para adicionar vetor ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
                            if Compare(next,"A"):
                                Adicionar(new_vector,banco_de_vetores)
                                print('\nVetor adicionado')
                            else:
                                print('\nVetor não adicionado')
                            break
                        else:
                            SetIntro(area_name)
                    else:
                        print("\nSem vetores para calcular :(")
                        break
                input("\nEnter para continuar")

            #Acesso à projeção de vetores
            elif Compare(entry,"P"):
                area_name = "Projeção de vetor:"
                while True:
                    SetIntro(area_name)
                    if len(banco_de_vetores):
                        while True:
                            k = Get('Número do vetor:')
                            print()
                            if k == "Error":
                                SetIntro(area_name)
                            if Find(k,area_name,"Vetor",banco_de_vetores):
                                break
                        while True:
                            conf = input('\nConfirmar vetor? (S) ou (N):')
                            if Compare(conf,"S") or Compare(conf,"N"):
                                break
                        if Compare(conf,"S"):
                            SetIntro(area_name)
                            ShowUnit(banco_de_vetores[k-1])
                            while True:
                                axis = input("\nEixo:")
                                if len(banco_de_vetores[k-1]) == 2:
                                    if CompareSegment(axis,"XY"):
                                        break
                                else:
                                    if CompareSegment(axis,"XYZ"):
                                        break
                                SetIntro(area_name)
                                ShowUnit(banco_de_vetores[k-1])
                            if len(banco_de_vetores[k-1]) == 2:
                                new_vector = Projection2D(banco_de_vetores[k-1],axis)
                            else:
                                new_vector = Projection3D(banco_de_vetores[k-1],axis)
                            print("\nProjeção no eixo {}:\n".format(axis))
                            ShowUnit(new_vector)
                            next = input('\n(A) para adicionar vetor ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
                            if Compare(next,"A"):
                                Adicionar(new_vector,banco_de_vetores)
                                print('\nVetor adicionado')
                            else:
                                print('\nVetor não adicionado')
                            break
                        else:
                            SetIntro(area_name)
                    else:
                        print("\nSem vetores para calcular :(")
                        break
                input("\nEnter para continuar")

            #Acesso ao cisalhamento
            elif Compare(entry,"C"):
                area_name = "Cisalhamento:"
                while True:
                    SetIntro(area_name)
                    if len(banco_de_vetores):
                        while True:
                            k = Get('Número do vetor:')
                            print()
                            if k == "Error":
                                SetIntro(area_name)
                            if Find(k,area_name,"Vetor",banco_de_vetores): 
                                break
                        while True:
                            conf = input('\nConfirmar vetor? (S) ou (N):')
                            if Compare(conf,"S") or Compare(conf,"N"):
                                break
                        if Compare(conf,"S"):
                            #Quebra temporária caso vetor seja 3D
                            if len(banco_de_vetores[k-1]) == 3:
                                SetIntro(area_name)
                                print('Ops, a versão {} ainda não suporta cisalhamento 3D :('.format(versao))
                                break
                            SetIntro(area_name)
                            ShowUnit(banco_de_vetores[k-1])
                            while True:
                                axis = input("\nEixo:")
                                if len(banco_de_vetores[k-1]) == 2:
                                    if CompareSegment(axis,"XY"):
                                        break
                                else:
                                    if CompareSegment(axis,"XYZ"):
                                        break
                                SetIntro(area_name)
                                ShowUnit(banco_de_vetores[k-1])
                            while True:
                                factor = Get("Fator:")
                                if factor != 'Error':
                                    break
                            if len(banco_de_vetores[k-1]) == 2:
                                new_vector = Cisilh2D(banco_de_vetores[k-1],axis,factor)
                            else:
                                pass
                            print("\nCisalhamento de fator {} no eixo {}:\n".format(factor,axis))
                            ShowUnit(new_vector)
                            next = input('\n(A) para adicionar vetor ao banco\nQualquer outro para sair sem adicionar\n\nInput:')
                            if Compare(next,"A"):
                                Adicionar(new_vector,banco_de_vetores)
                                print('\nVetor adicionado')
                            else:
                                print('\nVetor não adicionado')
                            break
                        else:
                            SetIntro(area_name)
                    else:
                        print("\nSem vetores para calcular :(")
                        break
                input("\nEnter para continuar")

            #Limpar banco
            elif Compare(entry,"L"):
                banco_de_vetores = []

            #Saída de vetores/programa
            elif Compare(entry,"M") or Compare(entry,"E"):
                break

            else:
                SetColor(entry)

    #Acesso ao 2048
    elif entry == '2048':
        os.system('cls')
        grid_size = 4
        grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
        playing = True

        while playing:
            free_places = VerifyFree(grid)
            if len(free_places):
                coord = choice(free_places)
                grid[coord[0]][coord[1]] = 2
            else:
                SetIntro('\nPerdeu KKKKKKK')
                input("")
                break

            if Win(grid):
                SetIntro(0)
                Show2048(grid)
                print('\nNice :)')
                input('\nEnter para voltar')
                break
                    
            while True:
                SetIntro(0)
                Show2048(grid)
                next_move = input('\nMove: ')
                os.system('cls')
                
                if len(next_move) == 1 and next_move in 'aAdD':
                    Move('h', next_move)
                    Fuse('h', next_move)
                    Move('h', next_move)
                    Fuse('h', next_move)
                    break
                elif len(next_move) == 1 and next_move in 'wWsS':
                    Move('v', next_move)
                    Fuse('v', next_move)
                    Move('v', next_move)
                    Fuse('v', next_move)
                    break
                elif next_move == 'e' or next_move == 'E':
                    playing = False
                    break

    else:
        SetColor(entry)

    os.system('cls')
