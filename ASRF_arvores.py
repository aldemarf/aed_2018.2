# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO -- UFRPE
# DEPARTAMENTO DE ESTATISTICA E INFORMATICA -- DEINFO
# SISTEMAS DE INFORMAÇÃO -- BSI

# ALGORITMOS E ESTRUTURA DE DADOS
# PROF. TIAGO FERREIRA
# ALUNO ALDEMAR S R FILHO


class TreeNode:
	def __init__(self, data, color=None, height=None, balance=None):
		self.__data = data
		self.__color = color
		self.__height = height
		self.__balance = balance
		self.__father = None
		self.__rightSon = None
		self.__leftSon = None

	def __getData(self):
		return self.__data

	def __getColor(self):
		return self.__color

	def __getHeight(self):
		return self.__height

	def __getBalance(self):
		return self.__balance

	def __getFather(self):
		return self.__father

	def __getRightSon(self):
		return self.__rightSon

	def __getLeftSon(self):
		return self.__leftSon

	def __setData(self, data):
		self.__data = data

	def __setColor(self, color):
		self.__color = color

	def __setHeight(self, height):
		self.__height = height

	def __setBalance(self, balance):
		self.__balance = balance

	def __setFather(self, father):
		self.__father = father

	def __setRightSon(self, rightSon):
		self.__rightSon = rightSon

	def __setLeftSon(self, leftSon):
		self.__leftSon = leftSon

	def hasLeftSon(self):
		return self.leftSon is not None

	def hasRightSon(self):
		return self.rightSon is not None

	def isLeaf(self):
		return self.leftSon is None and self.rightSon is None

	# ### DECORATORS #### #
	data = property(__getData, __setData)
	color = property(__getColor, __setColor)
	height = property(__getHeight, __setHeight)
	balance = property(__getBalance, __setBalance)
	father = property(__getFather, __setFather)
	rightSon = property(__getRightSon, __setRightSon)
	leftSon = property(__getLeftSon, __setLeftSon)


class BinaryTree:
	def __init__(self):
		self.__root = None
		self.__height = 0


	def __getRoot(self):
		return self.__root


	def __getHeight(self):
		return self.__height


	def __setRoot(self, node):
		self.__root = node


	def __setHeight(self, height):
		self.__height = height

	def isEmpty(self):
		if self.root is None:
			return True
		else:
			return False

	def isOnlyRoot(self):
		return self.root.isLeaf()

	root = property(__getRoot, __setRoot)
	height = property(__getHeight, __setHeight)


	def insertNode(self, value):
		newNode = TreeNode(value)
		node = self.root
		father = None

		while node is not None:
			father = node
			if value <= node.data:
				node = node.leftSon
			else:
				node = node.rightSon

		newNode.father = father
		if father is None:
			self.root = newNode
		else:
			if value <= father.data:
				father.leftSon = newNode
			else:
				father.rightSon = newNode

			# node = self.root
			# while True:
				# if value <= node.data:
				# 	if node.leftSon is not None:
				# 		node = node.leftSon
				# 	else:
				# 		newNode.father = node
				# 		node.leftSon = newNode
				# 		return
				# else:
				# 	if node.rightSon is not None:
				# 		node = node.rightSon
				# 	else:
				# 		newNode.father = node
				# 		node.rightSon = newNode
				# 		return


	def insertNodeRec(self, value, node, father=None):
		if node is not None:
			if value <= node.data:
				self.insertNodeRec(value, node.leftSon, node)
			else:
				self.insertNodeRec(value, node.rightSon, node)
		else:
			newNode = TreeNode(value)
			newNode.father = father

			if father is not None:
				if value <= father.data:
					father.leftSon = newNode
				else:
					father.rightSon = newNode
			else:
				self.root = newNode


		# if self.isEmpty():
		# 	newNode = TreeNode(value)
		# 	self.root = newNode

		# elif value <= node.data:
		# 	if node.leftSon is not None:
		# 		self.insertNodeRec(value, node.leftSon)
		# 	else:
		# 		newNode = TreeNode(value)
		# 		newNode.father = node
		# 		node.leftSon = newNode
		# 		return
		# else:
		# 	if node.rightSon is not None:
		# 		self.insertNodeRec(value, node.rightSon)
		# 	else:
		# 		newNode = TreeNode(value)
		# 		newNode.father = node
		# 		node.rightSon = newNode
		# 		return


	def searchValue(self, value):
		if self.isEmpty():
			raise RuntimeError("The tree is empty!")
		else:
			node = self.root
			while True:
				if node is None:
					raise ValueError("Value not found!")
				elif value < node.data:
					node = node.leftSon
				elif value > node.data:
					node = node.rightSon
				else:
					return node


	def order(self, node=None, method="io"):
		if node is None:
			node = self.root

		if method.lower() == "io":
			self.inOrderRecEngine(node)
		elif method.lower() == "pre":
			self.preOrderRecEngine(node)
		else:
			self.posOrderRecEngine(node)


	def inOrderIterEngine(self, node):
		# if node is not None:
		# 	currentNode = node
		# 	while True:
		# 		if currentNode.hasLeftSon():
		# 			currentNode = currentNode.leftSon

		# 			continue
		# 		if currentNode.hasRightSon():
		# 			currentNode = currentNode.rightSon
		pass


	def inOrderRecEngine(self, node):
		if node is not None:
			self.inOrderRecEngine(node.leftSon)
			print(node.data,end=" ")
			self.inOrderRecEngine(node.rightSon)

	def preOrderRecEngine(self, node):
		if node is not None:
			print(node.data,end=" ")
			self.inOrderRecEngine(node.leftSon)
			self.inOrderRecEngine(node.rightSon)

	def posOrderRecEngine(self, node):
		if node is not None:
			self.inOrderRecEngine(node.leftSon)
			self.inOrderRecEngine(node.rightSon)
			print(node.data,end=" ")

	def maximum(self, node=None):
		if node is None:
			node = self.root

		if self.isEmpty():
			raise ValueError("Empty tree!")
		else:
			while node.rightSon is not None:
				node = node.rightSon
			return node

	def minimum(self, node=None):
		if node is None:
			node = self.root

		if self.isEmpty():
			raise ValueError("Empty tree!")
		else:
			while node.leftSon is not None:
				node = node.leftSon
			return node

	def predecessor(self, value=None, node=None):
		if value == None:
			if node is None:
				node = self.root
			value = node.data
		else:
			node = self.searchValue(value)

		if self.isOnlyRoot():
			raise ValueError("Root hasn't predecessors!")

		if node.hasLeftSon():
			return self.maximum(node.leftSon)
		else:
			son = node
			node = node.father
			while (node is not None) and (son is node.leftSon):
				son = node
				node = node.father

			return node

	def sucessor(self, value=None, node=None):
		if value == None:
			if node is None:
				node = self.root
			value = node.data
		else:
			node = self.searchValue(value)

		if self.isOnlyRoot():
			raise ValueError("Root hasn't sucessors!")

		if node.hasRightSon():
			return self.minimum(node.rightSon)
		else:
			son = node
			node = node.father
			while (node is not None) and (son is node.rightSon):
				son = node
				node = node.father

			return node


	def remove(self, value):
		node = self.searchValue(value)
		pass



############### MAIN ###############


############### TESTES ###############

def amostras (tamanho):
	from random import sample, shuffle
	population = list(range(tamanho * 100))
	amostra = sample(population, tamanho)
	# print(amostra)
	return amostra

from time import perf_counter as pc
from random import sample

for _ in range(5):
	a = pc()
	amostra = amostras(20000)
	b = pc()
	createSampleT = b - a

	arvore = BinaryTree()
	c = pc()

	for item in amostra:
		arvore.insertNodeRec(item, arvore.root)
	d = pc()
	insertT = d - c

	e = pc()
	valor, *_ = sample(amostra, 1)
	e1 = pc()
	assignT = e1 - e

	no = arvore.searchValue(valor)
	f = pc()
	print(no.data)
	g = pc()
	searchT = f - e1

	# arvore.order()
	# print("\n")
	h = pc()
	orderT = h - g
	i = pc()
	max = arvore.maximum().data
	j = pc()
	maximoT = j - i

	min = arvore.minimum().data
	k = pc()
	minimoT = k - j

	pred = arvore.predecessor(valor)
	l = pc()
	predT = l - k
	suces = arvore.sucessor(valor)
	m = pc()
	sucessT = m - l

	print("Root", arvore.root.data)
	print("Max", max)
	print("Min", min)
	print("Predecessor", pred.data)
	print("Sucessor", suces.data)

	print("""
	Criação de amostra : {:.5f}s
	Insercao de elementos na arvore : {:.5f}s
	Busca do valor : {:.5f}s
	Impressao da Arvore : {:.5f}s
	Maximo da Arvore : {:.5f}s
	Minimo da Arvore : {:.5f}s
	Predecessor da Arvore : {:.5f}s
	Sucessor da Arvore : {:.5f}s
	""".format(createSampleT, insertT, searchT, orderT, maximoT, minimoT, predT, sucessT))
