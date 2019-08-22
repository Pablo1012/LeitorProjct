
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
  print("2 realizar filtro")
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
    arquivo1 = open("Arquivo_Substituido.txt","w")
    arquivo=abrir_a()
    find=raw_input("Substituir: ")
    trocar=raw_input("Por: ")
    while True:
        texto=arquivo.readline()
        if texto.find(find)!=-1:
            texto = texto.replace(find,trocar)
            arquivo1.write(texto)
        if not texto:
            break

    fechar_a(arquivo1)
    fechar_a(arquivo)

if opcao==2:

    cls()
    filtro=raw_input("Digite o filto\n")
    arquivo = abrir_a()
    filtro=open("Arquivo_Filro.txt","w")

    while True:
         linhas=arquivo.readline()
         valor=linhas.find("cebrom")
         '''linha_quebrada=linhas.split()'''
         if valor != -1:
             filtro.write(linhas)
         if not linhas:
             break

    fechar_a(arquivo)
    fechar_a(filtro)
    os.system("pause")

if opcao==3:
    cls()
    arquivo = abrir_a()
    linhas=arquivo.readlines()
    print linhas
    fechar_a(arquivo)
cls()
