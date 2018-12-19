# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO -- UFRPE
# DEPARTAMENTO DE ESTATISTICA E INFORMATICA -- DEINFO
# SISTEMAS DE INFORMAÇÃO -- BSI

# ALGORITMOS E ESTRUTURA DE DADOS
# PROF. TIAGO FERREIRA
# ALUNO ALDEMAR S R FILHO


### BIBLIOTECA DE FUNCOES ###

from libClasses import Book, User, RedWhiteTree
from time import sleep
import os

# usersBase = RedWhiteTree()
# booksBase = RedWhiteTree()

def cleanScreen():
	# LIMPA A TELA
	return os.system('cls' if os.name == 'nt' else 'clear')

def validateEntry(question, start, end):
	# VALIDA A ENTRADA DE ACORDO COM UMA FAIXA DE INTEIROS RECEBIDA
	while True:
		try:
			value = int(input(question))
			if start <= value <= end:
				return(value)
			else:
				pauseForRead('\033[91mINVALID VALUE. PLEASE ENTER BETWEEN {} AND {}\033[0m'.format(start, end), 2)
		except ValueError:
			print()
			pauseForRead('\033[91mINVALID VALUE. PLEASE ENTER BETWEEN {} AND {}\033[0m'.format(start, end), 2)
	return

def pauseForRead(text, time=1.5, end="\n"):
	# PAUSA PROGRAMA PARA LEITURA DE MENSAGENS
	print ('{}'.format(text), end=end)
	sleep(time)


def loadBooksDatabase():
	booksBase = RedWhiteTree()

	currentFileDir = os.path.dirname(__file__)
	filePath = os.path.join(currentFileDir, "books.base")

	with open(filePath,"r",encoding = "UTF-8") as booksFile:
		booksFileContent = booksFile.readlines()

	for item  in booksFileContent:
		book = Book(*item.split())
		booksBase.insertNode(book)
	return booksBase

def loadUsersDatabase():
	usersBase = RedWhiteTree()

	currentFileDir = os.path.dirname(__file__)
	filePath = os.path.join(currentFileDir, "users.base")

	with open(filePath,"r",encoding = "UTF-8") as usersFile:
		usersFileContent = usersFile.readlines()

	for item  in usersFileContent:
		user = User(*item.split())
		usersBase.insertNode(user)
	return usersBase


def addUser(usersBase):
	userName = input("\nNome: ")
	userPassword = input("Senha: ")
	admin = input("Admin: (y/N)  ")
	if admin.lower() == "y":
		admin = True
	else:
		admin = False
	user = User(userName, userPassword, admin=admin)
	userID = user.key
	cleanScreen()
	pauseForRead("\nUser \033[91m\"{}\"\033[0m registred at the id \033[91m\"{}\"\033[0m".format(userName, userID), time=3)
	usersBase.insertNode(user)


def addBook(booksBase):
	cleanScreen()
	bookTitle = input("Titulo do livro: ")
	book = Book(bookTitle)
	bookID = book.key
	try:
		if booksBase.searchValue(book) is not booksBase.NoneNode:
			return pauseForRead("\nBook already registered.")
	except ValueError:
		pass
	booksBase.insertNode(book)
	pauseForRead("\nBook registred at the id \"{}\".".format(bookID))


def listBooks(booksBase):
	cleanScreen()
	print("\n--------------------  LIVROS  --------------------\n")
	print(booksBase)
	print("\n-----------------------  X  -----------------------")
	input("Press Enter to return...")

def borrowedBooks(usersBase, loggedUser=None):
	if loggedUser is None:
		return pauseForRead("No user logged.")

	print("\n--------------------  LIVROS  --------------------\n")
	for bookID, bookTitle in loggedUser.books.items():
		print("{} -- {}".format(bookID, bookTitle))
	print("\n-----------------------  X  -----------------------")
	input("Press Enter to return...")


def withdrawBook(usersBase, booksBase, loggedUser):
	user = loggedUser

	if user is usersBase.NoneNode:
		return pauseForRead("Invalid user ID.")

	bookID = -1

	while bookID != 0:
		cleanScreen()
		bookID = int(input("Book ID: (0 - exit)   "))
		if bookID == 0:
			return
		book = booksBase.searchKey(bookID)
		if book is booksBase.NoneNode:
			pauseForRead("Invalid book ID. Try again.")
		else:
			break

	if book.isAvailable:
		if user.loans >= 5:
			pauseForRead("\nYou have passed loans' limit.")
		else:
			user.withdrawBook(book.key, book.title)
			book.copies -= 1
			pauseForRead("\nBook withdrawn.")
	else:
		pauseForRead("\nUnavailable book.")


def returnBook(usersBase, booksBase, loggedUser):
	user = loggedUser

	if user is usersBase.NoneNode:
		return pauseForRead("Invalid user ID.")

	bookID = -1
	while bookID != 0:
		print("\nSelect the book to return (0 - exit)")

		for bookCode, bookTitle in user.books.items():
			print("{:d} : {:s}".format(bookCode, bookTitle))

		bookID = int(input("Book ID: "))

		if bookID == 0:
			return

		book = booksBase.searchKey(bookID)
		if book is booksBase.NoneNode:
			pauseForRead("\nInvalid book ID. Try again.")
			continue
		else:
			break

	user.returnBook(book.key)
	book.returnBook()
	pauseForRead("\nBook returned.")


def removeUser(usersBase):
	while True:
		cleanScreen()
		print("\n{:-^30}\n".format("  Users  "))
		print(usersBase)
		
		userKey = int(input("User ID: (0 - Exit)   "))
		if userKey == 0:
			return

		user = usersBase.searchKey(userKey).data

		if user is usersBase.NoneNode:
			pauseForRead("\nInvalid user!")
			continue
		else:
			break

	while True:
		userPassword = input("Password: (0 - exit)   ")

		if userPassword == "0":
			return

		if userPassword == user.password:
			usersBase.removeNode(user.key)
			return pauseForRead("\nUser removed.")
		else:
			pauseForRead("Invalid password.", end="\r")
			continue

def removeBook(booksBase):
	cleanScreen()
	print("\n{:-^30}\n".format("  Collection  "))
	print(booksBase)

	while True:
		bookKey = int(input("Book ID: (0 - Exit)   "))

		if bookKey == 0:
			return

		book = booksBase.searchKey(bookKey).data
		if book is booksBase.NoneNode:
			pauseForRead("\nInvalid book ID.")
			continue
		else:
			break

	if book.borrowedCopies == 0:
		booksBase.removeNode(bookKey)
		pauseForRead("\nBook removed.\n")
	else:
		pauseForRead("\nYou can't remove books who has borrowed copies!")


def userLogin(usersBase):
	while True:
		userKey = int(input("\nUser ID: (0 - Exit)   "))
		if userKey == 0:
			return

		if usersBase.isEmpty():
			return pauseForRead("Empty tree!")

		user = usersBase.searchKey(userKey).data
		if user is usersBase.NoneNode:
			pauseForRead("\nInvalid user ID.")
			print("\r\r")
			continue
		else:
			break

	while True:
		password = int(input("\nPassword: (0 - Exit)   "))

		if password == 0:
			return

		if password == user.password:
			pauseForRead("\nUSER LOGGED.")
			return userMenu(user, usersBase, booksBase)
		else:
			pauseForRead("Invalid password!", end="\r")
			print("\r")

def adminLogin(usersBase):
	while True:
		cleanScreen()
		userKey = int(input("\nUser ID: (0 - Exit)   "))
		if userKey == 0:
			return

		if usersBase.isEmpty():
			return pauseForRead("Empty tree!")

		user = usersBase.searchKey(userKey).data
		if user is usersBase.NoneNode:
			pauseForRead("\nInvalid user ID.")
			print("\r")
			continue
		elif not user.isAdmin:
			return pauseForRead("User isn't a admin.")
		else:
			break

	while True:
		password = int(input("Password: (0 - Exit)   "))

		if password == 0:
			return

		if password == user.password:
			pauseForRead("ADMIN LOGGED.")
			return adminMenu(user, booksBase)
		else:
			pauseForRead("Invalid password!", end="\r")
			



def MainMenu(usersBase, booksBase):
	usersBase = usersBase
	booksBase = booksBase

	MainMenu = {1: (adminLogin, (usersBase)),
				2: (userLogin, (usersBase)),
				3: (addUser, (usersBase)),
				4: (removeUser, (usersBase))
				}

	option = -1
	while True:
		cleanScreen()
		print('''
-----------------------
-     \033[1m   MENU    \033[0m     -
-----------------------
 1 : Admin Login
 2 : User Login
 3 : Create User
 4 : Remove User
-----------------------
 0 : EXIT
-----------------------
''')
		option = validateEntry("Option: ",0,4)
		if option == 0:
			return None
		function, arguments = MainMenu[option]
		function(arguments)


def userMenu(loggedUser, usersBase, booksBase):
	UserMenu = {1: (borrowedBooks, (usersBase, loggedUser)),
				2: (withdrawBook, (usersBase, booksBase, loggedUser)),
				3: (returnBook, (usersBase, booksBase, loggedUser))
				}

	option = -1
	while True:
		cleanScreen()
		print('''
-----------------------
-     \033[1m   USER    \033[0m     -
-----------------------
 1 : Borrowed Books
 2 : Withdraw Books
 3 : Return Books
-----------------------
 0 : EXIT
-----------------------
''')
		option = validateEntry("Option: ",0,3)
		if option == 0:
			loggedUser = usersBase.NoneNode
			return loggedUser, usersBase, booksBase
		function, arguments = UserMenu[option]
		function(*arguments)

def adminMenu(loggedUser, booksBase):
	AdminMenu = {1: (addBook, (booksBase)),
				 2: (removeBook, (booksBase)),
				 3: (listBooks, (booksBase))
				}

	option = -1
	while True:
		cleanScreen()
		print('''
-----------------------
-     \033[1m   ADMIN   \033[0m     -
-----------------------
 1 : Add Book
 2 : Remove Book
 3 : List Books
-----------------------
 0 : EXIT
-----------------------
''')
		option = validateEntry("Option: ",0,3)
		if option == 0:
			loggedUser = usersBase.NoneNode
			return loggedUser, booksBase
		function, arguments = AdminMenu[option]
		function(arguments)

booksBase = loadBooksDatabase()
usersBase = loadUsersDatabase()