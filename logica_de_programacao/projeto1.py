# usando for
for andar in range(20, 0, -1):  # Começa em 20 e vai até 1
    if andar == 13:  # Ignora o 13
        continue
    print(andar)

print("#############################################")
#usando while
andar = 20
while andar > 0:  # Enquanto o andar for maior que 0
    if andar != 13:  # Ignora o 13
        print(andar)
    andar -= 1  # Decrementa o número do andar
print("#############################################")
#usando do-while
andar = 20
while True:
    if andar != 13:  # Ignora o 13
        print(andar)
    andar -= 1  # Decrementa o número do andar
    if andar == 0:  # Condição de parada
        break
