from funciones import *


print('\n 	Calculadora de Esperanza Matematica\n 	Proabilidad y estadistica\n')
print(' 	Carga de elementos del rango de la variable aleatoria\n')

rg=[]
lista=[]
CargarRg(rg)
if  CargarProb(rg, lista)== OK:
	e=Esperanza(lista)
	print('\n 	R(X): '+ str(rg))
	print(' 	------------------')
	print(' 	  Probabilidades  ')
	print(' 	------------------')

	for x in lista:
		print(' 	   p(%s) | %s' %(x['valor'],x['prob']))
		print(' 	------------------')

	print('\n 	E(X)= %s \n\n' %(e))
else:
	print(' 	Error: La suma de las probabilidades es mayor a 1\n\n')