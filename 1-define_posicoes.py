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