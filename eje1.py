print('cantidad de numeros')
cantidad =  input()
list  = [] 
while  int(cantidad)  != 0:
    cantidad = int(cantidad) - 1
    print('ingresar digito')
    num = input()
    list.append(int(num))
    res = sum(list) / int(len(list)) 
    
print(' el  resultado es : ')
print (res)
