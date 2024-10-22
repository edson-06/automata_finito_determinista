import graphviz

class Nodo():
	def __init__(self, nombre, estado):
		self.nombre=nombre
		self.estado=estado

	def setNombre(self, nom):
		self.nombre=nom

	def getNombre(self):
		return self.nombre

	def setEstado(self,est):
		self.estado=est
	
	def getEstado(self):
		return self.estado

class arrayNodoAlfabeto():
	def __init__(self,valorNodo, valorAlfabeto, tamanoNodo, tamanoAlfabeto):
		self.valorNodo = valorNodo
		self.valorAlfabeto = valorAlfabeto
		self.tamanoNodo = tamanoNodo
		self.tamanoAlfabeto = tamanoAlfabeto
		self.listaNodos=[]

	nombreABCM =['A','B','C','D','E','F','G','H']
	nombreQ =['q0','q1','q2','q3','q4','q5','q6','q8']
	nombre012 =['N0','N1','N2','N3','N4','N5','N6','N8']

	alfabetoAbc=['a', 'b', 'c']
	alfabeto012=['0', '1', '2']
	alfabeto0xyz=['x', 'y', 'z']


	def getNombreNodo(self, valorNodo):
		if valorNodo == 1:
			return  self.nombreABCM
		elif valorNodo == 2:
			return self.nombreQ
		elif valorNodo == 3:
			return self.nombre012
	
	def getNombreAlfabeto(self, valorAlfabeto):
		if valorAlfabeto == 1:
			return self.alfabetoAbc
		elif valorAlfabeto == 2:
			return self.alfabeto012
	
	def arrayNodo(self):
		i = self.tamanoNodo
		self.arrayNodoFinal=[]
		for Nodo in self.getNombreNodo(self.valorNodo):
			if i > 0:
				self.arrayNodoFinal.append(Nodo)
				i=i-1
			else:
				break
		return self.arrayNodoFinal

	def arrayAlfabeto(self):
		i = self.tamanoAlfabeto
		self.arrayAlfabetoFinal=[]
		for alfabeto in self.getNombreAlfabeto(self.valorAlfabeto):
			if i > 0:
				self.arrayAlfabetoFinal.append(alfabeto)
				i=i-1
			else:
				break
		return self.arrayAlfabetoFinal
	
	def setTiposNodos(self, nodoNombre, nodoEstado):
		self.nodo = Nodo(nodoNombre, nodoEstado)
		self.listaNodos.append(self.nodo)
	
	def getTiposNodos(self): 
		return self.listaNodos

class transicionesNodos():
	def __init__(self,listaTiposNodos, tamanoNodo, tamanoAlfabeto ):
		self.listaTiposNodos=listaTiposNodos
		self.tamanoNodo=tamanoNodo
		self.tamanoAlfabeto=tamanoAlfabeto
		self.componentesGrap()

	def componentesGrap(self):
		self.f = graphviz.Digraph('finite_state_machine', filename='imgAutomata.gv',format="png")
		self.f.attr(rankdir='LR', size='8,5')

	def recorridoNodosEstado(self):
		for n in afd.arrayNodo:
			if n.getEstado() == "inicial":
				ppppppp= ""+n.getNombre()
				print("nodo inicial: ", ppppppp)
				#nodo inicial
				self.f.node('LR_234', shape="point")
				#nodos
				self.f.attr('node', shape='circle')
				self.f.edge('LR_234', ppppppp, label='')

			elif n.getEstado() == "final":
				ppppppp= ""+n.getNombre()
				print("nodo FINAL: ", ppppppp)
				self.f.attr('node', shape='doublecircle')
				self.f.node(ppppppp)

			elif n.getEstado() == "inicialFinal":
				ppppppp= ""+n.getNombre()
				print("nodo inicial: ", ppppppp)
				#nodo inicial
				self.f.node('LR_234', shape="point")
				#nodos
				self.f.attr('node', shape='doublecircle')
				self.f.edge('LR_234', ppppppp, label='')

	def setTransision(self, nombreEstado, estadoSiguiente, letraAlfabeto):
		self.f.attr('node', shape='circle')
		self.f.edge(nombreEstado, estadoSiguiente, label=letraAlfabeto)

	def generarImagen(self):
		self.f.render()

##################################
valorNodo = 1
valorAlfabeto = 1
tamanoNodo = 3
tamanoAlfabeto = 2

afd = arrayNodoAlfabeto(valorNodo, valorAlfabeto, tamanoNodo, tamanoAlfabeto)
nodosAFD = afd.getNombreNodo
alfabetoAFD = afd.getNombreAlfabeto

arregloNodos = afd.arrayNodo()
print("Nodos")
for n in arregloNodos:
	print(n)
	
afd.setTiposNodos("A","inicialFinal")
afd.setTiposNodos("A","final")
afd.setTiposNodos("B","final")
#afd.setTiposNodos("C","")

print("Alfabeto")
for n in afd.arrayAlfabeto():
	print(n)

tiposNodos = afd.getTiposNodos
###################################

tna = transicionesNodos(tiposNodos, tamanoNodo, tamanoAlfabeto)
tna.recorridoNodosEstado()

tna.setTransision("A", "A", "a")
tna.setTransision("A", "B", "a")

tna.generarImagen()









