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
                