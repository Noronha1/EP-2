def converte_orientacao(orientacao):
    if orientacao == 2 or orientacao == 1:

        if orientacao == 1:
            orientacao2 = "vertical"
            return orientacao2

        elif orientacao == 2:
            orientacao2 = "horizontal"
            return orientacao2
    
    return False
    


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
        

print(frota)