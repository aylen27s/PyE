ERR = -1
OK = 1

def CargarRg(lista):
	valores = input(' 	Ingrese los valores del Rango : ')
	for n in valores.split(" "):
		lista.append(int(n))
	
def CargarProb(rango, tabla):
	cont = 0
	for valor in rango:
		p = input(' 	P_x(%s): '%(str(valor)))
		cont += float(p)
		obj={'valor':valor, 'prob':p}
		tabla.append(obj)

	if cont == 1:
		return OK
	else:
		tabla=[]
		return ERR

def Esperanza(varAleatoria):
	esperanza = 0

	for x in varAleatoria:
		esperanza += int(x['valor']) * float(x['prob'])

	return esperanza