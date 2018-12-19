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
		return print("{} : {}".format(self.key, self.name))
	
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
		return self.__books.items()

	@books.setter
	def books(self, bookID, title):
		self.__books[bookID] = title
		return

	def returnBook(self, bookID=None, title=None):
		if bookID is None and title is None:
			raise ValueError("Enter a valid ID or Title!")
		elif bookID is None:
			for bookKey, bookTitle in self.__books.items():
				if bookTitle == title:
					bookID = bookKey
		try:
			self.__books.pop(bookID)
			self.__loans -= 1
		except:
			return print("User didn't take this book!")

	def withdrawBook(self, bookID, title):
		if self.loans > 5:
			return print("Reached the max number of books' loan! Return one first.")
		else:
			self.books = (bookID, title)
			self.loans += 1


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
		return print("{} : {} -- Copies:{} -- Borrowed Copies: {}".format(self.key, self.title, self.copies, self.borrowedCopies))
	
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
		self.availableCopies = self.copies - self.borrowedCopies
		
		if self.availableCopies > 0:
			self.isAvailable = True
		else:
			self.isAvailable = False
	
	def returnBook(self):
		self.borrowedCopies -= 1
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
		self.__father = self
		self.__leftSon = self
		self.__rightSon = self

	@property
	def color(self):
		return self.__color

class RWTNode:
	
	def __init__(self, data, color, NoneNode):
		self.__color = color
		self.__data = data
		self.__height = NoneNode
		self.__father = NoneNode
		self.__leftSon = NoneNode
		self.__rightSon = NoneNode
		self.NoneNode = NoneNode

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
	def height(self):
		return self.__height

	@height.setter
	def height(self, height):
		self.__height = height

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

	def hasLeftSon(self):
		return self.leftSon is not self.NoneNode

	def hasRightSon(self):
		return self.rightSon is not self.NoneNode

	def isLeaf(self):
		return self.leftSon is self.NoneNode and self.rightSon is self.NoneNode

	def sons(self):
		sons = 0
		if self.hasLeftSon():
			sons += 1
		if self.hasRightSon():
			sons += 1
		return sons


class RedWhiteTree():
	NoneNode = RWTNoneNode()

	def __init__(self):
		self.__root = self.NoneNode

	@property
	def root(self):
		return self.__root

	@root.setter
	def root(self, value):
		self.__root = value

#   #####################################################################
#  # TEST	  TEST		TEST	  TEST	    TEST    	TEST	  TEST #
# #####################################################################

	def __str__(self):
		self.inOrderRecEngine(self.root)
		return "\n"

	def isEmpty(self):
		if self.root is self.NoneNode:
			return True
		else:
			return False

	def isOnlyRoot(self):
		return self.root.isLeaf()

	def insertNode(self, value):
		newNode = RWTNode(value, "red", self.NoneNode)
		node = self.root
		father = self.NoneNode

		while node is not self.NoneNode:
			father = node
			if value.data.key <= node.data.key:
				node = node.leftSon
			else:
				node = node.rightSon

		newNode.father = father
		if father is self.NoneNode:
			self.root = newNode
		else:
			if value.key <= father.data.key:
				father.leftSon = newNode
			else:
				father.rightSon = newNode

		pass # self.insertFix(newNode)
		return


	def insertNodeRec(self, value, node, father=None):
		if node is not self.NoneNode:
			if value.key <= node.data.key:
				self.insertNodeRec(value, node.leftSon, node)
			else:
				self.insertNodeRec(value, node.rightSon, node)
		else:
			newNode = RWTNode(value, "red", self.NoneNode)
			newNode.father = father

			if father is None:
				father = self.NoneNode

			if father is not self.NoneNode:
				if value.key <= father.data.key:
					father.leftSon = newNode
				else:
					father.rightSon = newNode
			else:
				self.root = newNode

			pass # self.insertFix(newNode)
			return


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
			return print("The tree is empty!")
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
			print(node.data,end=" ")
			self.inOrderRecEngine(node.leftSon)
			self.inOrderRecEngine(node.rightSon)

	def posOrderRecEngine(self, node):
		if node is not self.NoneNode:
			self.inOrderRecEngine(node.leftSon)
			self.inOrderRecEngine(node.rightSon)
			print(node.data,end=" ")


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


	def calculateTreeHeight(self, node):
		# print("Tree height...")
		if node is self.NoneNode:
			return -1
		else:
			leftHeight = self.calculateTreeHeight(node.leftSon)
			rightHeight = self.calculateTreeHeight(node.rightSon)

			if leftHeight >= rightHeight:
				node.height = leftHeight + 1
			else:
				node.height = rightHeight + 1

			return node.height



#   #####################################################################
#  # ERROR	  ERROR		ERROR	  ERROR	    ERROR      ERROR	 ERROR #
# #####################################################################

	def balance(self, node):
		# print("Balancing... ... ...")
		while node is not None:
			self.calculateHeightAscendent(node)
			balanceFactor = self.nodeHeight(node.leftSon) - self.nodeHeight(node.rightSon)

			if balanceFactor < -1 or balanceFactor > 1:
				if node.hasRightSon() and node.rightSon.hasRightSon():
					self.rotateLeft(node)
				elif node.hasLeftSon() and node.leftSon.hasLeftSon():
					self.rotateRight(node)
				elif node.hasLeftSon() and node.leftSon.hasRightSon():
					self.doubleRotateRight(node)
				else:
					self.doubleRotateLeft(node)
			else:
				node = node.father
		return


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
		# print("Rotated LEFT...")
		self.calculateTreeHeight(swap)

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

		# print("Rotated RIGHT...")
		self.calculateTreeHeight(swap)

		return swap


	def doubleRotateLeft(self, node):
		# print("Rotated DOUBLE LEFT...")
		self.rotateRight(node.rightSon) # Rotacao convencional a direita do filho direito
		self.rotateLeft(node) # Rotacao convencional a esquerda
		return

	def doubleRotateRight(self, node):
		# print("Rotated DOUBLE RIGHT...")
		self.rotateLeft(node.leftSon) # Rotacao convencional a esquerda do filho esquerdo
		self.rotateRight(node) # Rotacao convencional a direita
		return





#   #####################################################################
#  # REDACT	  REDACT		REDACT		REDACT		REDACT		REDACT #
# #####################################################################



	def Insert_Fixup(self, z):
		while z.get_p().get_cor() == "RED":
			if z.get_p() == z.get_p().get_p().get_left():
				y = z.get_p().get_p().get_right()
				if y.get_cor() == "RED":
					z.get_p().set_cor("BLACK")
					y.set_cor("BLACK")
					z.get_p().get_p().set_cor("RED")
					z = z.get_p().get_p()
				else:
					if z == z.get_p().get_right():
						z = z.get_p()
						self.Left_Rotate(z)
					z.get_p().set_cor("BLACK")
					z.get_p().get_p().set_cor("RED")
					self.Right_Rotate(z.get_p().get_p())
			else:
				y = z.get_p().get_p().get_left()
				if y.get_cor() == "RED":
					z.get_p().set_cor("BLACK")
					y.set_cor("BLACK")
					z.get_p().get_p().set_cor("RED")
					z = z.get_p().get_p()
				else:
					if z == z.get_p().get_left():
						z = z.get_p()
						self.Right_Rotate(z)
					z.get_p().set_cor("BLACK")
					z.get_p().get_p().set_cor("RED")
					self.Left_Rotate(z.get_p().get_p())
		self.root().set_cor("BLACK")


	def removeFix(self, x):
		while x != self.root() and x.get_cor() == "BLACK":
			if x == x.get_p().get_left():
				w = x.get_p().get_right()
				if w.get_cor() == "RED":
					w.set_cor("BLACK")
					x.get_p().set_cor("RED")
					self.Left_Rotate(x.get_p())
					w = x.get_p().get_right()
				if w.get_left().get_cor() == "BLACK" and w.get_right().get_cor() == "BLACK":
					w.set_cor("RED")
					x = x.get_p()
				else:
					if w.get_right() == "BLACK":
						w.get_left().set_cor("BLACK")
						w.set_cor("RED")
						self.Right_Rotate(w)
						w = x.get_p().get_right()
						w.set_cor(x.get_p().get_cor())
						x.get_p.set_cor("BLACK")
						w.get_right().set_cor("BLACK")
						self.Left_Rotate(x.get_p())
						x = self.root()
			else:
				w = x.get_p().get_left()
				if w.get_cor() == "RED":
					w.set_cor("BLACK")
					x.get_p().set_cor("RED")
					self.Right_Rotate(x.get_p())
					w = x.get_p().get_left()
				if w.get_right().get_cor() == "BLACK" and w.get_left().get_cor() == "BLACK":
					w.set_cor("RED")
					x = x.get_p()
				else:
					if w.get_left() == "BLACK":
						w.get_right().set_cor("BLACK")
						w.set_cor("RED")
						self.Left_Rotate(w)
						w = x.get_p().get_left()
						w.set_cor(x.get_p().get_cor())
						x.get_p.set_cor("BLACK")
						w.get_left().set_cor("BLACK")
						self.Right_Rotate(x.get_p())
						x = self.root()
		x.set_cor("BLACK")

	def remove(self,key):
		z = self.SearchId(self.root(), key)
		if z == self.NoneNode:
			return 0
		if z.get_left() == self.NoneNode or z.get_right() == self.NoneNode:
			y = z
		else:
			y = self.Sucessor(z)
		if y.get_left() != self.NoneNode:
			x = y.get_left()
		else:
			x = y.get_right()
		if x != self.NoneNode:
			x.set_p(y.get_p())
		if y.get_p() == self.NoneNode:
			self.root(x)
		elif y == y.get_p().get_left():
			y.get_p().set_left(x)
		else:
			y.get_p().set_right(x)
		if y != z:
			z.set_key(y.get_key())
		if y.get_cor() == "BLACK":
			self.removeFix(x)
		return y

	def Left_Rotate(self, x):
		y = x.get_right()
		x.set_right(y.get_left())
		y.get_left().set_p(x)
		y.set_p(x.get_p())

		if x.get_p() == self.NoneNode:
			y.get_left().set_p(x)
		y.set_p(x.get_p())
		if x.get_p() == self.NoneNode:
			self.root(y)
		elif x == x.get_p().get_left():
			x.get_p().set_left(y)
		else:
			x.get_p().set_right(y)
		y.set_left(x)
		x.set_p(y)

	def Right_Rotate(self, x):
		y = x.get_left()
		x.set_left(y.get_right())
		y.get_right().set_p(x)
		y.set_p(x.get_p())
		if x.get_p() == self.NoneNode:
			y.get_right().set_p(x)
		y.set_p(x.get_p())
		if x.get_p() == self.NoneNode:
			self.root(y)
		elif x == x.get_p().get_right():
			x.get_p().set_right(y)
		else:
			x.get_p().set_left(y)
		y.set_right(x)
		x.set_p(y)