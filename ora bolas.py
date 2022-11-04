from math import sqrt
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
    vel= 2.8
    raio= 0.12

    posirobo.append(posirobox)
    posirobo.append(posiroboy)

    temporizador=0
    linha=0
    distrel=[]
    

    for i in range(len(bola)):
        dist =sqrt(((bola[i][0] - posirobo[0])**2) + ((bola[i][1] - posirobo[1])**2))
        if (dist- raio)<= temporizador *vel:
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
    
    plt.plot(xbola, ybola, color= "red", label='Bola')
    plt.plot(xrobo,yrobo, color = "blue",label='Robô')
    plt.legend(loc='upper center')
    
    plt.title("Gráfico de trajetória do Robô até a Bola")
    plt.xlabel("Eixo X(m)")
    plt.ylabel("Eixo Y(m)")
    plt.show()
    #graph1(t[0],t[1], posirobox, posiroboy)
    

def graf2(posirobox,posiroboy,xintercept, yintercept,temporizador,bolax,bolay,tempo):
    x=posirobox, xintercept
    y= posiroboy, yintercept
    time= 0.0 , temporizador
    
    plt.subplot(1,2,1)
    plt.plot(tempo, bolax, color="red")
    plt.plot(time, x, color="blue")
    plt.title("Cordenada X")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Metros (m)")
    
    plt.subplot(1,2,2)
    plt.plot(tempo, bolay,color='red')
    plt.plot(time, y, color='blue')
    plt.title("Coordenada Y")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Metros (m)")
    plt.suptitle("Coordenadas de X e Y Do Robô E Bola em Função Do Tempo")
    plt.show()
    
    #graf2(posirobox, posiroboy, t[5] , t[6], t[3], t[0], t[1], t[4])

def graf3(tempo):
    velxbola=[]
    velybola=[]
    velrobo=[]
    for i in range(len(tempo)):
        velxbola.append(((-0.76) *tempo[i]) + 4.1792)
    for i in range(len(tempo)):
        velybola.append(((-0.4 *tempo[i] ) +1,8))
    
    for i in range(len(tempo)):
        if tempo[i] < 1:
            velrobo.append(tempo[i] * 2.8)
        else:
            velrobo.append(2.8)
    
    plt.subplot(1,2,1)
    plt.plot(tempo , velxbola,color="blue")
    plt.plot(tempo, velrobo , color='red')
    plt.title("Cordenada X")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Velocidade (m/s)")
    
    plt.subplot(1,2,2)
    plt.plot(tempo , velybola,color="blue")
    plt.plot(tempo, velrobo , color='red')
    plt.title("Cordenada Y")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Velocidade (m/s)")
    plt.suptitle("Velocidade em X e Y Do Robô E Bola em Função Do Tempo")
    
    plt.show()

def graf4(tempo):
    acelx= -0.76 , -0.76
    acely= -0.4 , -0.4
    chegada= 0 , tempo[(len(tempo) - 1)]
    velrobo=[]
    for i in range(len(tempo)):
        if tempo[i] > 1:
            velrobo.append(0)
        else:
            velrobo.append(2.8)
    
    plt.subplot(2,1,1)
    plt.plot(chegada,acelx,tempo, velrobo, color='blue')
    plt.plot(tempo, velrobo,color='red')
    plt.title("Cordenada X")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração (m/s²)")
    
    plt.subplot(2,1,2)
    plt.plot(chegada,acely,color='blue')
    plt.plot(tempo, velrobo,color='red')
    plt.title("Cordenada Y")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Aceleração (m/s²)")
    plt.suptitle("Aceleração em X e Y Do Robô E Bola em Função Do Tempo")

    
    plt.show()


def graf5(posrobo,bola,tempo):
    distrel=[]
    for i in range(len(posrobo)):
        dist =sqrt(((bola[i][0] - posrobo[i][0])**2) + ((bola[i][1] - posrobo[i][1])**2))
        distrel.append(dist)
    
    plt.title(" Distância Relativa entre Robo e Bola em função do tempo")
    plt.xlabel("Tempo(s)")
    plt.ylabel("Distância Relativa (m)")
    
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
    
    posirobox= int 
    posiroboy=int
    

    def chamargraf1(posirobox,posiroboy):  
        t= robo(posirobox,posiroboy)
        graf1(t[0],t[1], posirobox, posiroboy)
        
    def chamargraf2(posirobox,posiroboy):
        t= robo(posirobox,posiroboy)
        graf2(posirobox, posiroboy, t[5] , t[6], t[3], t[0], t[1], t[4])
    
    def chamargraf3(posirobox,posiroboy):
        t= robo(posirobox,posiroboy)
        graf3(t[4])

    def chamargraf4(posirobox,posiroboy):
        t= robo(posirobox,posiroboy)
        graf4(t[4])

    
    def chamargraf5(posirobox,posiroboy):
        t= robo(posirobox,posiroboy)
        graf5(t[8], t[7] , t[4])
    
    def salvar():
        posirobox = float(entry1.get())
        posiroboy= float(entry2.get())
        return [posirobox, posiroboy]

    
    button1 = tk.Button(text='Gráfico de Interceptação', command= lambda: chamargraf1(posirobox,posiroboy))
    canvas1.create_window(100, 350, window=button1)
    
    button2 = tk.Button(text='Gráfico de Interceptação de XY em T', command=chamargraf2)
    canvas1.create_window(300, 350, window=button2)
    
    button3 = tk.Button(text='Gráfico de Velocidade em X e Y do Robô e Bola', command=chamargraf3)
    canvas1.create_window(550, 350, window=button3)

    button4 = tk.Button(text='Gráfico de Aceleração em X e Y do Robô e Bola', command=chamargraf4)
    canvas1.create_window(150, 450, window=button4)

    button5 = tk.Button(text='Gráfico de Distância Relativa entre Robô e Bola', command=chamargraf5)
    canvas1.create_window(450, 450, window=button5)

    button6 = tk.Button(text='Salvar', command=salvar)
    canvas1.create_window(500, 100, window=button6)
    

    root.mainloop()
    
    
main()


    

    







            


    
    

        



    








