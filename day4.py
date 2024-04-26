import random
import time

print("Escolhas:")
print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")

jogador = int(input('Qual sua jogada? Digite 0 para pedra, 1 para papel e 2 para tesoura: '))
computador = random.randint(0, 2)

if computador == 0:
    print("O computador jogou pedra")
elif computador == 1:
    print("O computador jogou papel")
else:
    print("O computador jogou tesoura")

print('=-' * 10)

print('JO') 
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)


if jogador == 0 and computador == 0:
    print('Empate!')
elif jogador == 0 and computador == 1:
    print('Vitória do Computador!')
elif jogador == 0 and computador == 2:
    print('Vitória do Jogador!')

if jogador == 1 and computador == 0:
    print('Vitória do Jogador!')
elif jogador == 1 and computador == 1:
    print('Empate!')
elif jogador == 1 and computador == 2:
    print('Vitória do Computador!')

if jogador == 2 and computador == 0:
    print('Vitória do Computador!')
elif jogador == 2 and computador == 1:
    print('Vitória do Jogador!')
elif jogador == 2 and computador == 2:
    print('Empate!')
