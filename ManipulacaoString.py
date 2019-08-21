'''
References:
Manipular string: https://wiki.python.org.br/ManipulandoStringsComPython
Manipular arquivo: https://panda.ime.usp.br/pensepy/static/pensepy/10-Arquivos/files.html
'''

import os

def cls():
    os.system('cls')

def abrir_a():
    input_file=raw_input("Digite o caminho do arquivo: ")
    arquivof=open(input_file,'r')
    return arquivof

def fechar_a(arquivo):
    arquivo.close()

opcao=0
countl=0

while opcao>4 or opcao<1:
  print("Qual das operaracao deseja realizar ?")
  print("###############################\n")
  print("1 substituir texto")
  print("2 Ler linha do arquivo")
  print("3 abrir arquivo completo")
  print("4 Alterar caracter\n")
  print("###############################")
  opcao=input()
  if opcao>4 or opcao<1:
    cls()
    continue
  else:
    break

if opcao==1:
    cls()
    texto=raw_input("Digite a string a ser manipulada\n")
    find=raw_input("Substituir: ")
    trocar=raw_input("Por: ")
    ntexto = trocar.join(texto.split(find))
    print ntexto

if opcao==2:
    cls()

    arquivo = abrir_a()

    while 1:
        
        lin=arquivo.readline()
        linhas=lin.replace('""','\n')
        print "testando o count "+linhas
        if not linhas:
            break
        else:
            
            linhas=arquivo.readline()
            linha_quebrada=linhas.split()
            print linha_quebrada[0], linha_quebrada[1], linha_quebrada[2]
            continue
           
    fechar_a(arquivo)

    os.system("pause")

if opcao==3:
    cls()
    arquivo = abrir_a()
    linhas=arquivo.readlines()
    print linhas
    fechar_a(arquivo)
cls()
