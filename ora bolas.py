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
    
    velrobox=(intercept[0] - posirobox) / temporizador
    velroboy=(intercept[1] - posiroboy) /temporizador
    velbolax=(intercept[0] -bola[0][0]) /temporizador
    velbolay=(intercept[1] -bola[0][1]) /temporizador
 
    if velroboy <0:
        velroboy = velroboy*-1

    if velrobox <0:
        velrobox= velrobox*-1
 
    return [bolax, bolay,pontos,temporizador,tempo,intercept[0],intercept[1],posbola,posrobo,velbolax,velbolay,velrobox,velroboy]


def graf1(bolax,bolay,posirobox,posiroboy):
    xbola = bolax
    ybola = bolay
    xrobo = posirobox, bolax[len(bolax)-1]
    yrobo = posiroboy, bolay[len(bolay)-1]
    
    plt.plot(xbola, ybola, color= "red", label='Bola')
    plt.plot(xrobo,yrobo, color = "blue",label='Rob??')
    plt.legend(loc='upper center')
    
    plt.title("Gr??fico de trajet??ria do Rob?? at?? a Bola")
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
    plt.suptitle("Coordenadas de X e Y Do Rob?? E Bola em Fun????o Do Tempo")
    plt.show()
    
    #graf2(posirobox, posiroboy, t[5] , t[6], t[3], t[0], t[1], t[4])

def graf3(tempo):
    velxbola=[]
    velybola=[]
    velrobo=[]
    for i in range(len(tempo)):
        velxbola.append(((-0.76) *tempo[i]) + 4.1792)
    
    for i in range(len(tempo)):
        velybola.append(((-0.4 *tempo[i] ) +1.8))
    
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
    plt.plot(tempo , velybola, color="blue")
    plt.plot(tempo, velrobo , color='red')
    plt.title("Cordenada Y")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Velocidade (m/s)")
    plt.suptitle("Velocidade em X e Y Do Rob?? E Bola em Fun????o Do Tempo")
    
    plt.show()

    return[velxbola[len(velxbola)-1],velybola[len(velybola)-1],velrobo[len(velrobo)-1]]

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
    plt.ylabel("Acelera????o (m/s??)")
    
    plt.subplot(2,1,2)
    plt.plot(chegada,acely,color='blue')
    plt.plot(tempo, velrobo,color='red')
    plt.title("Cordenada Y")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Acelera????o (m/s??)")
    plt.suptitle("Acelera????o em X e Y Do Rob?? E Bola em Fun????o Do Tempo")

    
    plt.show()


def graf5(posrobo,bola,tempo):
    distrel=[]
    for i in range(len(posrobo)):
        dist =sqrt(((bola[i][0] - posrobo[i][0])**2) + ((bola[i][1] - posrobo[i][1])**2))
        distrel.append(dist)
    
    plt.title(" Dist??ncia Relativa entre Robo e Bola em fun????o do tempo")
    plt.xlabel("Tempo(s)")
    plt.ylabel("Dist??ncia Relativa (m)")
    
    plt.plot(tempo , distrel)
    plt.show()


def main():
    
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width=800, height=600)
    canvas1.pack()
    
    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)
    canvas1.create_window(400, 50, window=entry1)
    canvas1.create_window(400, 100, window=entry2)
    
    canvas1.create_text(200, 50, text="Digite a posi????o X do rob??", fill="black", font=('Helvetica 15 bold'))
    canvas1.create_text(200, 100, text="Digite a posi????o Y do rob??", fill="black", font=('Helvetica 15 bold'))
    canvas1.pack()

    T = tk.Text(root, height = 7, width = 90)
    T.place(relx = 0.5, rely = 0.4, anchor = 'c')

    def chamargraf1(posirobox,posiroboy):
        if posirobox == 'nada' or posiroboy == 'nada':
            T.insert(tk.END,"Digite as coordenadas primeiro ! \n")    
        else:
            t= robo(posirobox,posiroboy)
            graf1(t[0],t[1], posirobox, posiroboy)
        
    def chamargraf2(posirobox,posiroboy):
        if posirobox == 'nada' or posiroboy == 'nada':
            T.insert(tk.END,"Digite as coordenadas primeiro ! \n")     
        else:
            t= robo(posirobox,posiroboy)
            graf2(posirobox, posiroboy, t[5] , t[6], t[3], t[0], t[1], t[4])
    
    def chamargraf3(posirobox,posiroboy):
        if posirobox == 'nada' or posiroboy == 'nada':
            T.insert(tk.END,"Digite as coordenadas primeiro ! \n")     
        else:
            t= robo(posirobox,posiroboy)
            j= graf3(t[4])
            T.insert(tk.END,"Velocidade da bola no instante de intercepta????o em X= %.2f m/s Y= %.2f m/s \n" %(j[0],j[1]))
            T.insert(tk.END,"Velocidade do rob?? no instante de intercepta????o ?? de %.2f \n" %j[2])

    def chamargraf4(posirobox,posiroboy):
        if posirobox == 'nada' or posiroboy == 'nada':
            T.insert(tk.END,"Digite as coordenadas primeiro ! \n")     
        else:
            t= robo(posirobox,posiroboy)
            graf4(t[4])
             
             
    def chamargraf5(posirobox,posiroboy):
        if posirobox == 'nada' or posiroboy == 'nada':
            T.insert(tk.END,"Digite as coordenadas primeiro ! \n")     
        else:
            t= robo(posirobox,posiroboy)
            graf5(t[8], t[7] , t[4])
    
    def salvar():
        posirobox = float(entry1.get())
        posiroboy= float(entry2.get())
        t= robo(posirobox,posiroboy)        
        if posirobox >9 or posiroboy>6:
            T.insert(tk.END,"Comandos inv??lidos ! \n")  
        else:
            global params
            params=[posiroboy,posirobox]
        T.delete('1.0', 'end')
        T.insert(tk.END,"Informa????es recebidas ! \n" )
        T.insert(tk.END,"O rob?? interceptou a Bola em %.2f segundos \n" %t[3])
        T.insert(tk.END,"A bola foi interceptada no ponto X= %.2f Y= %.2f \n" %(t[5],t[6]))
        T.insert(tk.END,"A velocidade m??dia da bola na coordenada X= %.2f m/s e  Y= %.2f m/s \n" %(t[9],t[10]))
        T.insert(tk.END,"A velocidade m??dia do rob?? na coordenada X= %.2f m/s e  Y= %.2f m/s \n" %(t[11],t[12]))
        
    
    def limpar():
        global params
        params=['nada','nada']
        T.delete('1.0', 'end')
        T.insert(tk.END,"Resetado.")  

    button1 = tk.Button(text='Gr??fico de Intercepta????o', command=lambda :chamargraf1(params[0],params[1]))
    canvas1.create_window(100, 350, window=button1)
    
    button2 = tk.Button(text='Gr??fico de Intercepta????o de XY em T', command= lambda: chamargraf2(params[0],params[1]))
    canvas1.create_window(300, 350, window=button2)
    
    button3 = tk.Button(text='Gr??fico de Velocidade em X e Y do Rob?? e Bola', command=lambda: chamargraf3(params[0],params[1]))
    canvas1.create_window(550, 350, window=button3)

    button4 = tk.Button(text='Gr??fico de Acelera????o em X e Y do Rob?? e Bola', command=lambda: chamargraf4(params[0],params[1]))
    canvas1.create_window(150, 450, window=button4)

    button5 = tk.Button(text='Gr??fico de Dist??ncia Relativa entre Rob?? e Bola', command=lambda: chamargraf5(params[0],params[1]))
    canvas1.create_window(450, 450, window=button5)

    button6 = tk.Button(text='Salvar', command=salvar)
    canvas1.create_window(500, 100, window=button6)

    button7 = tk.Button(text='Resetar', command=limpar)
    canvas1.create_window(550, 100, window=button7)

    root.mainloop()

    
main()
