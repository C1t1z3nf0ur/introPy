secFum = 50
secNoFum = 50
i = 100
while int(i) > 0:
    i = int(i) - 1
    print('coloque 1 para la seccion de fumadores y 2 para la de no fumadores')
    op = input()
    if  int(op) == 1:
         secFum = int(secFum) - 1
         print('todavia quedan: ', secFum)
         if  int(secFum) <= 0:
          print('se acabo el espacio para fumadores')
       
    if  int(op) == 2:
         secNoFum = int(secNoFum) -1
         print('todavia quedan: ', secNoFum)
         if int(secNoFum) <= 0:
           print('se acabo el espacio para no fumadores')

print('restantes sec fumadores:')
print(secFum)
print('restantes sec no fumadores')
print(secNoFum)

       

