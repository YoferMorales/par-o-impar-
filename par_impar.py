n1=float(input('cual es el numero 1 \n'))
n2=float(input('cual es el numero 2 \n'))

if n1 or n1 > 0:
    resultado=n1+n2
    resto=resultado%2
else:
  print('numeros no validos')
  
if resto == 0:
    print(f'''
          el resultado de la suma es de: {resultado}
          y el numero es par''')
else:
    print(f'''
          el resultado de la suma es de: {resultado}
          y el numero es impar''')
    
