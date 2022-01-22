
def inverter_lista(lista):
	tamanho = len(lista)-1
	limite = tamanho//2
	for i in range(limite):
		aux = lista[i]
		lista[i] = lista[tamanho - i]
		lista[tamanho -  i] = aux
		print(lista)

def inverter_lista2(lista):
	nova_lista = []
	tamanho = len(lista)-1
	for i in range(tamanho+1):
		nova_lista.append(lista[tamanho-i])
	print(nova_lista)

inverter_lista(["a", "b", "c"])
inverter_lista2(["a", "b", "c"])