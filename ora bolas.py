from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


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
    linha=0
    distrel=[]
    

    for i in range(len(bola)):
        dist =sqrt(((bola[i][0] - posirobo[0])**2) + ((bola[i][1] - posirobo[1])**2))
        if (dist- raio)/ acel <= temporizador:
            intercept.append( bola[i][0])
            intercept.append( bola[i][1])
            
            
            linha=i
            
            break
        else:
            
            temporizador += 0.02
            
    
    bolax=[]
    bolay=[]
    posbola=[]

    for linhas in range(linha+1):
        for colunas in range(len(bola[linhas])):
            if colunas == 0:
                bolax.append(bola[linhas][colunas])
            else:
                bolay.append(bola[linhas][colunas])
    pontos= 0

    for linha in range(len(bolax)):
        teste=[]
        teste.append(bolax[linha])
        teste.append(bolay[linha])
        posbola.append(teste)
    
    tempo=[]
    t=0
    while True:
        if t == temporizador:
            tempo.append(t)
            break
        else:
            tempo.append(t)
            t = t+0.02
    

    coefangx= (intercept[0]-posirobox)/ temporizador
    coeflinx= intercept[0] - (temporizador*coefangx)
    coefangy= (intercept[1]-posiroboy)/ temporizador
    coefliny= intercept[1] - (temporizador*coefangy)
    
    posx=[]
    posy=[]
    posrobo=[]
    
    for i in range(len(tempo)):
        x= (tempo[i] * coefangx) + coeflinx
        y = (tempo[i] * coefangy) + coefliny
        posx.append(x)
        posy.append(y)
    
    for linha in range(len(tempo)):
        teste=[]
        teste.append(posx[linha])
        teste.append(posy[linha])
        posrobo.append(teste)
    
 
    

    return [bolax, bolay,pontos,temporizador,tempo,intercept[0],intercept[1],posbola,posrobo]


def graf1(bolax,bolay,posirobox,posiroboy):
    xbola = bolax
    ybola = bolay
    xrobo = posirobox, bolax[len(bolax)-1]
    yrobo = posiroboy, bolay[len(bolay)-1]
    
    plt.plot(xbola, ybola, color= "red", label='robo')
    plt.plot(xrobo,yrobo, color = "blue",label='bola')

    leg = plt.legend(loc='upper center')
    
    plt.title("Gráfico de trajetória do Robô até a Bola")
    plt.xlabel("Eixo X(m)")
    plt.ylabel("Eixo Y(m)")
    plt.show()
    #graph1(t[0],t[1], posirobox, posiroboy)
    

def graf2(posirobox,posiroboy,xintercept, yintercept,temporizador,bolax,bolay,tempo):
    x=posirobox, xintercept
    y= posiroboy, yintercept
    time= 0.0 , temporizador
    
    plt.title("Cordenada X do Robô e Bola em função do Tempo")
    plt.xlabel("Eixo X(s)")
    plt.ylabel("Eixo Y(m)")
    plt.plot(tempo, bolax, color="red")
    plt.plot(time, x, color="blue")
    plt.show()
    
    plt.title("Coordenada Y do Robô e Bola em função do Tempo")
    plt.xlabel("Eixo X(s)")
    plt.ylabel("Eixo Y(m)")
    plt.plot(tempo, bolay,color='red')
    plt.plot(time, y, color='blue')
    plt.show()
    
    #graf2(posirobox, posiroboy, t[5] , t[6], t[3], t[0], t[1], t[4])



def graf5(posrobo,bola,tempo):
    distrel=[]
    for i in range(len(posrobo)):
        dist =sqrt(((bola[i][0] - posrobo[i][0])**2) + ((bola[i][1] - posrobo[i][1])**2))
        distrel.append(dist)
    
    plt.title(" Distância Relativa entre Robo e Bola em função do tempo")
    plt.xlabel("Eixo X(s)")
    plt.ylabel("Eixo Y(m)")
    
    plt.plot(tempo , distrel)
    plt.show()
    #graf5(t[8], t[7] , t[4])



def main():
    
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width=800, height=600)
    canvas1.pack()
    
    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)
    canvas1.create_window(400, 50, window=entry1)
    canvas1.create_window(400, 100, window=entry2)
    
    canvas1.create_text(200, 50, text="Digite a posição X do robô", fill="black", font=('Helvetica 15 bold'))
    canvas1.create_text(200, 100, text="Digite a posição Y do robô", fill="black", font=('Helvetica 15 bold'))
    canvas1.pack()
    
    def chamargraf1():  
        posirobox = float(entry1.get())
        posiroboy= float(entry2.get())
        t= robo(posirobox,posiroboy)
        graf1(t[0],t[1], posirobox, posiroboy)
        
    def chamargraf2():
        posirobox = float(entry1.get())
        posiroboy= float(entry2.get())
        t= robo(posirobox,posiroboy)
        graf2(posirobox, posiroboy, t[5] , t[6], t[3], t[0], t[1], t[4])
    
    def chamargraf5():
        posirobox = float(entry1.get())
        posiroboy= float(entry2.get())
        t= robo(posirobox,posiroboy)
        graf5(t[8], t[7] , t[4])
    
        
    button1 = tk.Button(text='Gráfico de Interceptação', command=chamargraf1)
    canvas1.create_window(100, 350, window=button1)
    
    button2 = tk.Button(text='Gráfico de Interceptação de XY em T', command=chamargraf2)
    canvas1.create_window(300, 350, window=button2)
    
    button3 = tk.Button(text='Gráfico de distância relativa entre Robô e Bola', command=chamargraf5)
    canvas1.create_window(500, 350, window=button3)
    

    root.mainloop()
    

main()


    

    







            


    
    

        



    










    







            


    
    

        



    








