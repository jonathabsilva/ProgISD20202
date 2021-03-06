from os import system
system('clear')

# INICIANDO VARIÁVEIS
toqueBarra = 0  # Número de toques na barra
distanciaEstabelecida = 30  # Distância em cm do animal às barras
som1 = False  # Som Phee - Indica que o som Phee está sendo emitido
som2 = False  # Som Trill - Indica que o som Trill está sendo emitido
animalHabituado = False
etapaAproximacao = False
etapaSomToque = False
distanciaEstabelecida = 30  # 30cm
barraEsquerda = False  # Indica o toque na barra esquerda
barraDireita = False  # Indica o toque na barra direita
tempoValido = True  # Experimento sendo realizado dentro de 30min
proximaEtapa = False

while(True):
    # RECEBENDO INFORMAÇÃO SE O ANIMAL ESTÁ HABITUADO (Questão 2 - letra a)
    resposta = input('Informe se o animal está habituado [sim ou não]: ')
    if(resposta[0].lower() == 's'):
        animalHabituado = True
        etapaAproximacao = True
        print('Animal Habituado!')
    elif (resposta[0].lower() == 'n'):
        animalHabituado = False
        print('Animal não habituado ainda.\n')
    else:
        print('Não entendi sua resposta. Vou considerar que o animal está habituado...\n')
        animalHabituado = True
        etapaAproximacao = True
    # FIM DE RECEBENDO INFORMAÇÃO SE O ANIMAL ESTÁ HABITUADO (Questão 2 - letra a)

    # ETAPA DE APROXIMAÇÃO
    if(animalHabituado and etapaAproximacao and tempoValido):
        distanciaEntrada = float(
            input('\nInforme a distância entre o animal e a barra: '))
        if(distanciaEntrada < distanciaEstabelecida):
            print('Distância menor que 30cm.')
            print('Animal aproximou. Liberado 0,5ml de rec...\n')
            resposta = input('O animal tocou a barra? ')
            if(resposta[0].lower() == 's'):
                toqueBarra += 1
                print('O animal tocou a barra '+str(toqueBarra)+'x.\n')
                if(toqueBarra >= 20):
                    etapaAproximacao = False
                    etapaSomToque = True
                    print('Procedimento passou para próxima etapa.\n')
                    toqueBarra = 0
            else:
                print('O animal se aproximou mas não tocou a barra.\n')
        else:
            print('O animal não se aproximou.\n')
    # FIM ETAPA DE APROXIMAÇÃO

    # ETAPA DE SOM_E_TOQUE
    if(animalHabituado and not etapaAproximacao and etapaSomToque and tempoValido):
        resposta = input(
            'Para emitir som Phee digite 1, para emitir som Trill digite 2: ')
        if(resposta == '1'):
            som1 = True
            print('Emitindo som Phee...')
        elif(resposta == '2'):
            som2 = True
            print('Emitindo som Trill...')
        else:
            print('Resposta não identificada, tente novamente.')

        if(som1 or som2):
            print('\nSe o animal tocou a barra esquerda digite 1.')
            print('Se o animal tocou a barra direita digite 2.')
            resposta = input(
                'Respostas diferentes indicarão que o animal não tocou a barra: ')
            if(resposta == '1'):
                barraEsquerda = True
            elif(resposta == '2'):
                barraDireita = True
            else:
                barraDireita = False
                barraEsquerda = False

            if(som1 and barraEsquerda):
                toqueBarra += 1
                print('\nO animal acertou '+str(toqueBarra)+'x até agora.')
                print('Liberado 0,5 de rec.')
            elif(som2 and barraDireita):
                toqueBarra += 1
                print('\nO animal acertou '+str(toqueBarra)+'x até agora.')
                print('Liberado 0,5 de rec.')
            else:
                print('\nO animal não tocou a barra correspondente.')
                print('Não foi liberado nada.')

            som1 = False
            som2 = False

        # VERIFICAR SE O PROCEDIMENTO IRÁ PARA PRÓXIMA ETAPA
        resposta = input(
            '\nJá faz 30min que iniciou o experimento [sim ou não]? ')
        if(resposta[0].lower() == 's'):
            tempoValido = False
            print('\nNão habilitado a seguir para próxima etapa.')
            print('O animal precisa descansar. Repita o experimento em outro momento.\n')
        elif(toqueBarra >= 50 and not proximaEtapa):
            print('\nEtapa finalizada. Seguir para próxima etapa do experimento.\n')
            etapaSomToque = False
            proximaEtapa = True
            break
        else:
            print('\nContinue o experimento...\n')
        # FIM DA VERIFICAÇÃO SE O PROCEDIMENTO IRÁ PARA PRÓXIMA ETAPA
    # FIM ETAPA DE SOM_E_TOQUE
