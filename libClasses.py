# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO -- UFRPE
# DEPARTAMENTO DE ESTATISTICA E INFORMATICA -- DEINFO
# SISTEMAS DE INFORMAÇÃO -- BSI

# ALGORITMOS E ESTRUTURA DE DADOS
# PROF. TIAGO FERREIRA
# ALUNO ALDEMAR S R FILHO


### BIBLIOTECA DE CLASSES ###


class User:
	userSequential = 0

	def __init__(self, name, password, admin=False):
		User.userSequential += 1
		self.__key = User.userSequential
		self.__name = name
		self.__admin = admin
		self.__password = password
		self.__loans = 0
		self.__books = {}


	def __str__(self):
		return "{} : {} -- Pendent Books: {}".format(self.key, self.name, self.loans)

	@property
	def key(self):
		return self.__key

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@property
	def password(self):
		return self.__password

	@password.setter
	def password(self, password):
		self.__password = password

	@property
	def isAdmin(self):
		return self.__admin

	@property
	def loans(self):
		return self.__loans

	@property
	def booksID(self):
		return self.__books.keys()

	@property
	def bookNames(self):
		return self.__books.values()

	@property
	def books(self):
		return self.__books

	@property
	def booksList(self):
		return self.books

	@books.setter
	def books(self, item):
		bookID, title = item
		self.__books[bookID] = title
		return

	def returnBook(self, bookID=None, title=None):
		if bookID is None and title is None:
			print("Enter a valid ID or Title!")
		elif bookID is None:
			for bookKey, bookTitle in self.__books.items():
				if bookTitle == title:
					bookID = bookKey
		try:
			self.books.pop(bookID)
			self.__loans -= 1
		except:
			return print("User didn't take this book!")

	def withdrawBook(self, bookID, title):
		if self.loans > 5:
			return print("Reached the max number of books' loan! Return one first.")
		else:
			self.books = (bookID, title)
			self.__loans += 1


class Book:
	bookSequential = 0

	def __init__(self, title, copies=1):
		Book.bookSequential += 1
		self.__key = Book.bookSequential
		self.__title = title
		self.__copies = copies
		self.__borrowedCopies = 0
		self.__availableCopies = copies
		self.__available = True

	def __str__(self):
		return "{} : {} -- Copies:{} -- Borrowed Copies: {}".format(self.key, self.title, self.copies, self.borrowedCopies)

	@property
	def key(self):
		return self.__key

	@property
	def title(self):
		return self.__title

	@property
	def copies(self):
		return self.__copies

	@property
	def borrowedCopies(self):
		return self.__borrowedCopies

	@borrowedCopies.setter
	def borrowedCopies(self, returned):
		self.__borrowedCopies = returned

	@property
	def availableCopies(self):
		return self.__availableCopies

	def __updateAvailableCopies(self):
		self.__availableCopies = self.copies - self.borrowedCopies

		if self.availableCopies > 0:
			self.isAvailable = True
		else:
			self.isAvailable = False

	def returnBook(self):
		self.borrowedCopies -= 1
		self.__updateAvailableCopies()

	def withdrawBook(self):
		self.borrowedCopies += 1
		self.__updateAvailableCopies()




	@property
	def isAvailable(self):
		return self.__available

	@isAvailable.setter
	def isAvailable(self, status):
		self.__available = status


class RWTNoneNode:
	def __init__(self):
		self.__color = "white"
		self.__data = None
		self.__father = self
		self.__leftSon = self
		self.__rightSon = self

	def __str__(self):
		return ""

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, color):
		self.color = color

	@property
	def data(self):
		return self.__data

	@property
	def father(self):
		return self.__father

	@father.setter
	def father(self, value):
		self.__father = value

	@property
	def leftSon(self):
		return self.__leftSon

	@leftSon.setter
	def leftSon(self, value):
		self.leftSon = value

	@property
	def rightSon(self):
		return self.__rightSon

	@rightSon.setter
	def rightSon(self, value):
		self.__rightSon = value

class RWTNode:
	def __init__(self, data=None, color="white"):
		self.__color = color
		self.__data = data
		self.__father = None
		self.__leftSon = None
		self.__rightSon = None

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, color):
		self.__color = color

	@property
	def data(self):
		return self.__data

	@data.setter
	def data(self, data):
		self.__data = data

	@property
	def father(self):
		return self.__father

	@father.setter
	def father(self, value):
		self.__father = value

	@property
	def leftSon(self):
		return self.__leftSon

	@leftSon.setter
	def leftSon(self, value):
		self.__leftSon = value

	@property
	def rightSon(self):
		return self.__rightSon

	@rightSon.setter
	def rightSon(self, value):
		self.__rightSon = value

class RedWhiteTree():
	NoneNode = RWTNode()

	def __init__(self):
		self.__root = self.NoneNode

	def __str__(self):
		self.inOrderRecEngine(self.root)
		return ""

	@property
	def root(self):
		return self.__root

	@root.setter
	def root(self, value):
		self.__root = value

	def isEmpty(self):
		if self.root is self.NoneNode:
			return True
		else:
			return False

	def isOnlyRoot(self):
		return self.root.isLeaf()

	def insertNode(self, value):
		newNode = RWTNode(value, "red")
		node = self.root
		father = self.NoneNode

		while node is not self.NoneNode:
			father = node
			if newNode.data.key <= node.data.key:
				node = node.leftSon
			else:
				node = node.rightSon

		newNode.father = father
		if father is self.NoneNode:
			self.root = newNode
		else:
			if newNode.data.key <= father.data.key:
				father.leftSon = newNode
			else:
				father.rightSon = newNode

		newNode.leftSon = self.NoneNode
		newNode.rightSon = self.NoneNode
		newNode.color = "red"
		self.insertFix(newNode)
		return


	def insertFix(self, node):
		while node.father.color == "red":
			if node.father == node.father.father.leftSon:

				y = node.father.father.rightSon
				if y.color == "red":
					node.father.color = "white"
					y.color = "white"
					node.father.father.color = "red"
					node = node.father.father

				else:
					if node == node.father.rightSon:
						node = node.father
						self.rotateLeft(node)
					node.father.color = "white"
					node.father.father.color = "red"
					self.rotateRight(node.father.father)

			else:
				y = node.father.father.leftSon
				if y.color == "red":
					node.father.color = "white"
					y.color = "white"
					node.father.father.color = "red"
					node = node.father.father

				else:
					if node == node.father.leftSon:
						node = node.father
						self.rotateRight(node)

					node.father.color = "white"
					node.father.father.color = "red"
					self.rotateLeft(node.father.father)

		self.root.color = "white"

	def transplantNode(self, node, node2):
		if node.father is self.NoneNode:
			self.root = node2
		elif node is node.father.leftSon:
			node.father.leftSon = node2
		else:
			node.father.rightSon = node2

		node2.father = node.father


	def removeNode(self, key):
		node = self.searchKey(key)

		swap = node
		swapOriginColor = swap.color

		if node.leftSon is self.NoneNode:
			swap2 = node.rightSon
			self.transplantNode(node, node.rightSon)
		elif node.rightSon is self.NoneNode:
			swap2 = node.leftSon
			self.transplantNode(node, node.leftSon)
		else:
			swap = self.minimum(node.rightSon)
			swapOriginColor = swap.color
			swap2 = swap.rightSon

			if swap.father is node:
				swap2.father = swap
			else:
				self.transplantNode(swap, swap.rightSon)
				swap.rightSon = node.rightSon
				swap.rightSon.father = swap

			self.transplantNode(node, swap)
			swap.leftSon = node.leftSon
			swap.leftSon.father = swap
			swap.color = node.color

		if swapOriginColor == "white":
			self.removesFix(swap2)


	def removesFix(self, node):
		while node is not self.root and node.color == "white":
			if node is node.father.leftSon:
				swap = node.father.rightSon

				if swap.color == "red": # Caso 1
					swap.color = "white"
					node.father.color = "red"

					self.rotateLeft(node.father)

					swap = node.father.rightSon

				if swap.leftSon.color == "white" and swap.rightSon.color == "white": # Caso 2
					swap.color = "red"
					node = node.father
				else: # Caso 3
					if swap.rightSon.color == "white":
						swap.leftSon.color = "white"
						swap.color = "red"

						self.rotateRight(swap)
						swap = node.father.rightSon

					swap.color = node.father.color
					node.father.color = "white"
					swap.rightSon.color = "white"

					self.rotateLeft(node.father)

					node = self.root
			else:
				swap = node.father.leftSon

				if swap.color == "red": # Caso 1
					swap.color = "white"
					node.father.color = "red"

					self.rotateRight(node.father)

					swap = node.father.leftSon

				if swap.rightSon.color == "white" and swap.leftSon.color == "white": # Caso 2
					swap.color = "red"
					node = node.father

				else: # Caso 3
					if swap.leftSon.color == "white":
						swap.rightSon.color = "white"
						swap.color = "red"

						self.rotateLeft(swap)
						swap = node.father.leftSon

					swap.color = node.father.color
					node.father.color = "white"
					swap.leftSon.color = "white"
					self.rotateRight(node.father)
					node = self.root

		node.color = "white"


	def searchValue(self, value):
		if self.isEmpty():
			return print("The tree is empty!")
		else:
			node = self.root
			while node is not self.NoneNode:
				if value.key < node.data.key:
					node = node.leftSon
				elif value.key > node.data.key:
					node = node.rightSon
				else:
					return node

			return self.NoneNode

	def searchKey(self, key):
		if self.isEmpty():
			print("The tree is empty!")
			return self.NoneNode
		else:
			node = self.root
			while node is not self.NoneNode:
				if key < node.data.key:
					node = node.leftSon
				elif key > node.data.key:
					node = node.rightSon
				else:
					return node

			return self.NoneNode


	def order(self, node=None, method="ino"):
		if node is None:
			node = self.root

		if method.lower() == "ino":
			self.inOrderRecEngine(node)
		elif method.lower() == "pre":
			self.preOrderRecEngine(node)
		elif method.lower() == "pos":
			self.posOrderRecEngine(node)
		else:
			return print("Order method not valid!")


	def inOrderRecEngine(self, node):
		if node is not self.NoneNode:
			self.inOrderRecEngine(node.leftSon)
			print("{}".format(node.data))
			self.inOrderRecEngine(node.rightSon)

	def preOrderRecEngine(self, node):
		if node is not self.NoneNode:
			print("{}".format(node.data))
			self.inOrderRecEngine(node.leftSon)
			self.inOrderRecEngine(node.rightSon)

	def posOrderRecEngine(self, node):
		if node is not self.NoneNode:
			self.inOrderRecEngine(node.leftSon)
			self.inOrderRecEngine(node.rightSon)
			print("{}".format(node.data))


	def maximum(self, node=None):
		if node is None:
			node = self.root

		if self.isEmpty():
			return print("The tree is empty!")
		else:
			while node.rightSon is not self.NoneNode:
				node = node.rightSon
			return node

	def minimum(self, node=None):
		if node is None:
			node = self.root

		if self.isEmpty():
			return print("The tree is empty!")
		else:
			while node.leftSon is not self.NoneNode:
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
			return print("Root hasn't predecessors!")

		if node.hasLeftSon():
			return self.maximum(node.leftSon)
		else:
			son = node
			node = node.father
			while (node is not self.NoneNode) and (son is node.leftSon):
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
			while (node is not self.NoneNode) and (son is node.rightSon):
				son = node
				node = node.father

			if node is self.NoneNode:
				print("Node hasn't successors!")
				return
			else:
				return node


	def rotateLeft(self, node):
		swap = node.rightSon
		node.rightSon = swap.leftSon

		if swap.leftSon is not self.NoneNode:
			swap.leftSon.father = node

		swap.father = node.father

		if node.father is self.NoneNode:
			self.root = swap
		elif node is node.father.leftSon:
			node.father.leftSon = swap
		else:
			node.father.rightSon = swap

		swap.leftSon = node
		node.father = swap
		return swap

	def rotateRight(self, node):
		swap = node.leftSon
		node.leftSon = swap.rightSon

		if swap.rightSon is not self.NoneNode:
			swap.rightSon.father = node

		swap.father = node.father

		if node.father is self.NoneNode:
			self.root = swap
		elif node is node.father.leftSon:
			node.father.leftSon = swap
		else:
			node.father.rightSon = swap

		swap.rightSon = node
		node.father = swap
		return swap