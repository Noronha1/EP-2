def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    #criar um indice caso ele não exista 
    if nome_navio not in frota:
        frota[nome_navio] = []
    #cria uma lista vazia para um novo navio
    navio_novo = []
    #preenche a lista de coordenadas de acordo com o tamanho do navio
    for listas_coordenada in range(tamanho):
        navio_novo.append([])
    
    #preenche coordenadas de acordo com a orientação
    if orientacao == 'vertical':
        for coordenadas_x in navio_novo:
            coordenadas_x.append(linha)
            linha+=1
        for coordenadas_y in navio_novo:
            coordenadas_y.append(coluna)

    if orientacao == 'horizontal':
        for coordenadas_x in navio_novo:
            coordenadas_x.append(linha)
        for coordenadas_y in navio_novo:
            coordenadas_y.append(coluna)
            coluna+=1


    #adiciona navio novo à frota 
    frota[nome_navio].append(navio_novo)
    return frota
    