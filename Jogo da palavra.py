import os

palavra_secreta = 'futebol'
letra_acertada = ''
tentativas = 0

while True:
    print('Olá, seja bem vindo ao game palavra secreta')
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    
    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print('PARABÉNS, MEU NOBRE GUERREIRO, VOCÊ DESCOBRIU QUAL ERA A PALAVRA SECRETA!!!')
        print('O número de tentativas foi', tentativas)
        letra_acertada = ''
        tentativas = 0
