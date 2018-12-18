# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO -- UFRPE
# DEPARTAMENTO DE ESTATISTICA E INFORMATICA -- DEINFO
# SISTEMAS DE INFORMAÇÃO -- BSI

# ALGORITMOS E ESTRUTURA DE DADOS
# PROF. TIAGO FERREIRA
# ALUNO ALDEMAR S R FILHO


### BIBLIOTECA DE FUNCOES ###

from libClasses import *

def valida_faixa_inteiro(pergunta, inicio, fim):
    # VALIDA A ENTRADA DE ACORDO COM UMA FAIXA DE INTEIROS RECEBIDA
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
            else:
                pausa_para_leitura('\033[91mValor inválido, favor digitar entre {} e {}\033[0m'.format(inicio, fim), 2)
        except ValueError:
            print()
            pausa_para_leitura('\033[91mValor inválido, favor digitar entre {} e {}\033[0m'.format(inicio, fim), 2)
    return

def pausa_para_leitura(texto, tempo=5):
    # PAUSA PROGRAMA PARA LEITURA DE MENSAGENS
    print ('{}'.format(texto))
    time.sleep(tempo)


def loadBooksDatabase():
	books = RedWhiteTree()
	with open("BaseLivros.txt","r",encoding = "UTF-8") as booksFile:
		booksBase = booksFile.read().splitlines()

	for book in booksBase:
		books.insertNode(book)


#   #####################################################################
#  # REDACT	  REDACT		REDACT		REDACT		REDACT		REDACT #
# #####################################################################


def cadastrar_usuario(Tree):
	entr = input("Digite seu nome: ")
	senha = input("Digite sua senha: ")
	usuario = User(entr,senha)
	ID = usuario.get_id()
	print("\n{}, seu id é |{}| e sua senha é |{}|".format(entr, ID, senha))
	Tree.Insert(usuario)

def cadastrar_livro(Tree):
	print("\nEsses são os livros já cadastrados: ")
	Tree.Inorder_books(Tree.get_root())
	entr = input("Digite o nome do livro: ")
	livro = Book(entr)
	Tree.Insert(livro)
	print("\nLivro cadastrado com sucesso")

def emprestar_livro(TreeU,TreeL,l):
	print("")
	TreeL.Inorder_disp(TreeL.get_root())
	while True:
		IdUser=l
		IdLivro=int(input("Digite o Id do livro: "))
		user = TreeU.SearchId(TreeU.get_root(),IdUser).get_key()
		book = TreeL.SearchId(TreeL.get_root(),IdLivro).get_key()
		if user != None and book != None:
			break
		else:
			print("")
			print("Id do Usuário ou do livro inválido")
			return
	if book.get_status() == False:
		print("")
		print("Livro indisponível")
	else:
		if user.get_emp() < 5:
			user.set_empSoma()
			book.set_status(False)
			user.set_livros(book.get_name())
			user.set_livrosId(book.get_id())
			print("")
			print('O "{}" foi entregue para {}, cujo ID é {}'.format(book.get_name(),user.get_name(),user.get_id()))
		else:
			print("")
			print("Usuário ultrapassou o limite de empréstimos")

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