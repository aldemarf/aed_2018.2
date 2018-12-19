# UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO -- UFRPE
# DEPARTAMENTO DE ESTATISTICA E INFORMATICA -- DEINFO
# SISTEMAS DE INFORMAÇÃO -- BSI

# ALGORITMOS E ESTRUTURA DE DADOS
# PROF. TIAGO FERREIRA
# ALUNO ALDEMAR S R FILHO


### MAIN SCRIPT ###

import time, os
from libFunctions import *
from libClasses import *
from collections import OrderedDict

loggedUser = None

def MainMenu():
    MainMenu = {1: adminLogin(usersBase),
                2: userLogin(usersBase),
                3: addUser(usersBase),
                4: removeUser(usersBase)
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
 2 : Create User
 3 : Remove User
-----------------------
 0 : EXIT
-----------------------
''')
        option = validateEntry("Option: ",0,4)
        if option == 0:
            return None
        MainMenu[option]


def userMenu():
    UserMenu = {1: borrowedBooks(usersBase, loggedUser),
                2: withdrawBook(usersBase, booksBase, loggedUser),
                3: returnBook(usersBase, booksBase, loggedUser)
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
            return None
        UserMenu[option]

def adminMenu():
    AdminMenu = {1: addBook(booksBase),
                 2: removeBook(booksBase),
                 3: returnBook(usersBase, booksBase, loggedUser)
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
            return None
        AdminMenu[option]

#   #####################################################################
#  # REDACT	  REDACT		REDACT		REDACT		REDACT		REDACT #
# #####################################################################

def userMenu(user,liv,l):
    while True:
        print("")
        print("==============  LOGADO  ================")
        print("== 1 - Meus livros                    ==")
        print("========================================")
        print("== 2 - Solicitar livro                ==")
        print("== 3 - Devolver livro                 ==")
        print("========================================")
        print("== 0 - Deslogar                       ==")
        print("========================================")
        ent=input("Digite sua escolha: ")
        if ent=="1":
            listBooks(user,l)
            continue
        if ent=="2":
            try:
                emprestar_livro(user,liv,l)
                continue
            except:
                print("\nDigite uma entrada numérica")
                continue
        if ent=="3":
            try:
                devolver_livro(user,liv,l)
                continue
            except:
                print("\nDigite uma entrada numérica")
                continue
        if ent=="0":
            break
        else:
            print("\nEntrada inválida")






def Menu_prop(user,liv):
    while True:
        print("")
        print("==============  LOGADO  ================")
        print("== 1 - Cadastrar livro                ==")
        print("== 2 - Deletar livro                  ==")
        print("========================================")
        print("== 3 - Relatório                      ==")
        print("========================================")
        print("== 0 - Deslogar                       ==")
        print("========================================")
        ent=input("Digite sua escolha: ")
        if ent=="1":
            cadastrar_livro(liv)
            continue
        if ent=="2":
            try:
                deletar_livro(liv)
                continue
            except:
                print("\nDigite uma entrada numérica")
                continue
        if ent=="3":
            print("")
            print("RELATÓRIO:")
            print("Livros disponíveis:")
            liv.Inorder_disp(liv.get_root())
            print("Livros emprestados:")
            user.relatorio(user.get_root())
            continue
        if ent=="0":
            break
        else:
            print("\nEntrada inválida")

def Inicio(user,liv,a,b):
    while True:
        print("")
        print("==============   INICIO  ===============")
        print("== 1 - Logar como usuário             ==")
        print("== 2 - Logar como proprietário        ==")
        print("========================================")
        print("== 3 - Cadastrar usuário              ==")
        print("== 4 - Deletar usuário                ==")
        print("========================================")
        print("== 0 - Fechar programa                ==")
        print("========================================")
        ent=input("Digite sua escolha: ")
        if ent=="1":
            try:
                l=Logar(user)
                if l==None:
                    continue
                if l>0:
                    userMenu(user,liv,l)
                    continue
                else:
                    print("\nERRO: Esta senha não é compatível com o ID digitado")
                    continue
            except:
                print("\nDigite uma entrada numérica")
                continue
        if ent=="2":
            if LogarProp(a,b):
                print("\nBem vindo ao modo proprietário")
                Menu_prop(user,liv)
                continue
            else:
                print("\nERRO: Usuário ou senha incorretos")
                continue
        if ent=="3":
            cadastrar_usuario(user)
            continue
        if ent=="4":
            try:
                deletar_usuario(user)
                continue
            except:
                print("\nDigite uma entrada numérica")
                continue
        if ent=="0":
            break
        else:
            print("\nEntrada inválida")




#   #####################################################################
#  #                                MAIN                               #
# #####################################################################

# Inicialização de variáveis
loggedUser = None
usersBase = RedWhiteTree()
booksBase = RedWhiteTree()
