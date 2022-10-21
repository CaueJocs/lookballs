from math import sqrt

def leitura():
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
    return lifinal

def robo(posirobox,posiroboy):
    bola =leitura()
    posirobo=[]
    intercept=[]
    acel= 2.8
    raio= 0.12

    posirobo.append(posirobox)
    posirobo.append(posiroboy)

    temporizador=0
    final=0

    for i in range(len(bola)):
        dist =sqrt(((bola[i][0] - posirobo[0])**2) + ((bola[i][1] - posirobo[1])**2))
        if (dist- raio)/ acel <= temporizador:
            intercept.append( bola[i][0])
            intercept.append( bola[i][1])

            break
        else:
            temporizador += 0.02
    
    velr= (dist) / (temporizador)
    
    distb= sqrt(((intercept[0] - bola[0][0])**2) + ((intercept[1] - bola[0][1])**2))

    velb= (distb) / (temporizador)


def main():
    
    posirobox= float(input("Digite a posição do robô no eixo X: "))
    posiroboy= float(input("Digite a posição do robô no eixo Y: "))

    robo(posirobox,posiroboy)

main()

    

    







            


    
    

        



    








