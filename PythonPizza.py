print('Bem vindo a Python Pizza! Criaremos seu pedido automaticamente!')

tamanho = input('Escolha o tamanho da sua pizza: (P, M, G) ').strip().upper()
add_pepperoni = input('Deseja adicionar PEPPERONI em sua pizza? [Y/N]').strip().upper()
add_queijo = input('Deseja adicionar QUEIJO em sua pizza? [Y/N]').strip().upper()

if tamanho == 'P':
    P = 15
    pepperoni = 2
    queijo = 1
    valor_total = P + pepperoni + queijo  
    if add_pepperoni == 'Y' and add_queijo == 'Y':
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    elif add_pepperoni == 'Y' and add_queijo == 'N':
        valor_total = P + pepperoni
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    elif add_pepperoni == 'N' and add_queijo == 'Y':
        valor_total = P + queijo
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    else: 
        valor_total = P
        print('O valor da sua pizza ficará em {}'.format(valor_total))

if tamanho == 'M': 
    M = 20
    pepperoni = 3
    queijo = 1
    valor_total = M + pepperoni + queijo  
    if add_pepperoni == 'Y' and add_queijo == 'Y':
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    elif add_pepperoni == 'Y' and add_queijo == 'N':
        valor_total = M + pepperoni
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    elif add_pepperoni == 'N' and add_queijo == 'Y':
        valor_total = M + queijo
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    else: 
        valor_total = M
        print('O valor da sua pizza ficará em {}'.format(valor_total))


if tamanho == 'G':
    G = 25
    pepperoni = 3
    queijo = 1
    valor_total = G + pepperoni + queijo  
    if add_pepperoni == 'Y' and add_queijo == 'Y':
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    elif add_pepperoni == 'Y' and add_queijo == 'N':
        valor_total = G + pepperoni
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    elif add_pepperoni == 'N' and add_queijo == 'Y':
        valor_total = G + queijo
        print('O valor total da sua pizza ficará em {}'.format(valor_total))
    else: 
        valor_total = G
        print('O valor da sua pizza ficará em {}'.format(valor_total))


# print('Thank you for choosing Python Pizzas Delivery')
# size = input ... 
# add pp = input ...
# # extra cheese ... 
 

#  bill = 0 
# if size == 'S':
#  elif size == 'M':
#    bill += 20
#  else: 
#    bill += 25

#  if add_pepperoni == 'S'
#   if size == 'S':
#       bill += 2
#   else: 
#       bill += 3
#
#
#
#
#
#
#
#
#
#
#
#
#