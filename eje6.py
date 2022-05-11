print('ingrese la palabra')
igual = 0
aux = 0
texto = input()
for ind in reversed(range(0, len(texto))):
    if texto[ind].lower() == texto[aux].lower():
        igual += 1
    aux += 1

if len(texto) == igual :
    print('palindromo')
else:
    print('no palindromo')
