promMa = []
promMe = []
prom = 0
notas = []
i = 5
while int(i) != 0:
    i = int(i) - 1
    print('ingrese la nota')
    nota = input()
    notas.append(int(nota))

c = 4
prom = sum(notas) / 5
print('culo', prom)
while int(i) <= 4:  
    i = int(i) + 1
    if  notas[c] < int(prom):
        promMa.append(int(notas[c]))
    if notas[c] > int(prom):
        promMe.append(int(notas[c]))

print(' las notas arriba del promedio')
print(promMa)
print('las notas abajo del promediio')
print(promMe)
