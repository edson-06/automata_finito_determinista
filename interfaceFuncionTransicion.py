from tkinter import *
import pygame
import interfaceDatos
from tkinter import ttk
from tkinter import messagebox
import graphviz
import interfaceAFD
import time

class TablaTranscisiones(object):
    """docstring for TablaTranscisiones"""
    def __init__(self, arrayN, arrayA, tamanoAlfabeto, tamanoNodos, nodosEstado):
        self.ventana = Tk()
        self.ventana.geometry("1200x650")
        self.ventana.minsize(width=1000, height=550)
        self.ventana.config(padx=3, pady=5)
        self.arrayNodo = arrayN
        self.arrayA = arrayA
        self.tamanoNodo = tamanoNodos
        self.tamanoAlfabeto = tamanoAlfabeto
        self.banderaActiva = 0;
        self.nodosYEstado = nodosEstado

        self.banderaAlfabetoVacio=0

        self.createContainers(self.ventana)                
        self.ventana.mainloop()

        

    def createContainers(self, contenedor):
        frameArriba = frameArriba = Frame(contenedor,bd=5,relief=RIDGE,padx=5)
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

        self.componentesContenedorCentral(frameCentral)

    
    def salirInterfaz(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()
        self.ventana.after(400, self.regresarVentanaPrincipal)

    def generarAFD(self):
        pygame.mixer.Sound("sonidos/click2.mp3").play()
        self.generarTransiciones()

    def regresarVentanaPrincipal(self):
        self.ventana.destroy()#se destruye la ventana del splash
        interfaceDatos.crearINPrincipal()
    
    def componentesContenedorCentral(self, ventana):
        self.game_frame = Frame(ventana)
        self.game_frame.pack()

        #SCROLLBAR
        self.game_scroll = Scrollbar(self.game_frame)
        self.game_scroll.pack(side=RIGHT, fill=Y)

        self.game_scroll = Scrollbar(self.game_frame,orient='horizontal')
        self.game_scroll.pack(side= BOTTOM,fill=X)

        self.my_game = ttk.Treeview(self.game_frame,yscrollcommand=self.game_scroll.set, xscrollcommand =self.game_scroll.set)

        self.my_game.pack()

        self.game_scroll.config(command=self.my_game.yview)
        self.game_scroll.config(command=self.my_game.xview)

        #FORMATO DE LA TABLA
        self.formatoTablaTrans()

        #AÑADIENDO DATOS 
        self.addDatosTabla()
        #POSICIONAMIENTO
        self.my_game.pack()

        #ETIQUETAS Y CAJAS
        self.labeslCajasTexto(ventana)

        #BOTONES
        self.posicionBotones(ventana)

    def labeslCajasTexto(self,ventana):
        #FRAME
        self.frame = Frame(ventana)
        self.frame.pack(pady=20)
        #ETIQUETAS
        contadorLE = 1
        self.nodoEscogido= Label(self.frame,text = "Nodo")
        self.nodoEscogido.grid(row=0,column=0 )
        #CAJAS DE TEXTO
        #el usuario solo ve pero no puede escribir
        self.nodoEscogido_entry= Entry(self.frame)
        self.nodoEscogido_entry.grid(row= 1, column=0)

        if contadorLE < self.tamanoAlfabeto:
            #ETIQUETAS
            self.alfabetoA = Label(self.frame,text=self.arrayA[contadorLE])
            self.alfabetoA.grid(row=0,column=1)
            #CAJAS DE TEXTO
            self.alfabetoA_entry = Entry(self.frame)
            self.alfabetoA_entry.grid(row=1,column=1)
            contadorLE = contadorLE + 1

        if contadorLE < self.tamanoAlfabeto:
            #ETIQUETAS
            self.alfabetoB = Label(self.frame,text=self.arrayA[contadorLE])
            self.alfabetoB.grid(row=0,column=2)
            #CAJAS DE TEXTO
            self.alfabetoB_entry = Entry(self.frame)
            self.alfabetoB_entry.grid(row=1,column=2)
            contadorLE = contadorLE + 1

        if contadorLE < self.tamanoAlfabeto:
            #ETIQUETAS
            self.alfabetoC = Label(self.frame,text=self.arrayA[contadorLE])
            self.alfabetoC.grid(row=0,column=3)
            #CAJAS DE TEXTO
            self.alfabetoC_entry = Entry(self.frame)
            self.alfabetoC_entry.grid(row=1,column=3)
            contadorLE = contadorLE + 1

    def formatoTablaTrans(self):
        #DEFINE COLUMNAS
        print(self.arrayA)
        self.my_game['columns'] = self.arrayA
        print(type(self.my_game))
        # FORMATO A COLUMNAS
        self.my_game.column("#0", width=0,  stretch=NO)
        self.my_game.column("nodoNombre",anchor=CENTER, width=80)
        for x in range(1,self.tamanoAlfabeto):
            nombreAlfabeto = self.arrayA[x] + ""
            self.my_game.column(nombreAlfabeto,anchor=CENTER,width=80)
        #CREA ENCABEZADOS 
        self.my_game.heading("#0",text="",anchor=CENTER)
        self.my_game.heading("nodoNombre",text="Nodo",anchor=CENTER)
        for x in range(1, self.tamanoAlfabeto):
            nombreAlfabeto = self.arrayA[x] + ""
            self.my_game.heading(nombreAlfabeto,text=nombreAlfabeto,anchor=CENTER)

    def addDatosTabla(self):
        valoresNodos=[]
        for x in range(0, self.tamanoNodo):
            del valoresNodos[:]
            valoresNodos.append(self.arrayNodo[x])
            for i in range(1, self.tamanoAlfabeto):
                valoresNodos.append(' ')
                print("a")
            print(valoresNodos)
            self.my_game.insert(parent='',index='end',iid = x,text='',values=valoresNodos)
    
    #SELECCIONAR FILA
    def select_record(self):
        self.banderaActiva = 1;
        self.limpiarCajasTexto()
        contadorLE = 0
        #GUARDAR FILA SELECCIONADA
        self.selected=self.my_game.focus()
        #GUARDAR VALORES
        self.values = self.my_game.item(self.selected,'values')

        #output to entry boxes
        print("----------",self.selected)
        if self.selected == '':
            messagebox.showwarning(message="Por favor selecciona una fila", title="Advertencia") 
        else:

            if contadorLE < self.tamanoAlfabeto:
                self.nodoEscogido_entry.insert(0,self.values[0])
                contadorLE = contadorLE + 1
            if contadorLE < self.tamanoAlfabeto: 
                self.alfabetoA_entry.insert(0,self.values[1])
                contadorLE = contadorLE + 1
            if contadorLE < self.tamanoAlfabeto:
                self.alfabetoB_entry.insert(0,self.values[2])
                contadorLE = contadorLE + 1
            if contadorLE < self.tamanoAlfabeto:
                self.alfabetoC_entry.insert(0,self.values[3])  
                contadorLE = contadorLE + 1

    #ACTUALIZANDO VALORES
    def update_record(self):
        print("guardando valores: " , self.tamanoAlfabeto)
        print("alfabeto: ", self.arrayA )
        self.selected=self.my_game.focus()
        #GUARDAR LOS DATOS NUEVOS
        if self.tamanoAlfabeto == 2:
            print("tamaño del alfabeto 1: " , self.tamanoAlfabeto)
            self.my_game.item(self.selected,text="",values=(self.values[0],self.alfabetoA_entry.get()))
        if self.tamanoAlfabeto == 3:
            print("tamaño del alfabeto 2: " , self.tamanoAlfabeto)
            print(self.alfabetoA_entry.get()," : ",self.alfabetoB_entry.get())
            self.my_game.item(self.selected,text="",values=(self.values[0],self.alfabetoA_entry.get(),self.alfabetoB_entry.get()))
        if self.tamanoAlfabeto == 4:
            print("tamaño del alfabeto 3: " , self.tamanoAlfabeto)
            self.my_game.item(self.selected,text="",values=(self.values[0],self.alfabetoA_entry.get(),self.alfabetoB_entry.get(),self.alfabetoC_entry.get()))
        
        self.limpiarCajasTexto()
        self.banderaActiva = 0;

    def limpiarCajasTexto(self):
        contadorLE = 0
        #LIMPIANDO CAJAS DE TEXTO, COMPARA SI EL NUMERO DE CONTADOR DE LABELS Y ENTRYS ES DEL NUMERO DEFINIDO, ENTONCES LOS LIMPIA
        if contadorLE < self.tamanoAlfabeto:
            self.nodoEscogido_entry.delete(0,END)
            contadorLE = contadorLE + 1
        if contadorLE < self.tamanoAlfabeto:
            self.alfabetoA_entry.delete(0,END)
            contadorLE = contadorLE + 1
        if contadorLE < self.tamanoAlfabeto:
            self.alfabetoB_entry.delete(0,END)
            contadorLE = contadorLE + 1
        if contadorLE < self.tamanoAlfabeto:
            self.alfabetoC_entry.delete(0,END)
            contadorLE = contadorLE + 1

    def posicionBotones(self,ventana):
        #BOTONES
        self.select_button = Button(ventana,text="Selecionar", command=self.select_record)
        self.select_button.pack(pady =10)

        self.edit_button = Button(ventana,text="Editar ",command=self.select_update)
        self.edit_button.pack(pady = 10)

    def select_update(self):
        #FUNCION QUE SELECCIONA Y ACTUALIZA EL VALOR ESCOGIDO
        if(self.nodoEscogido_entry.get() == "" or self.banderaActiva == 0):
            messagebox.showwarning(message="Debes presionar seleccionar \nantes de actualizar", title="Advertencia")
        else:
            self.update_record()

    def limpiaCadena(self,txt):
        caracteres = " '"
        for sp in caracteres:
            txt = txt.replace(sp,'')
        return txt

    def generarTransiciones(self):
        self.cadenaGenerarT = []
        self.cadena =[]


        #inicializacion de la clase transicionesNodos
        generarTransNodos = transicionesNodos(self.nodosYEstado)
        generarTransNodos.recorridoNodosEstado()
        print("inicializando nuevamnete bandera: ", self.banderaAlfabetoVacio)
        self.banderaAlfabetoVacio = 0###########################################################################
        #ciclo para recorrer nodos
        for x in range(0, self.tamanoNodo):
            #valor de la variable
            #GUARDAR VALORES
            self.values = self.my_game.item(x,'values') #se guardan las variables
            for alfa in range(1, self.tamanoAlfabeto):              #ciclo para recorrer el alfabeto
                nodo1 = self.limpiaCadena(self.values[0])
                nodo2 = self.limpiaCadena(self.values[alfa])
                nodo3 = self.limpiaCadena(self.arrayA[alfa])
                #Si tiene valor no esta vacio
                if nodo2 and nodo2.strip():
                    if nodo2 not in self.arrayNodo:
                        messagebox.showwarning(message=nodo2+" no pertenece", title="Advertencia")
                        self.banderaAlfabetoVacio = 1
                        print("Cambiando bandera: ", self.banderaAlfabetoVacio)
                    else:
                        print(nodo1,":",nodo2,":",nodo3) #impresion de valores
                        generarTransNodos.setTransision(nodo1,nodo2,nodo3)
                        #generarndo la transisicon con los datos corre3ctos
                        self.cadenaGenerarT = (nodo1,nodo2,nodo3)
                        self.cadena.append(self.cadenaGenerarT)
                else:
                    self.banderaAlfabetoVacio = 1
                    
        print("Comparando bandera final bandera: ", self.banderaAlfabetoVacio)
        if self.banderaAlfabetoVacio == 0:
            pygame.mixer.Sound("sonidos/click2.mp3").play()
            messagebox.showwarning(message="es un Automata Finito Determinista", title="Advertencia")
            ################################# metodo para generar la imagen
            
            for x in self.cadena:
                pass
                #generarTransNodos.setTransision(self.cadenaGenerarT[0],self.cadenaGenerarT[1],self.cadenaGenerarT[2])
                #print("|",self.cadenaGenerarT[0],":",self.cadenaGenerarT[1],":",self.cadenaGenerarT[2],"|")
            
            generarTransNodos.generarImagen()
            self.ventana.destroy()#se destruye la ventana del splash
            self.mostrarVentanaAutomata()
            

        else:
            messagebox.showwarning(message="NO es un Automata Finito Determinista", title="Advertencia")

    def mostrarVentanaAutomata(self):
        #time.sleep(5) 
        interfaceAFD.crearIAFD()

##############################################################################################################
def crearInterfaceTabla(nodos, alfabeto, tamanoAlfabeto, tamanoNodos, nodosEstado):
    TablaTranscisiones(nodos, alfabeto, tamanoAlfabeto, tamanoNodos, nodosEstado)
##############################################################################################################
class transicionesNodos():
    def __init__(self,listaTiposNodos):
        self.listaTiposNodos=listaTiposNodos
        self.componentesGrap()

    def componentesGrap(self):
        self.f = graphviz.Digraph('finite_state_machine', filename='imgAutomata.gv',format="png")
        self.f.attr(rankdir='LR', size='8,5')

    def recorridoNodosEstado(self):
        for n in self.listaTiposNodos:
            if n.getEstado() == "inicial":
                ppppppp= ""+n.getNombre()
                print("nodo inicial: ", ppppppp)
                #nodo inicial
                self.f.node('LR_234', shape="point")
                #nodos
                self.f.attr('node', shape='circle')
                self.f.edge('LR_234', ppppppp, label='')

            elif n.getEstado() == "final":
                ppppppp= ""+n.getNombre()
                print("nodo FINAL: ", ppppppp)
                self.f.attr('node', shape='doublecircle')
                self.f.node(ppppppp)

            elif n.getEstado() == "inicialFinal":
                ppppppp= ""+n.getNombre()
                print("nodo inicial: ", ppppppp)
                #nodo inicial
                self.f.node('LR_234', shape="point")
                #nodos
                self.f.attr('node', shape='doublecircle')
                self.f.edge('LR_234', ppppppp, label='')

    def setTransision(self, nombreEstado, estadoSiguiente, letraAlfabeto):
        self.f.attr('node', shape='circle')
        print("*******************************************************")
        print(nombreEstado,"|", estadoSiguiente,"|",letraAlfabeto)
        print("*******************************************************")
        self.f.edge(nombreEstado, estadoSiguiente, label=letraAlfabeto)

    def generarImagen(self):
        self.f.render()