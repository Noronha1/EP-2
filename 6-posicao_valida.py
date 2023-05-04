def define_posicoes(linha, coluna, orientacao, tamanho):
    if tamanho == 1:
        lista = [[int(linha),int(coluna)]]
        return lista   
    else:
        if orientacao == "vertical":
            lista = []
            for i in range(tamanho):
                lista.append([int(linha)+i,int(coluna)])
            
        if orientacao == "horizontal":
            lista = []
            for i in range(tamanho):
                lista.append([int(linha) ,int(coluna)+ i])

    return lista




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
