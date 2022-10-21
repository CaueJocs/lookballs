linhas=[]
bola= open('bola.txt' ,'r')
for linha in bola:
    linhas.append(linha)
linhas2=[]
linhas3=[]
final=[]
for i in range(len(linhas)):
    linhas2.append(linhas[i].replace('\n', ''))
    linhas3.append(linhas2[i].replace('\t', ' '))
    final.append(linhas3[i].replace(',' , '.'))
del final[0]

lifinal=[]
for i in range(len(final)):
    li=[]
    base=0
    for j in range(len(final[i])):
        if final[i][j] == ' ':
            li.append(float(final[i][base:j]))
            base=j
        if j+1 == len(final[i]):
            li.append(float(final[i][base:j+1]))
    lifinal.append(li)


            


    
    

        



    








