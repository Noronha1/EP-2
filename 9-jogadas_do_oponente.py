import random
random.seed(2)
jogando = True
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def afundados(frota,tabuleiro):
    c = 0
    for navio in frota.values():

        for lista in navio:
            c2 = 0
            for coordenadas in lista:
                x = coordenadas [0]
                y = coordenadas [1]
                if tabuleiro[x][y] == "X":
                    c2 += 1
            if c2 >= len(lista):
                c +=1 


    return c    
                

def converte_orientacao(orientacao):
    if orientacao == 2 or orientacao == 1:

        if orientacao == 1:
            orientacao2 = "vertical"
            return orientacao2

        elif orientacao == 2:
            orientacao2 = "horizontal"
            return orientacao2
    
    return False
    
def posiciona_frota(frota):
    #tabuleiro vazio
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navios in frota.values():
        for lista_coordenadas in navios:
            for coordenadas in lista_coordenadas:
                x = coordenadas[0]
                y = coordenadas[1]
                tabuleiro[x][y] = 1
    return tabuleiro
     

def define_posicoes(linha, coluna, orientacao, tamanho):
    if tamanho == 1:
        lista = [[int(linha),int(coluna)]]
        
         
    else:
        if orientacao == "vertical":
            lista = []
            for i in range(tamanho):
                linha2 = linha + i
                lista.append([int(linha2),int(coluna)])

                
        if orientacao == "horizontal":
            lista = []
            for i in range(tamanho):
                coluna2 = coluna + i
                lista.append([int(linha) ,int(coluna2)])

    return lista





def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    #criar um indice caso ele não exista 
    if nome_navio not in frota:
        frota[nome_navio] = []
    #cria uma lista vazia para um novo navio
    navio_novo = define_posicoes(linha, coluna, orientacao, tamanho)
    #adiciona navio novo à frota 
  
    frota[nome_navio].append(navio_novo)
    return frota

def posicao_valida(navios,linha, coluna,orientacao, tamanho):
    navio_novo = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for coordenadas in navio_novo:
    #checar se a posição é maior que 9
        for x_e_y in coordenadas:
            if x_e_y >=10:
                return False
        for checando_navios in navios.values():
            for checando_coordenadas in checando_navios:
                if coordenadas in checando_coordenadas:
                    return False
    
    return True 



    
    
###########################################################################################################################


frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

for embarcacao in frota.keys():
    if embarcacao == "porta-aviões":
        nome_navio = "porta-aviões"
        i = 0
        while i < 1:
            print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
            tamanho = 4 
            linha = int(input("qual linha: "))
            coluna = int(input("qual coluna: "))
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            orientacao2 = converte_orientacao(orientacao)
            if orientacao2 != False:
                resultado = posicao_valida(frota, linha, coluna, orientacao2, tamanho)
                if resultado == True:
                    frota = preenche_frota(frota,nome_navio,linha,coluna,orientacao2,tamanho)
                    i = i + 1
                else:
                    print("Esta posição não está válida!")
                
            else:
                print("Esta posição não está válida!")

            



    if embarcacao == "navio-tanque":
        nome_navio = "navio-tanque"
        i = 0
        while i < 2:
            print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
            tamanho = 3
            linha = int(input("qual linha: "))
            coluna = int(input("qual coluna: "))
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            orientacao2 = converte_orientacao(orientacao)
            if orientacao2 != False:
                resultado = posicao_valida(frota, linha, coluna, orientacao2, tamanho)
                if resultado == True:
                    frota = preenche_frota(frota,nome_navio,linha,coluna,orientacao2,tamanho)
                    i = i + 1
                else:
                    print("Esta posição não está válida!")


            else:
                print("Esta posição não está válida!")



    if embarcacao == "contratorpedeiro":
        nome_navio = "contratorpedeiro"
        i = 0
        while i < 3:
            print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
            tamanho = 2
            linha = int(input("qual linha: "))
            coluna = int(input("qual coluna: "))
            orientacao = int(input("[1] Vertical [2] Horizontal "))
            orientacao2 = converte_orientacao(orientacao)
            if orientacao2 != False:
                resultado = posicao_valida(frota, linha, coluna, orientacao2, tamanho)
                if resultado == True :
                    frota = preenche_frota(frota,nome_navio,linha,coluna,orientacao2,tamanho)
                    i = i + 1
                else:
                    print("Esta posição não está válida!")
          
            else:
                print("Esta posição não está válida!")





    if embarcacao == "submarino":
        nome_navio = "submarino"
        i = 0
        while i < 4:
            print('Insira as informações referentes ao navio submarino que possui tamanho 1')
            tamanho = 1
            linha = int(input("qual linha: "))
            coluna = int(input("qual coluna: "))
            orientacao2 = 1

            resultado = posicao_valida(frota, linha, coluna, orientacao2, tamanho)
            if resultado == True:
                frota = preenche_frota(frota,nome_navio,linha,coluna,orientacao2,tamanho)
                i = i + 1
            else:
                print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)      
tabuleiro_oponente = posiciona_frota(frota_oponente)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

usadas = []
usadas2= []


while jogando:
    valido = 1
    print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))
    linha = int(input('Informe a linha que você deseja atacar.'))
    while linha<0 or linha>9:
        print('Linha inválida!')
        linha = int(input('Informe a linha que você deseja atacar.'))
    

    coluna = int(input('Informe a coluna que você deseja atacar.'))
    while coluna<0 or coluna>9:
        print('Coluna inválida!')
        coluna = int(input(('Informe a coluna que você deseja atacar.')))
    
    atual = [linha,coluna]
    if atual in usadas:
        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha,coluna))
        valido = 0
     
    if valido == 1:
        usadas.append(atual)
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    afundou = afundados(frota_oponente,tabuleiro_oponente)
    if afundou >= 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
        break
    


    inimigo = True
    while inimigo == True:
        valido2 = 1
        linha3 = random.randint(0,9)
        coluna3 = random.randint(0,9)
        atual2 = [linha3,coluna3]

        if atual2 in usadas2:
            valido2 = 0
        
        if valido2 == 1:
            usadas2.append(atual2)
            tabuleiro_jogador = faz_jogada(tabuleiro_jogador,linha3,coluna3)
            print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha3,coluna3))
        afundou2 = afundados(frota,tabuleiro_jogador)
        if afundou2 >= 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
        if valido2 == 1:
            inimigo = False       


