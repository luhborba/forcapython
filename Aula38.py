import random
lista = ['coxinha','pastel','hamburguer','sanduiche','pizza']

numero = random.randint(0,5)
palavra = lista[numero]
digitadas = []
chances = 0
parar = 10

print(10 * '-' + 'Bem Vindo ao Jogo da Forca' + 10 * '-')
print('-------------By: Luciano Borba----------------')

print('Dica: Trata-se do nome de um lanche simples\n')
print('Você pode errar:\n 6 Palpites no modo fácil(Modo 1)\n'
      ' 4 Palpites no modo Normal(Modo 2)\n 2 Palpites no modo dificil(Modo 3)\n')

# Escolher Dificuldade
while True:

    if parar == 0:
        break

    modo = input('Escolha seu modo de jogo: ')

    # Verificar Modo de Jogo
    if modo.isnumeric() == False or int(modo) >= 4:
        print('\nDigite um número de 1 a 3')
        print()
        continue
    else:
        if int(modo) == 1:
            chances = 6
        if int(modo) == 2:
            chances = 4
        if int(modo) == 3:
            chances = 2
    print('\nO jogo começou')

    # Regras da Forca
    while True:

        # Verificar Chances
        if chances <= 0:
            parar = 0
            print('Você Perdeu!!!!!!')
            break

        letra = input('Digite uma letra: ')

        if len(letra) > 1:
            print('Ahhh, isso não vale, digite apenas 1 letra.')
            continue

        digitadas.append(letra)

        if letra in palavra:
            print('UALLLLLLL!!!!, Você acertou uma das letras da palavra secreta, {letra}.')
            
        else:
            print('AFFFZzzz, Errastes, a letra {letra} NÃO EXISTE na palabra secreta.')
            digitadas.pop()

        secreta_temp = ''

        for letra_secreta in palavra:
            if letra_secreta in digitadas:
                secreta_temp += letra_secreta
            else:
                secreta_temp += '*'

        if secreta_temp == palavra:
            print(f'Parabéns, Você Ganhou!!! A palavra era {secreta_temp}.')
            exit()
        else:
            print(f'A palavra secreta está assim {secreta_temp}')

        # Zerar Chances
        if letra not in palavra:
            chances -= 1
            print(f'Você pode erras  {chances} vezes ainda. Boa Sorte')

        print()
