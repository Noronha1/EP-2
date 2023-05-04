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

def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    #criar um indice caso ele não exista 
    if nome_navio not in frota:
        frota[nome_navio] = []
    #cria uma lista vazia para um novo navio
    navio_novo = define_posicoes(linha, coluna, orientacao, tamanho)
    #adiciona navio novo à frota 
    frota[nome_navio].append(navio_novo)
    return frota
    