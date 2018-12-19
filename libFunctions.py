# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO -- UFRPE
# DEPARTAMENTO DE ESTATISTICA E INFORMATICA -- DEINFO
# SISTEMAS DE INFORMAÇÃO -- BSI

# ALGORITMOS E ESTRUTURA DE DADOS
# PROF. TIAGO FERREIRA
# ALUNO ALDEMAR S R FILHO


### BIBLIOTECA DE FUNCOES ###

from libClasses import Book, User, RedWhiteTree
import os, time

usersBase = RedWhiteTree()
booksBase = RedWhiteTree()

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

def pauseForRead(text, time=5):
    # PAUSA PROGRAMA PARA LEITURA DE MENSAGENS
    print ('{}'.format(text))
    time.sleep(time)


def loadBooksDatabase():
	books = RedWhiteTree()
	with open("BaseLivros.txt","r",encoding = "UTF-8") as booksFile:
		booksBase = booksFile.read().splitlines()

	for book in booksBase:
		books.insertNode(book)


def addUser(usersBase):
	userName = input("Nome: ")
	userPassword = input("Senha: ")
	user = User(userName, userPassword)
	userID = user.key
	print("\n USER \"{}\" registred at the id \033[91m\"{}\"\033[0m".format(userName, userID))
	usersBase.Insert(user)


def addBook(booksBase):
	bookTitle = input("Titulo do livro: ")
	book = Book(bookTitle)
	bookID = book.key
	try:
		if booksBase.searchValue(book) is not booksBase.NoneNode:
			return("\nBook already registered.")
	except ValueError:
		pass
	booksBase.Insert(book)
	print("\nBook registred at the id \"{}\".".format(bookID))


def listBooks(booksBase):
    print("\n--------------------  LIVROS  --------------------")
    booksBase.order()    
    print("-----------------------  X  -----------------------")

def borrowedBooks(usersBase,loggedUser):
    if loggedUser is None:
        return pauseForRead("No user logged.")        

    print("\n--------------------  LIVROS  --------------------")

    for bookID, bookTitle in loggedUser.books.items():
        print("{} -- {}".format(bookID, bookTitle))
    
    print("-----------------------  X  -----------------------")


def withdrawBook(usersBase, booksBase, loggedUser):
	user = loggedUser

	if user is usersBase.NoneNode:
		return print("Invalid user ID.")

	bookID = -1

	while bookID != 0:
		cleanScreen()
		bookID = int(input("ID do livro: (0 - exit)"))
		book = booksBase.SearchKey(bookID)
		if book is booksBase.NoneNode:
			print("Invalid book ID. Try again.")
		else:
			break

	if book.isAvailable:
		if user.loans >= 5:
			print("\nYou have passed loans' limit.")
		else:
			user.withdrawBook(book.key, book.title)
			book.copies -= 1
			print("\nBook withdrawn.")
	else:
		print("\nUnavailable book.")


def returnBook(usersBase, booksBase, loggedUser):
	user = loggedUser

	if user is usersBase.NoneNode:
		return print("Invalid user ID.")

	bookID = -1
	while bookID != 0:
		print("\nSelect the book to return (0 - exit)")

		for bookCode, bookTitle in user.books.items():
			print("{:d} : {:s}".format(bookCode, bookTitle))

		bookID = int(input("Book ID: "))
		
		if bookID == 0:
			return

		book = booksBase.SearchKey(bookID)
		if book is booksBase.NoneNode:
			print("\nInvalid book ID. Try again.")
			continue
		else:
			break

	user.returnBook(book.key)
	book.returnBook()
	print("\nBook returned.")
	

def removeUser(usersBase):
	while True:
		userKey = int(input("User ID: "))
		user = usersBase.SearchKey(userKey)
		
		if user is usersBase.NoneNode:
			print("\nInvalid user!")
			continue
		else:
			break
		
	while True:
		userPassword = input("Password: (0 - exit)")

		if userPassword == 0:
			return

		if userPassword == user.password:
			usersBase.remove(user.key)
			return print("\nUser removed.")
		else:
			print("\nInvalid password. Try Again.")
			continue

def removeBook(booksBase):
	print("\nCollection\n")
	print(booksBase)

	while True:
		bookKey = int(input("Book ID: (0 - Exit)"))

		if bookKey == 0:
			return
		
		book = booksBase.SearchKey(bookKey)
		if book is booksBase.NoneNode:
			print("\nInvalid book ID.")
			continue
		else:
			break
			
	if book.borrowedCopies == 0:
		booksBase.remove(bookKey)
		print("\nBook removed.\n")
	else:
		print("\nYou can't remove books who has borrowed copies!")


def userLogin(usersBase):
	while True:		
		userKey = int(input("User ID: (0 - Exit)"))		
		if userKey == 0:
			return

		user = usersBase.SearchKey(userKey)
		if user is usersBase.NoneNode:
			print("\nInvalid user ID.")
			continue
		else:
			break

	while True:
		password = input("Password: (0 - Exit)")

		if password == 0:
			return
		
		if password == user.password:
			print("\nUSER LOGGED.")
			return user

def adminLogin(usersBase):
	
	while True:		
		userKey = input("User ID: (0 - Exit)")
		if userKey == 0:
			return
		
		user = usersBase.searchKey(userKey)
		if user is usersBase.NoneNode:
			print("\nInvalid user ID.")
			continue
		elif not user.isAdmin():
			return print("User isn't a admin.")
		else:
			break

	while True:
		password = input("Password: ")
		
		if password == user.password:
			print("ADMIN LOGGED.")
			return user
		else:
			print("\nInvalid password!")

#   #####################################################################
#  # REDACT	  REDACT		REDACT		REDACT		REDACT		REDACT #
# #####################################################################