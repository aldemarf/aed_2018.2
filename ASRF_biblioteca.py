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



#   #####################################################################
#  # REDACT	  REDACT		REDACT		REDACT		REDACT		REDACT #
# #####################################################################


def menuPrincipal():
    menu_principal = { 1: menuAdministrador,
                       2: menuUsuarios,
                       3: listaLivros,
                       4: aluno_memoria.menu_aluno,
                       5: disciplina_arquivo.menu_disciplina,
                       6: disciplina_memoria.menu_disciplina,
                       7: turma_arquivo.menu_turma,
                       8: turma_memoria.menu_turma,
                       9: relatorio_arquivo.menu_relatorio,
                      10: relatorio_memoria.menu_relatorio}

    opcao = -1
    while True:
        limpa_tela()
        print('''
---------------------------
-     \033[1m     MENU      \033[0m     -
---------------------------
 1  - Professor - Arquivo
 2  - Professor - Memoria
 3  - Aluno - Arquivo
 4  - Aluno - Memoria
 5  - Disciplina - Arquivo
 6  - Disciplina - Memoria
 7  - Turma - Arquivo
 8  - Turma - Memoria
 9  - Relatorios - Arquivo
 10 - Relatorios - Memoria
---------------------------
 0 - SAIR
---------------------------
''')
        opcao = valida_faixa_inteiro('Escolha uma opção: ',0,10)
        if opcao == 0:
            break
        menu_principal[opcao]()
    return