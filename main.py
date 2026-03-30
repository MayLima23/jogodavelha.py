def interface(tabuleiro):
    print("    0   1   2 ")
    print("0  [{}] [{}] [{}]".format(tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print("1  [{}] [{}] [{}]".format(tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print("2  [{}] [{}] [{}]".format(tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))

def validarVitoria(rodada):
    global parar
    # Verificação das Horizontais
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        interface(tabuleiro)
        print("o {} Vencedor!".format(rodada))
        parar = True

    if (tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][2] == rodada):
            interface(tabuleiro)
            print("o {} Vencedor!".format(rodada))
            parar = True

    if (tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
        interface(tabuleiro)
        print("o {} Vencedor!".format(rodada))
        parar = True
    # Verficação das Verticais
    if (tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada):
        interface(tabuleiro)
        print("o {} Vencedor!".format(rodada))
        parar = True

    if (tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][1] == rodada):
        interface(tabuleiro)
        print("o {} Vencedor!".format(rodada))
        parar = True

    if (tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro[2][2] == rodada):
        interface(tabuleiro)
        print("o {} Vencedor!".format(rodada))
        parar = True
    #Verificação das Diagonais
    if (tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada):
        interface(tabuleiro)
        print("o {} Vencedor!".format(rodada))
        parar = True

    if (tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[0][2] == rodada):
        interface(tabuleiro)
        print("o {} Vencedor!".format(rodada))
        parar = True

# Configurações básicas
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
parar = False
rodada = "x"
jogadas = 0

# Loop do jogo
while parar == False:
    interface(tabuleiro)
    linha = int(input("Digite a linha da tabuleiro: "))
    coluna = int(input("Digite a coluna da tabuleiro: "))

    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada. Escolha outra!")
        continue

    tabuleiro[linha][coluna] = rodada
    validarVitoria(rodada)
    jogadas += 1

    if rodada == "x":
        rodada = "o"
    else:
        rodada = "x"

    # Verificação de Empate
    if jogadas == 9 and parar == False:
        interface(tabuleiro)
        print("Empate!")
        parar = True
