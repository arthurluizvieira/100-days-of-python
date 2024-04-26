print('Bem-Vindo a Montanha Russa!')

altura = int(input('Digite sua altura em centímetros: '))

if altura > 140:
    print('Você poderá participar dessa aventura! Prossiga com o pagamento.')
    idade = int(input('Digite sua idade: '))
    if idade < 12:
        taxa = 5
        print('O valor do ingresso é de $5')
    elif idade < 18:
        taxa = 7
        print('O valor do ingresso é de $7')
    elif idade >= 45 and idade <= 55:
        taxa = 0
        print('Seus tickets são gratuitos!')
    else:
        taxa = 12
        print('O valor do ingresso é de $12')
    fotos = input('Você gostaria de acrescentar fotos na sua aventura? [S/N]').strip().upper()
    if fotos == 'S':
        valortotal = taxa + 3
        print('O valor total do ingresso ficará ${}'.format(valortotal))
    else:
        print('O valor final será {}'.format(taxa))

else: 
    print('Infelizmente você não poderá participar dessa aventura pois tem menos de 140 cm!')