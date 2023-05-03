def posicao_valida(navios,linha, coluna,orientacao, tamanho):
    #cria um navio novo para a verificação:
    navio_novo = []
    #preenche a lista de coordenadas de acordo com o tamanho do navio
    for listas_coordenada in range(tamanho):
        navio_novo.append([])
    
    if orientacao == 'vertical':
        for coordenadas_x in navio_novo:
            if linha >=10:
                return False
            coordenadas_x.append(linha)
            linha+=1
        for coordenadas_y in navio_novo:
            coordenadas_y.append(coluna)

    if orientacao == 'horizontal':
        for coordenadas_x in navio_novo:
            coordenadas_x.append(linha)
        for coordenadas_y in navio_novo:
            if coluna>=10:
                return False
            coordenadas_y.append(coluna)
            coluna+=1       
    
    #percorrer a lista do navio novo verificando se nenhuma de suas posições sobrepõe outro

    for coordenadas in navio_novo:
        for checando_navios in navios.values():
            for checando_coordenadas in checando_navios:
                if coordenadas in checando_coordenadas:
                    return False
    
    return True 
