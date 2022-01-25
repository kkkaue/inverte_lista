
def inverter_lista(lista):
	tamanho = len(lista)
	limite = tamanho//2
	for i in range(limite):
		aux = lista[i]
		lista[i] = lista[tamanho - i - 1]
		lista[tamanho -  i] = aux
		print(lista)

def inverter_lista2(lista):
	nova_lista = []
	tamanho = len(lista)
	for i in range(tamanho):
		nova_lista.append(lista[tamanho - i - 1])
	print(nova_lista)

inverter_lista(["a", "b", "c"])
inverter_lista2(["a", "b", "c"])
