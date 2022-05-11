lista1  = []
lista2  = []
print('ingrese el limite de las listas')
lim = input()
while int(lim) != 0:
    print('ingrese un digito para la lista 1')
    num  = input()
    lista1.append(int(num))
    lim = int(lim) - 1

while int(lim) <= 2:
    print ('ingrese un digito para la lista 2')
    num = input()
    lista2.append(int(num))
    lim = int(lim) + 1

res = sum(lista1) + sum(lista2)
print(' el  resultado es: ')
print(res)

