from tkinter import *
import pygame
import interfaceDatos

class VentanaPrincipal:
    pygame.mixer.init()
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1200x650")
        self.ventana.minsize(width=1000, height=550)
        self.ventana.config(padx=3, pady=5)
        self.createContainer(self.ventana)
        self.ventana.mainloop()

    def createContainer(self, contenedor):

        self.img= PhotoImage(file="imagenes/descarga.png")#guardamos la direccion de una imagen en una variable
        Label(contenedor, image=self.img,bg="white").place(relx=0,rely=0,relwidth=1,relheight=1)#mostramos la imagen en la ventana
        
        frameArriba = Frame(contenedor,bd=5,relief=RIDGE,padx=5)
        frameArriba.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.15)
        self.labelPalabraDibujar = Label(frameArriba,
            bg="gray",
            fg="white",
            text="Generador de Automata Finito Determinista",
            relief="flat",
            font=("Agency FB",30)).place(relx=0,rely=0,relwidth=1,relheight=1)


        self.buttonCrearJuego = Button(contenedor,
            text="Crear Automata",
            cursor="hand2",
            font=("Agency FB",40) ,
            command=self.crearInterfazDatos).place(relx=0.55,rely=0.75,relwidth=0.4,relheight=0.15)

        self.buttonSalirJuego = Button(contenedor,
            text="Salir",
            cursor="hand2",
            font=("Agency FB",40) ,
            command=self.accionSalir).place(relx=0.1,rely=0.75,relwidth=0.4,relheight=0.15)

    def crearInterfazDatos(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()
        self.ventana.after(400, self.crearInterfazCapturarDatos)

    def crearInterfazCapturarDatos(self):
        self.ventana.destroy()#se destruye la ventana del splash
        interfaceDatos.crearINPrincipal()

    def accionSalir(self):
        self.ventana.destroy()#se destruye la ventana del splash


def crearINPrincipal():
    INprincipal = VentanaPrincipal()

