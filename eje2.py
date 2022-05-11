lim = 9
lista = []
while int(lim) != 0:
    lim = int(lim) - 1
    print('ingrese las temperatura')
    temp = input()
    lista.append(int(temp))
temPro = sum(lista) / float(len(lista))
c = 9
res = [] 
print('la temperatura promedio es')
print(temPro)
while c != 0:
    c = int(c) -1 
    if int(lista[c]) < int(temPro):
        res.append(int(lista[c])) 
       
print(' las temperaturas abajo del promedio es ')
print(res)
