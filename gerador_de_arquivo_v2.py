import os

arquivo=open("teste.txt","w")
for x in range(1,100,1):
    if x<10:
        s="\ndevice"+str(x)+"; user"+str(x)+"; malware"+str(x)+"; zona: cebrom"
        arquivo.write(s)
    if x>=10 and x<40:
        s="\ndevice"+str(x)+"; user"+str(x)+"; malware"+str(x)+"; zona: record"
        arquivo.write(s)
    if x>=40:
        s="\ndevice"+str(x)+"; user"+str(x)+"; malware"+str(x)+"; zona: coapil"
        arquivo.write(s)

arquivo.close()
