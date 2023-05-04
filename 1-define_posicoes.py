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