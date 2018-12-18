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

def limpaTela():
    # LIMPA A TELA
    return os.system('cls' if os.name == 'nt' else 'clear')

def validaFaixaInteiro(pergunta, inicio, fim):
    # VALIDA A ENTRADA DE ACORDO COM UMA FAIXA DE INTEIROS RECEBIDA
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
            else:
                pausaParaLeitura('\033[91mValor inválido, favor digitar entre {} e {}\033[0m'.format(inicio, fim), 2)
        except ValueError:
            print()
            pausaParaLeitura('\033[91mValor inválido, favor digitar entre {} e {}\033[0m'.format(inicio, fim), 2)
    return

def pausaParaLeitura(texto, tempo=5):
    # PAUSA PROGRAMA PARA LEITURA DE MENSAGENS
    print ('{}'.format(texto))
    time.sleep(tempo)


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
	print("\n USER \"{}\" REGISTRED AT THE ID \033[91m\"{}\"\033[0m".format(userName, userID))
	usersBase.Insert(user)


def addBook(booksBase):
	bookTitle = input("Titulo do livro: ")
	book = Book(bookTitle)
	bookID = book.key
	try:
		if booksBase.searchValue(book) is not booksBase.NoneNode:
			return("\nBOOK ALREADY REGISTERED.")
	except ValueError:
		pass
	booksBase.Insert(book)
	print("\nBOOK REGISTRED AT THE ID \"{}\".".format(bookID))


def withdrawBook(usersBase,booksBase,userKey):
	user = usersBase.SearchKey(userKey)

	if user is usersBase.NoneNode:
		return print("Invalid user ID.")

	bookID = -1

	while bookID != 0:
		limpaTela()
		bookID = int(input("ID do livro: (0 - exit)"))
		book = booksBase.SearchKey(bookID)
		if book is booksBase.NoneNode:
			print("Invalid book ID. Try again.")
		else:
			break

	if book.isAvailable:
		if user.loans >= 5:
			print("\nYou have passed loans' limit.")

			user.set_empSoma()
			book.set_status(False)
			user.set_livros(book.get_name())
			user.set_livrosId(book.get_id())
			print("\nBook withdrawn.")
		else:
			user.withdrawBook(book.key, book.title)
			book.copies -= 1
	else:
		print("\nUnavailable book.")




#   #####################################################################
#  # REDACT	  REDACT		REDACT		REDACT		REDACT		REDACT #
# #####################################################################




def devolver_livro(TreeU,TreeL,l):
	while True:
		IdUser=l
		user = TreeU.SearchId(TreeU.get_root(),IdUser).get_key()
		print("\nEsses são os livros que estão em sua conta: ")
		for i in range(len(user.get_livros())):
			print("%d - %s"%(user.get_livrosId()[i],user.get_livros()[i]))
		IdLivro=int(input("Digite o Id do livro: "))
		book = TreeL.SearchId(TreeL.get_root(),IdLivro).get_key()
		if user != None and book != None:
			print('\n"{}" devolvido com sucesso!'.format(book.get_name()))
			break
		else:
			print("\nId do Usuário ou do livro inválido")
	if book.get_name() in user.get_livros():
		book.set_status(True)
		user.set_empSub()
		user.remove_livro(book.get_name())
		user.remove_livroId(IdLivro)
	else:
		 print("\nVocê não pegou este livro")

def deletar_usuario(TreeU):
	user = int(input("Digite seu ID: "))
	nodo = TreeU.SearchId(TreeU.get_root(), user).get_key()
	if nodo==None:
		print("\nERRO: Este usuário não existe em nosso banco de dados")
	else:
		senha = input("Digite sua senha: ")
		if senha==nodo.get_senha():
			deletar = TreeU.Delete(user)
			print("\nUsuário excluído com sucesso")
		else:
			print("\nERRO: Esta senha não é compatível com o ID digitado")

def deletar_livro(TreeL):
	print("\nEsses são os livros da biblioteca:")
	TreeL.Inorder_books(TreeL.get_root())
	livro = int(input("Digite o ID do livro (número): "))
	x = TreeL.SearchId(TreeL.get_root(),livro)
	x = x.get_key()
	if x == None:
		print("\nLivro não existe")
	else:
		if x.get_status():
			TreeL.Delete(livro)
			print('\nLivro excluído da biblioteca com sucesso!')
			print("\nNova lista de livros:")
			TreeL.Inorder_books(TreeL.get_root())
		else:
			print("\nO livro está emprestado e não poderá ser deletado")

def Logar(TreeU):
	user = int(input("Digite seu id: "))
	nodo = TreeU.SearchId(TreeU.get_root(), user).get_key()
	if nodo==None:
		print("\nERRO: Este usuário não existe em nosso banco de dados")
	else:
		senha = input("Digite sua senha: ")
		if senha==nodo.get_senha():
			print("\nBem vindo %s"%(nodo.get_name()))
			return user
		else:
			return 0

def LogarProp(a,b):
	user = input("Digite seu id: ")
	senha = input("Digite sua senha: ")
	if user==a and senha==b:
		return True
	else:
		return False