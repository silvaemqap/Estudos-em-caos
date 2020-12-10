'''A ideia desse arquivo é implementar uma função que aplique a transformação do gato de Arnold. A complexidade computacional de constroi_ciclos(n) é (n^3)*lg(n)'''

from pprint import pprint
from time import time
from fractions import Fraction

def gato(ponto, p, reticulado):
	'''(tuple, int, list) -> (tuple)
	Recebe um par ordenado ponto e devolve a aplicação do gato de Arnold nesse ponto - no espaço do reticulado do quadrado unitário em p^2 pixels. É necessario passar como argumento a lista reticulado, que é da forma [0/p, 1/p, 2/p, ... , (p-1)/p]'''
	
	#Vamos trabalhar apenas com objetos Fraction
	x = Fraction(ponto[0])
	y = Fraction(ponto[1])
	novo_x = x + y
	novo_y = x + 2*y
	
	#Agora aplicamos a aritmética modular
	novo_x %= 1
	novo_y %= 1
	#Por fim, precisamos converter o ponto para o espaço de pixels
		
	novo_x = busca_binaria(novo_x.limit_denominator(p), reticulado)
	novo_y = busca_binaria(novo_y.limit_denominator(p), reticulado)
	return novo_x, novo_y
	
def busca_binaria(ponto, lista):
	''' (float, list) -> Fraction
	Essa função faz uma busca binária numa lista ordenada de frações e retorna o maior elemento da lista que seja menor ou igual a ponto'''
	direita = len(lista)
	esquerda = 0
	meio = (direita-esquerda)//2
	while direita > esquerda:
		if lista[meio] <= ponto:
			esquerda = meio
			if meio +1 == len(lista) or lista[meio+1] > ponto:
				return lista[meio]	
		else:
			direita = meio
		meio = esquerda + (direita-esquerda)//2
		
	return None

def constroi_ciclos(p):
	''' (int) -> dic
	Essa função recebe um inteiro p e retorna um dicionario ciclos, cujas chaves são inteiros representando períodos e os valores são listas associadas ao período sob a transformação de Arnold
	'''
	ini = time()
	print(f"Rodando os testes para p = {p} \n")
	todos_pontos = []
	ret= []
	for i in range(0,p):
		#Criando a lista 'reticulado'
		ret.append(Fraction(i,p))
		for j in range(0,p):
			#A lista todos_pontos contém todos os p^2 pontos do quadrado unitário reticulado
			todos_pontos.append((Fraction(i,p), Fraction(j,p)))

	print("Construindo os ciclos")
	#O dicionário abaixo terá o período k do ciclo como chave e uma lista de todos os ciclos de período k como valores
	ciclos = {}
	while todos_pontos != []:
		#Enquanto eu não tiver caminhado por todo o reticulado
		#Inicio um ciclo vazio, do qual não sei o período
		ciclo = []
	
		#Pego um ponto inicial qualquer
		inicial = todos_pontos[0]
	
		#E o adiciono ao ciclo
		ciclo.append(inicial)
	
		#Removendo-o da lista de pontos ainda não vistos
		todos_pontos.remove(inicial)
	
		#A princípio o período é zero
		periodo = 0
		
		#Aplico a função do gato de Arnold no ponto inicial 
		final = gato(inicial, p, ret)
		#A cada aplicação do gato, adiciono um ao período
		periodo += 1
		
		if final != inicial:
			#O ciclo contém apenas pontos diferentes
			ciclo.append(final)
		if final in todos_pontos:
			todos_pontos.remove(final)
	
		while final != inicial:
			#Enquanto a aplicação não voltar ao ponto inicial, repito os passos acima
			final = gato(final, p, ret)
			periodo += 1
			if final in todos_pontos:
				todos_pontos.remove(final)
			if final not in ciclo:
				ciclo.append(final)

		if periodo not in ciclos.keys():
			#Achamos um ciclo de período desconhecido
			ciclos[periodo] = [ciclo]
		else:
			ciclos[periodo].append(ciclo)
	fim = time()
	print(f"Construção do ciclo para p = {p} levou {(fim-ini):.3f}s")
	return ciclos
		
pprint(constroi_ciclos(6))

'''pprint(constroi_ciclos(12))

pprint(constroi_ciclos(24))

pprint(constroi_ciclos(48))'''

'''a = constroi_ciclos(3)
b = constroi_ciclos(6)
c = constroi_ciclos(12)
d = constroi_ciclos(24)
f = constroi_ciclos(48)
g = constroi_ciclos(96)
h = constroi_ciclos(101)'''
	


