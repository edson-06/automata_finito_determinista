from tkinter import *
import pygame
import interfaceDatos

class VentanaPrincipal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1200x650")
        self.ventana.minsize(width=1000, height=550)
        self.ventana.config(padx=3, pady=5)
        self.createContainer(self.ventana)
        self.ventana.mainloop()

    def createContainer(self, contenedor):

        frameArriba = Frame(contenedor,bd=5,relief=RIDGE,padx=5)
        frameArriba.place(relx=0.01,rely=0,relwidth=0.97,relheight=0.15)
        Label(frameArriba,
            bg="gray",
            fg="white",
            text="Escoge los datos",
            relief="flat",
            font=("Agency FB",30)).place(relx=0,rely=0,relwidth=1,relheight=1)

        frameIzquierda = Frame(contenedor,bg="gray",bd=1,relief=SOLID)
        frameIzquierda.place(relx=0,rely=0.15,relwidth=0.15,relheight=1)

        frameDerecha = Frame(contenedor,bg="gray",bd=1,relief=SOLID)
        frameDerecha.place(relx=0.85,rely=0.15,relwidth=0.15,relheight=1)

        frameCentral = Frame(contenedor,bd=5,relief=RIDGE,padx=5)
        frameCentral.place(relx=0.16,rely=0.16,relwidth=0.68,relheight=0.84)

        self.labelPalabraDibujar = Label(frameArriba,
            bg="gray",
            fg="white",
            text="Automata Finito Determinista",
            relief="flat",
            font=("Agency FB",30)).place(relx=0,rely=0,relwidth=1,relheight=1)

        self.img= PhotoImage(file="imgAutomata.gv.png")#guardamos la direccion de una imagen en una variable
        
        Label(frameCentral, image=self.img,bg="white").place(relx=0,rely=0,relwidth=1,relheight=1)#mostramos la imagen en la ventana

        self.buttonSalirJuego = Button(frameIzquierda,
            text="<---",
            cursor="hand2",
            font=("Agency FB",20) ,
            command=self.salirInterfaz).place(relx=0.1,rely=0.7,relwidth=0.66,relheight=0.09)

        self.buttonGenerarAFD = Button(frameDerecha,
            text="--->",
            cursor="hand2",
            font=("Agency FB",20) ,
            command=self.generarAFD).place(relx=0.1,rely=0.7,relwidth=0.66,relheight=0.09)
    
    def salirInterfaz(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()
        self.ventana.after(400, self.regresarVentana)

    def generarAFD(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()

    def regresarVentana(self):
        self.ventana.destroy()#se destruye la ventana del splash
        interfaceDatos.crearINPrincipal()


def crearIAFD():
    INprincipal = VentanaPrincipal()

