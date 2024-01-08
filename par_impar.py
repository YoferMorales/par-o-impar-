# Ejercicio 3: Suma de Números Pares e Impares Escribe un programa en Python que
# solicite al usuario ingresar un número entero positivo. Luego, calcula y muestra
# la suma de los números pares y la suma de los números impares desde 1 hasta el número ingresado.

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
    
