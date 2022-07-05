import random

palavras = ["xanascript","cu","piton","javagina","esquistossomose", "naftalina", "ribonucleico", "idiossincratico", "fagocitose", "quinquagesimo"]

def selectRandom(palavras):
  return random.choice(palavras)
palavra_secreta = selectRandom(palavras)

digitadas = []

chances = 6

def imprime_mensagem_vencedor():

    print("")
    print("                 GANHOU")
    print("")
    print("────────────────█████████───────────────")
    print("──────────────█████████████─────────────")
    print("───────────███████████████████──────────")
    print("────────────────────────────────────────")
    print("────────████████████████████████────────")
    print("────────████████████████████████────────")
    print("────────────────────────────────────────")
    print("█████████─████████████████████─█████████")
    print("█████████─████████████████████─█████████")
    print("███───────████████────████████───────███")
    print("███───────██████───██───██████───────███")
    print("─███──────█████──████────█████──────███─")
    print("──███─────████─────██─────████─────███──")
    print("───███────████─────██─────████────███───")
    print("────███───█████────██────█████───███────")
    print("─────███──█████────██────█████──███─────")
    print("──────███─███████──────███████─███──────")
    print("───────██─████████████████████─██───────")
    print("────────█─████████████████████─█────────")
    print("────────────────────────────────────────")
    print("──────────████████████████████──────────")
    print("───────────██████████████████───────────")
    print("─────────────██████████████─────────────")
    print("───────────────███████████──────────────")
    print("────────────────────────────────────────")
    print("────────────────█████████───────────────")
    print("──────────────█████████████─────────────")
    print("Siga @luis_fjs14 no instagram")

def imprime_mensagem_perdedor(palavra_secreta):

    print("")
    print("A palavra era {}".format(palavra_secreta))
    print("")
    print("          PERDEU")
    print("")
    print("███████████████████████████")
    print("███████▀▀▀░░░░░░░▀▀▀███████")
    print("████▀░░░░░░░░░░░░░░░░░▀████")
    print("███│░░░░░░░░░░░░░░░░░░░│███")
    print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
    print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
    print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
    print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
    print("██▌░│██████▌░░░▐██████│░▐██")
    print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
    print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
    print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
    print("████▄─┘██▌░░░░░░░▐██└─▄████")
    print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
    print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
    print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
    print("███████▄░░░░░░░░░░░▄███████")
    print("██████████▄▄▄▄▄▄▄██████████")
    print("███████████████████████████")
    print("Siga @luis_fjs14 no instagram")

def desenha_forca(erros):

    print("  _______     ")
    print(" |/      |    ")

    if(chances == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(chances == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(chances == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(chances == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(chances == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (chances == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

alfabeto = list("abdcefghijklmnopqrstuvwxyz")

print("------------------------------")
print("| Jogo da forca de luisfjs14 |")
print("------------------------------")

while True:

    print(f"As letras digitadas são: {digitadas}")
    print(f"Chances: {chances}")

    for letra_secreta in palavra_secreta:

        if letra_secreta in digitadas:

            print(letra_secreta, end=' ')

        else:

            print('_', end=' ')

    chute = input("\nDigite uma letra ou 'sair' para fechar o programa (somente letras minúsculas): ")

    if chute == "sair":

        break

    elif chute not in alfabeto or chute == '':

        print("")
        print("Isso não é uma letra, você deve digitar apenas letras")
        print("")
        continue

    elif len(chute) > 1:

        print("")
        print("Não vale digitar mais que uma letra amigo!")
        print("")
        continue

    elif chute in digitadas:

        print("")
        print("Você já digitou essa letra")
        print("")
        continue

    digitadas.append(chute)

    if chute in palavra_secreta:

        print("")
        print("Acertou uma letra, parabéns!")
        print("A palavra está assim:")

        for letra_secreta in palavra_secreta:

            if letra_secreta in digitadas:

                print(letra_secreta, end=' ')

            else:

                print('_', end=' ')

        tentativa = input("Deseja chutar a palavra? digite 's' para digitar ou qualquer outra letra para continuar tentando: ")

        if tentativa == "s":

            tenta = input("Digite a palavra (somente letras minúsculas): ")

            if tenta == palavra_secreta:

                imprime_mensagem_vencedor()
                break

            else:

                imprime_mensagem_perdedor(palavra_secreta)
                break

        else:

            continue

    else:

        desenha_forca(chances)
        print("")
        print(f"Errou, cuidado você só tem {chances - 1} chances")
        print("")
        chances -= 1

    if chances <= 0:

        imprime_mensagem_perdedor(palavra_secreta)
        break

    elif set(palavra_secreta).issubset(set(digitadas)):

        imprime_mensagem_vencedor()
        break