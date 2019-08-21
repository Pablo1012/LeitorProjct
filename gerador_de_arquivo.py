import os


arquivo=open("teste.txt","w")
for x in range(1,100,1):
  s="device"+str(x)+"; user"+str(x)+"; malware"+str(x)+"\n"
  arquivo.write(s)
arquivo.close()
os.system("exit")
