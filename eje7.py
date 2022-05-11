print('ingrese la frase')
frase = input()
vidas = 10
enc = 0
print(vidas)
while (int(vidas))  != 0:
   print( 'ingrese la letra')
   letra= input()
   e = (frase.count(letra)>0)
   if  e  == True:
       enc = int(enc) + 1
       if  int(enc) ==  (len(frase)):
             print('completado')
             break
   
   else:
          print('erro, intentos restantes:')
          vidas = int(vidas) - 1
          print(vidas)

print('juego terminado')
