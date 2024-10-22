from tkinter import *
import pygame
import interfacePrincipal
from tkinter import ttk
from tkinter import messagebox
import interfaceFuncionTransicion

class VentanaPrincipal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("1200x650")
        self.ventana.minsize(width=1000, height=550)
        self.ventana.config(padx=3, pady=5)
        self.crearContenedores(self.ventana)
        
        self.banderaNodoIF="dfsd"
        self.banderaNodoI="ffsdfsd"
        self.banderaNodoF="dfsdf"

        self.definirNodos=""
        self.definirNumeroNodos=""
        self.definirAlfabeto=""
        self.definirNumeroAlfabeto=""
        self.banderaActivaNodos = 0

        self.ventana.mainloop()

        #################################################
        

    def crearContenedores(self, contenedor):
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

        self.frameCentral = Frame(contenedor,bd=5,relief=RIDGE,padx=5)
        self.frameCentral.place(relx=0.16,rely=0.16,relwidth=0.68,relheight=0.84)

        self.buttonSalirJuego = Button(frameIzquierda,
            text="<---",
            cursor="hand2",
            font=("Agency FB",20) ,
            command=self.salirInterfaz).place(relx=0.1,rely=0.7,relwidth=0.66,relheight=0.09)

        self.buttonCambiarJuego = Button(frameDerecha,
            text="--->",
            cursor="hand2",
            font=("Agency FB",20) ,
            command=self.cambiarVentaFuncionT).place(relx=0.1,rely=0.7,relwidth=0.66,relheight=0.09)

        self.buttonGenerarNodoEstados = Button(frameDerecha,
            text="Estados",
            cursor="hand2",
            font=("Agency FB",20) ,
            command=self.generarComboEstados).place(relx=0.1,rely=0.14,relwidth=0.66,relheight=0.09)


        self.componentesContenedorCentral(self.frameCentral)
    
    def componentesContenedorCentral(self, contenedor):
        self.banderaActivaNodos = 0 #bandera para poder pasar a la siguiente ventana
        Label(contenedor,
            bg="white" ,text= "Nombre de nodos:",
            font =('Times New Roman', 15)).place(relx=0.05,rely=0.05,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
        self.comboNodos = ttk.Combobox(contenedor,
            state="readonly",justify=CENTER ,
            font =('Times New Roman', 20))#creamos una lista desplegable
        self.comboNodos["values"] = ["A,B,C,D", "q0,q1,q2,q3", "N0,N1,N2"]#agregamos valores a la lista desplegable
        self.comboNodos.place(relx=0.05,rely=0.15,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
        self.comboNodos.current(0)#seleccionamos el item en la primera pósicion
        
        Label(contenedor,
            bg="white" ,text= "Número de nodos:",
            font =('Times New Roman', 15)).place(relx=0.30,rely=0.05,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
        self.comboNumeroNodos = ttk.Combobox(contenedor,
            state="readonly",justify=CENTER ,
            font =('Times New Roman', 20))#creamos una lista desplegable
        self.comboNumeroNodos["values"] = ["1", "2", "3", "4","5", "6","7","8"]#agregamos valores a la lista desplegable
        self.comboNumeroNodos.current(0)#seleccionamos el item en la primera pósicion
        self.comboNumeroNodos.place(relx=0.30,rely=0.15,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
        
        Label(contenedor,
            bg="white" ,text= "Alfabeto:",
            font =('Times New Roman', 15)).place(relx=0.55,rely=0.05,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
        self.comboAlfabeto = ttk.Combobox(contenedor,
            state="readonly",justify=CENTER ,
            font =('Times New Roman', 20))#creamos una lista desplegable
        self.comboAlfabeto["values"] = ["a,b,c", "0,1,2", "x,y,z"]#agregamos valores a la lista desplegable
        self.comboAlfabeto.current(0)#seleccionamos el item en la primera pósicion
        self.comboAlfabeto.place(relx=0.55,rely=0.15,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
        
        Label(contenedor,
            bg="white" ,text= "Letras del Alfabeto:",
            font =('Times New Roman', 15)).place(relx=0.79,rely=0.05,relwidth=0.21,relheight=0.08)#Creamos una etiqueta
        self.comboNumeroAlfabeto = ttk.Combobox(contenedor,
            state="readonly",justify=CENTER ,
            font =('Times New Roman', 20))#creamos una lista desplegable
        self.comboNumeroAlfabeto["values"] = ["1", "2", "3"]#agregamos valores a la lista desplegable
        self.comboNumeroAlfabeto.current(0)#seleccionamos el item en la primera pósicion
        self.comboNumeroAlfabeto.place(relx=0.79,rely=0.15,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
        
    def generarComboEstados(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()
        self.definirNodos=self.comboNodos.get()
        self.definirNumeroNodos=int(self.comboNumeroNodos.get())
        self.definirAlfabeto=self.comboAlfabeto.get()
        self.definirNumeroAlfabeto=int(self.comboNumeroAlfabeto.get())
        ##### uso de la clase############################
        self.afd = arrayNodoAlfabeto(self.definirNodos, self.definirAlfabeto, self.definirNumeroNodos, self.definirNumeroAlfabeto)
        self.nodosAFD = self.afd.getNombreNodo
        self.alfabetoAFD = self.afd.getNombreAlfabeto
        ##################################################
        self.arregloNodos = self.afd.arrayNodo()# ARREGLO DONDE ESTAN LOS NODOS DEPENDIENDO EL TAMAÑO SELECCIONADO

        self.pintarComboEstados(self.frameCentral)

    def pintarComboEstados(self,contenedor):
        self.banderaActivaNodos = 1
        contadorComboEstados = 0
        Label(contenedor,
            bg="white" ,text= "Nodo inicial:",
            font =('Times New Roman', 15)).place(relx=0.05,rely=0.30,relwidth=0.21,relheight=0.08)#Creamos una etiqueta
        self.comboNodoInicial = ttk.Combobox(contenedor,
            state="readonly",justify=CENTER ,
            font =('Times New Roman', 20))#creamos una lista desplegable
        self.comboNodoInicial["values"] = self.arregloNodos#agregamos valores a la lista desplegable
        self.comboNodoInicial.current(0)#seleccionamos el item en la primera pósicion
        self.comboNodoInicial.place(relx=0.05,rely=0.40,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
        
        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.30,rely=0.30,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
            self.combo1Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo1Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo1Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo1Estado.place(relx=0.30,rely=0.40,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1
        
        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.55,rely=0.30,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
            self.combo2Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo2Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo2Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo2Estado.place(relx=0.55,rely=0.40,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1

        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.79,rely=0.30,relwidth=0.21,relheight=0.08)#Creamos una etiqueta
            self.combo3Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo3Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo3Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo3Estado.place(relx=0.79,rely=0.40,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1

        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.05,rely=0.55,relwidth=0.21,relheight=0.08)#Creamos una etiqueta
            self.combo4Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo4Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo4Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo4Estado.place(relx=0.05,rely=0.65,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1

        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.30,rely=0.55,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
            self.combo5Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo5Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo5Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo5Estado.place(relx=0.30,rely=0.65,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1

        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.55,rely=0.55,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
            self.combo6Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo6Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo6Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo6Estado.place(relx=0.55,rely=0.65,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1

        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.79,rely=0.55,relwidth=0.21,relheight=0.08)#Creamos una etiqueta
            self.combo7Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo7Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo7Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo7Estado.place(relx=0.79,rely=0.65,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1

        if contadorComboEstados < self.definirNumeroNodos:
            Label(contenedor,
                bg="white" ,text= "Nodo: " + self.arregloNodos[contadorComboEstados],
                font =('Times New Roman', 15)).place(relx=0.05,rely=0.80,relwidth=0.2,relheight=0.08)#Creamos una etiqueta
            self.combo8Estado = ttk.Combobox(contenedor,
                state="readonly",justify=CENTER ,
                font =('Times New Roman', 20))#creamos una lista desplegable
            self.combo8Estado["values"] = ["normal", "final"]#agregamos valores a la lista desplegable
            self.combo8Estado.current(0)#seleccionamos el item en la primera pósicion
            self.combo8Estado.place(relx=0.05,rely=0.90,relwidth=0.20,relheight=0.1)#le damos tamaño y posicionamos la lista desplegable
            contadorComboEstados = contadorComboEstados + 1

    def salirInterfaz(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()
        self.ventana.after(400, self.regresarVentanaPrincipal)

    def regresarVentanaPrincipal(self):
        self.ventana.destroy()#se destruye la ventana del splash
        interfacePrincipal.crearINPrincipal()

    def cambiarVentaFuncionT(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()
        self.ventana.after(400, self.vFuncionTransicion)

    def vFuncionTransicion(self):
        self.nodoInicialActivo = ""
        if self.banderaActivaNodos == 1:
            self.retornaEstadosNodos(0)
            self.retornaEstadosNodos(1)
            self.retornaEstadosNodos(2)
            self.retornaEstadosNodos(3)
            self.retornaEstadosNodos(4)
            self.retornaEstadosNodos(5)
            self.retornaEstadosNodos(6)
            self.retornaEstadosNodos(7)
            ####################################################################
            if self.banderaNodoIF == "inicialFinal" or (self.banderaNodoI == "inicial" and self.banderaNodoF == "final"):
                
                alfabetoAbc = self.afd.arrayAlfabeto()
                alfabetoAbc.insert(0, 'nodoNombre')#se añade el nombre de los nodos al arreglo del alfabeto
                tamanoAlfabeto = len(alfabetoAbc)
                tamanoNodos = len(self.arregloNodos)
                self.ventana.destroy()#se destruye la ventana del splash
                interfaceFuncionTransicion.crearInterfaceTabla(self.arregloNodos, alfabetoAbc, tamanoAlfabeto, tamanoNodos, self.afd.getTiposNodos() )
            else:
                messagebox.showwarning(message="Debe tener un nodo final", title="Advertencia")

        elif self.banderaActivaNodos == 0:
            messagebox.showwarning(message="Te hace falta definir estados", title="Advertencia") 

    def retornaEstadosNodos(self, valorX):
        if valorX < self.definirNumeroNodos:
            self.nodoInicialActivo=self.comboNodoInicial.get()
            #si el nodo es igual al nodo inicial y ademas es final
            if(self.arregloNodos[valorX] ==  self.nodoInicialActivo and self.retornaCombo(valorX) == "final"):
                print("111111Nodo: ", self.arregloNodos[valorX],"Estado: inicialFinal")   
                ##################################################################
                self.afd.setTiposNodos(self.arregloNodos[valorX], "inicialFinal")  
                self.banderaNodoIF = "inicialFinal"              
            else:
                #Si el nodo es igul al nodo inicial pero no es final
                if(self.arregloNodos[valorX] ==  self.nodoInicialActivo and self.retornaCombo(valorX) != "final"):
                    print("22222Nodo: ", self.arregloNodos[valorX],"Estado: inicial")
                    self.afd.setTiposNodos(self.arregloNodos[valorX], "inicial")
                    self.banderaNodoI = "inicial"
                else:
                    #Si el nodo no es el nodo inicial y tiene estados, final o normal
                    print("3333Nodo: ", self.arregloNodos[valorX],"Estado: ", self.retornaCombo(valorX) )
                    ##################################################################
                    self.afd.setTiposNodos(self.arregloNodos[valorX], self.retornaCombo(valorX))
                    if self.retornaCombo(valorX) == "final":
                        self.banderaNodoF = "final"

    def retornaCombo(self, valorX):
        if valorX == 0:
            return self.combo1Estado.get()
        elif valorX == 1:
            return self.combo2Estado.get()
        elif valorX == 2:
            return self.combo3Estado.get()
        elif valorX == 3:
            return self.combo4Estado.get()
        elif valorX == 4:
            return self.combo5Estado.get()
        elif valorX == 5:
            return self.combo6Estado.get()
        elif valorX == 7:
            return self.combo7Estado.get()
        elif valorX == 8:
            return self.combo8Estado.get()
#####################################################################################
def crearINPrincipal():
    INprincipal = VentanaPrincipal()
#####################################################################################

class Nodo():
    def __init__(self, nombre, estado):
        self.nombre=nombre
        self.estado=estado

    def setNombre(self, nom):
        self.nombre=nom

    def getNombre(self):
        return self.nombre

    def setEstado(self,est):
        self.estado=est
    
    def getEstado(self):
        return self.estado

class arrayNodoAlfabeto():
    def __init__(self,valorNodo, valorAlfabeto, tamanoNodo, tamanoAlfabeto):
        self.valorNodo = valorNodo
        self.valorAlfabeto = valorAlfabeto
        self.tamanoNodo = tamanoNodo
        self.tamanoAlfabeto = tamanoAlfabeto
        self.listaNodos=[]

    nombreABCM =['A','B','C','D','E','F','G','H']
    nombreQ =['q0','q1','q2','q3','q4','q5','q6','q8']
    nombre012 =['N0','N1','N2','N3','N4','N5','N6','N8']

    alfabetoAbc=['a', 'b', 'c']
    alfabeto012=['0', '1', '2']
    alfabeto0xyz=['x', 'y', 'z']


    def getNombreNodo(self, valorNodo):
        if valorNodo == "A,B,C,D":
            return  self.nombreABCM
        elif valorNodo == "q0,q1,q2,q3":
            return self.nombreQ
        elif valorNodo =="N0,N1,N2":
            return self.nombre012
    
    def getNombreAlfabeto(self, valorAlfabeto):
        if valorAlfabeto == "a,b,c":
            return self.alfabetoAbc
        elif valorAlfabeto == "0,1,2":
            return self.alfabeto012
        elif valorAlfabeto == "x,y,z":
            return self.alfabeto0xyz
    
    def arrayNodo(self):
        i = self.tamanoNodo
        self.arrayNodoFinal=[]
        for Nodo in self.getNombreNodo(self.valorNodo):
            if i > 0:
                self.arrayNodoFinal.append(Nodo)
                i=i-1
            else:
                break
        return self.arrayNodoFinal

    def arrayAlfabeto(self):
        i = self.tamanoAlfabeto
        self.arrayAlfabetoFinal=[]
        for alfabeto in self.getNombreAlfabeto(self.valorAlfabeto):
            if i > 0:
                self.arrayAlfabetoFinal.append(alfabeto)
                i=i-1
            else:
                break
        return self.arrayAlfabetoFinal
    
    def setTiposNodos(self, nodoNombre, nodoEstado):
        self.nodo = Nodo(nodoNombre, nodoEstado)
        self.listaNodos.append(self.nodo)
    
    def getTiposNodos(self): 
        return self.listaNodos