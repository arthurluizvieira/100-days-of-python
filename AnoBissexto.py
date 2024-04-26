year = int(input('qual ano quer verificar? '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Ano Bissexto')

        else: 
            print('ano nao bissexto')
    else: 
        print('ano bissexto')
else:
    print('Ano não bissexto')