# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO -- UFRPE
# DEPARTAMENTO DE ESTATISTICA E INFORMATICA -- DEINFO
# SISTEMAS DE INFORMAÇÃO -- BSI

# ALGORITMOS E ESTRUTURA DE DADOS
# PROF. TIAGO FERREIRA
# ALUNO ALDEMAR S R FILHO


class AVLTreeNode:
	def __init__(self, data, height=None, balance=None):
		self.__data = data
		self.__height = height
		self.__balanceFactor = balance
		self.__father = None
		self.__rightSon = None
		self.__leftSon = None

	def __getData(self):
		return self.__data

	def __getHeight(self):
		return self.__height

	def __getBalance(self):
		return self.__balanceFactor

	def __getFather(self):
		return self.__father

	def __getRightSon(self):
		return self.__rightSon

	def __getLeftSon(self):
		return self.__leftSon

	def __setData(self, data):
		self.__data = data

	def __setHeight(self, height):
		self.__height = height

	def __setBalance(self, balance):
		self.__balanceFactor = balance

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

	def sons(self):
		sons = 0
		if self.hasLeftSon():
			sons += 1
		if self.hasRightSon():
			sons += 1
		return sons

	# ### DECORATORS #### #
	data = property(__getData, __setData)
	height = property(__getHeight, __setHeight)
	balanceFactor = property(__getBalance, __setBalance)
	father = property(__getFather, __setFather)
	rightSon = property(__getRightSon, __setRightSon)
	leftSon = property(__getLeftSon, __setLeftSon)


class AVLTree:
	def __init__(self):
		self.__root = None


	def __str__(self):
		self.inOrderRecEngine(self.root, printHeight=False, printBalanceFactor=False)
		return "\n"

	def __getRoot(self):
		return self.__root


	def __getHeight(self):
		return self.__height


	def __setRoot(self, node):
		self.__root = node


	def __setHeight(self, height):
		self.__height = height


	def calculateHeight(self, node):
		if node is None:
			return -1
		else:
			leftHeight = self.calculateHeight(node.leftSon)
			rightHeight = self.calculateHeight(node.rightSon)
			if leftHeight >= rightHeight:
				node.height = leftHeight + 1
				return node.height
			else:
				node.height = rightHeight + 1
				return node.height


	def calculateBalanceFactor(self, node):
		if node is None:
			return -1
		else:
			node.balanceFactor = self.calculateBalanceFactor(node.leftSon) - self.calculateBalanceFactor(node.rightSon)
			if node.balanceFactor > 1 or node.balanceFactor < -1:
				return self.rotate(node)
			return node.height

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
		newNode = AVLTreeNode(value)
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

		if value > self.root.data:
			self.calculateHeight(self.root.rightSon)
		else:
			self.calculateHeight(self.root.leftSon)
		return


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
			newNode = AVLTreeNode(value)
			newNode.father = father

			if father is not None:
				if value <= father.data:
					father.leftSon = newNode
				else:
					father.rightSon = newNode
			else:
				self.root = newNode

			if value > self.root.data:
				self.calculateHeight(self.root.rightSon)
			else:
				self.calculateHeight(self.root.leftSon)
			return


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
			while node != None:
				if value < node.data:
					node = node.leftSon
				elif value > node.data:
					node = node.rightSon
				else:
					return node
			raise ValueError("Value not found!")


	def order(self, node=None, method="io", printHeight=False, printBalanceFactor=False):
		if node is None:
			node = self.root

		if method.lower() == "io":
			self.inOrderRecEngine(node, printHeight, printBalanceFactor)
		elif method.lower() == "pre":
			self.preOrderRecEngine(node, printHeight, printBalanceFactor)
		else:
			self.posOrderRecEngine(node, printHeight, printBalanceFactor)


	def inOrderIterEngine(self, node):
		# from array import array
		# if node is not None:
		# 	currentNode = node
		# 	fila = array('l')
		# 	while True:
		# 		if currentNode.hasLeftSon():
		# 			currentNode = currentNode.leftSon

		# 			continue
		# 		if currentNode.hasRightSon():
		# 			currentNode = currentNode.rightSon
		pass


	def inOrderRecEngine(self, node, printHeight, printBalanceFactor):
		if node is not None:
			self.inOrderRecEngine(node.leftSon, printHeight, printBalanceFactor)
			print(node.data,end=" ")
			if printHeight:
				print(node.height, end= " ")
			if printBalanceFactor:
				print(node.balanceFactor, end=" ")
			self.inOrderRecEngine(node.rightSon, printHeight, printBalanceFactor)

	def preOrderRecEngine(self, node, printHeight, printBalanceFactor):
		if node is not None:
			print(node.data,end=" ")
			if printHeight:
				print(node.height, end= " ")
			if printBalanceFactor:
				print(node.balanceFactor, end=" ")
			self.inOrderRecEngine(node.leftSon, printHeight, printBalanceFactor)
			self.inOrderRecEngine(node.rightSon, printHeight, printBalanceFactor)

	def posOrderRecEngine(self, node, printHeight, printBalanceFactor):
		if node is not None:
			self.inOrderRecEngine(node.leftSon, printHeight, printBalanceFactor)
			self.inOrderRecEngine(node.rightSon, printHeight, printBalanceFactor)
			print(node.data,end=" ")
			if printHeight:
				print(node.height, end= " ")
			if printBalanceFactor:
				print(node.balanceFactor, end=" ")

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
			print("Root hasn't predecessors!")
			return

		if node.hasLeftSon():
			return self.maximum(node.leftSon)
		else:
			son = node
			node = node.father
			while (node is not None) and (son is node.leftSon):
				son = node
				node = node.father

			return node

	def successor(self, value=None, node=None):
		if value == None:
			if node is None:
				node = self.root
			value = node.data
		else:
			node = self.searchValue(value)

		if self.isOnlyRoot():
			print("Root hasn't successors!")
			return

		if node.hasRightSon():
			return self.minimum(node.rightSon)
		else:
			son = node
			node = node.father
			while (node is not None) and (son is node.rightSon):
				son = node
				node = node.father

			if node is None:
				print("Node hasn't successors!")
				return
			else:
				return node


	def remove(self, value):
		node = self.searchValue(value)

		if node.isLeaf():
			self.removeNS(node)
		elif node.sons() == 1:
			self.removeOS(node)
		else:
			self.removeTS(node)


	def removeNS(self, node):
		if node is self.root:
			self.root = None
		elif node.data <= node.father.data:
			node.father.leftSon = None
		else:
			node.father.rightSon = None
		return

	def removeOS(self, node):
		if node is self.root:
			if node.hasLeftSon():
				node.leftSon.father = None
				self.root = node
			else:
				node.rightSon.father = None
				self.root = node
		else:
			if node.hasLeftSon():
				node.leftSon.father = node.father
				if node.data <= node.father.data:
					node.father.leftSon = node.leftSon
				else:
					node.father.rightSon = node.leftSon
			else:
				node.rightSon.father = node.father
				if node.data <= node.father.data:
					node.father.leftSon = node.rightSon
				else:
					node.father.rightSon = node.rightSon
		return

	def removeTS(self, node):
		predecessor = self.predecessor(node=node)
		node.data = predecessor.data

		if predecessor.isLeaf():
			self.removeNS(predecessor)
		else:
			self.removeOS(predecessor)
		return


	def rotate(self, node):
		if node.hasRightSon() and node.rightSon.hasRightSon():
			self.rotateLeft(node)
		elif node.hasLeftSon() and node.leftSon.hasLeftSon():
			self.rotateRight(node)
		elif node.hasLeftSon() and node.leftSon.hasRightSon():
			self.doubleRotateRight(node)
		else:
			self.doubleRotateLeft(node)

		return self.calculateBalanceFactor(self.root)


	def rotateLeft(self, node):
		swap = node.rightSon

		## Troca do filho direito de "node" ##
		# swap.leftSon.father = node
		# node.rightSon = swap.rightSon

		## Troca do pai de "node" ##
		swap.leftSon = node
		swap.father = node.father
		node.father = swap

		## Ajuste do ponteiro do pai de "node" ##
		if node is self.root:
			self.root = swap
		elif node is node.father.leftSon:
			node.father.leftSon = swap
		else:
			node.father.rightSon = swap
		return

	def rotateRight(self, node):
		swap = node.leftSon

		## Troca do filho esquerdo de "node" ##
		# swap.rightSon.father = node
		# node.leftSon = swap.rightSon

		## Troca do pai de "node" ##
		swap.rightSon = node
		swap.father = node.father
		node.father = swap

		## Ajuste do ponteiro do pai de "node" ##
		if node is self.root:
			self.root = swap
		elif node is node.father.leftSon:
			node.father.leftSon = swap
		else:
			node.father.rightSon = swap
		return

	def doubleRotateLeft(self, node):
		swap = node.rightSon

		swap.leftSon.father = node
		node.rightSon = swap.leftSon
		swap.father = node.rightSon
		swap.leftSon = None
		swap.rightSon = None

		self.rotateLeft(node)
		return

	def doubleRotateRight(self, node):
		swap = node.leftSon

		swap.rightSon.father = node
		node.leftSon = swap.rightSon
		swap.father = node.leftSon
		swap.leftSon = None
		swap.rightSon = None

		self.rotateRight(node)
		return


############### MAIN ###############


############### TESTES ###############

def amostras (tamanho):
	from random import sample
	population = list(range(tamanho * 100))
	amostra = sample(population, tamanho)
	# print(amostra)
	return amostra

from time import perf_counter as pc
from random import sample

for _ in range(1):
	a = pc()
	# amostra = amostras(100000)
	amostra = [405, 46, 692, 344, 530, 131, 727, 908, 701, 923]
	b = pc()
	createSampleT = b - a

	arvoreAVL = AVLTree()
	c = pc()

	for item in amostra:
		arvoreAVL.insertNode(item)
	d = pc()
	insertT = d - c

	# print(amostra)




	e = pc()
	# valor, *_ = sample(amostra, 1)
	arvoreAVL.calculateHeight(arvoreAVL.root)
	e1 = pc()
	assignT = e1 - e

	# no = arvore.searchValue(valor)
	f = pc()
	# print(no.data)
	arvoreAVL.calculateBalanceFactor(arvoreAVL.root)
	g = pc()
	searchT = g - f

	# # arvore.order()
	# # print("\n")
	# h = pc()
	# orderT = h - g
	# i = pc()
	# max = arvore.maximum().data
	# arvoreAVL.order(method="pre",printBalanceFactor=False, printHeight=False)
	# j = pc()
	# maximoT = j - i

	# min = arvore.minimum().data
	# k = pc()
	# minimoT = k - j

	# pred = arvore.predecessor(valor)
	# l = pc()
	# predT = l - k
	# suces = arvore.successor(valor)
	# m = pc()
	# sucessT = m - l
	# n = pc()
	# arvore.remove(valor)
	# o = pc()
	# remT = o - n
	# # print("Valor que deveria ser removido : ", arvore.searchValue(valor).data)


# 	print("Root", arvoreAVL.root.data)
# 	print("Max", max)
# 	print("Min", min)
# 	if pred is not None:
# 		print("Predecessor", pred.data)
# 	if suces is not None:
# 		print("Sucessor", suces.data)
# 	print(amostra)
# 	print(arvoreAVL)

# print("""
# Criação de amostra : {:.5f}s
# Insercao de elementos na arvore : {:.5f}s
# Busca do valor : {:.5f}s
# Impressao da Arvore : {:.5f}s
# Maximo da Arvore : {:.5f}s
# Minimo da Arvore : {:.5f}s
# Predecessor da Arvore : {:.5f}s
# Sucessor da Arvore : {:.5f}s
# Remover da Arvore : {:.5f}s

# ----------------------------------------------
# """.format(createSampleT, insertT, searchT, orderT, maximoT, minimoT, predT, sucessT, remT))

print("""
Insercao de elementos na arvore : {:.5f}s
Altura dos nodes : {:.5f}s
Fator de balanceamento : {:.5f}s
----------------------------------------------
""".format(insertT, assignT, searchT))