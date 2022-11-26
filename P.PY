from tkinter import *
from tkinter import messagebox
from math import trunc
c = Canvas

def dsy1():
            ventana_desayuno1=Tk()
            ventana_desayuno1.title("Desayunos")
            ventana_desayuno1.geometry("1000x500")
            ventana_desayuno1.resizable(0,0)
            ventana_desayuno1.config(bg= "springgreen4")
            tren = Label(ventana_desayuno1, text= "\n---DESAYUNOS---\n 1.-Tortilla con queso y hierbas-\n\nIngredientes: 3 huevos batidos, 1 cucharada de hierbas de olor, \n1 cucharada de mantequilla sin sal, 50 gramos de queso. \n\nModo de preparar: \nse mezcla todos los ingredientes excepto la mantequilla y el queso.\ncalienta la mantequilla en un sartén y cuando esté caliente agrega la mezcla.\n Espera hasta que se forme el omelet, \nentonces coloca el queso encima y dobla por la mitad, \nse cocina por un minuto hasta que se derrita el queso y disfruta.")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)
    
             
        
def dsy2():
            ventana_desayuno2=Tk()
            ventana_desayuno2.title("Desayunos")
            ventana_desayuno2.geometry("1000x500")
            ventana_desayuno2.resizable(0,0)
            ventana_desayuno2.config(bg= "springgreen4")
            tren = Label(ventana_desayuno2, text= "\n---DESAYUNOS---\n\n2.-Panquecas de plátano-\n\nIngredientes: Tres plátanos hechos puré,100 gramos de mantequilla, \n1 cucharada de miel. \n\nPreparación: forma las panquecas con el puré de plátano. \nUna vez formadas, fríelas en la mantequilla una por una, \npor alrededor de dos minutos.\nacompaña con miel y disfruta")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)
            
def dsy3():
            ventana_desayuno2=Tk()
            ventana_desayuno2.title("Desayunos")
            ventana_desayuno2.geometry("1000x500")
            ventana_desayuno2.resizable(0,0)
            ventana_desayuno2.config(bg= "springgreen4")
            tren = Label(ventana_desayuno2, text= "\n---DESAYUNOS---\n\n 3.--Batido de papaya y piña--\n\nIngredientes: 1 taza, (225 gramos) de piña en trozos,\nmedia taza (120 gramos) de papaya en \ntrozos, media taza (125 ml) de cubos de hielo,\n60 ml de miel. \n\nPreparación: Vierte todos los ingredientes en la licuadora y \nlicúa hasta que se mezclen.")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)
        
def alm1():
            ventana_almuerzo1=Tk()
            ventana_almuerzo1.title("Almuerzos.")
            ventana_almuerzo1.geometry("1000x500")
            ventana_almuerzo1.resizable(0,0)
            ventana_almuerzo1.config(bg= "springgreen4")
            tren = Label(ventana_almuerzo1, text= "")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)
            
def alm2():
            ventana_almuerzo2=Tk()
            ventana_almuerzo2.title("Almuerzos.")
            ventana_almuerzo2.geometry("1000x500")
            ventana_almuerzo2.resizable(0,0)
            ventana_almuerzo2.config(bg= "springgreen4")
            tren = Label(ventana_almuerzo2, text= "")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)

def alm3():
            ventana_almuerzo3=Tk()
            ventana_almuerzo3.title("Almuerzos.")
            ventana_almuerzo3.geometry("1000x500")
            ventana_almuerzo3.resizable(0,0)
            ventana_almuerzo3.config(bg= "springgreen4")
            tren = Label(ventana_almuerzo3, text= "")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)
            
def cmd1():
            ventana_almuerzo1=Tk()
            ventana_almuerzo1.title("Comida.")
            ventana_almuerzo1.geometry("1000x500")
            ventana_almuerzo1.resizable(0,0)
            ventana_almuerzo1.config(bg= "springgreen4")
            tren = Label(ventana_almuerzo1, text= "")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)
            
def cmd2():
            ventana_almuerzo2=Tk()
            ventana_almuerzo2.title("Comida.")
            ventana_almuerzo2.geometry("1000x500")
            ventana_almuerzo2.resizable(0,0)
            ventana_almuerzo2.config(bg= "springgreen4")
            tren = Label(ventana_almuerzo2, text= "")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)

def cmd3():
            ventana_almuerzo3=Tk()
            ventana_almuerzo3.title("Comida.")
            ventana_almuerzo3.geometry("1000x500")
            ventana_almuerzo3.resizable(0,0)
            ventana_almuerzo3.config(bg= "springgreen4")
            tren = Label(ventana_almuerzo3, text= "")
            tren.config(bg="springgreen4", fg="black", font=("Arial",19))
            tren.place(x=50,y=5, width=900, height=400)




ventana_principal = Tk()

ventana_principal.title("SEAT")

# tamañan de la ventana
ventana_principal.geometry("1100x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)


# color de fondo de la ventana
bg = PhotoImage( file = "foto/img.png") 
label1 = Label( ventana_principal, image = bg) 
label1.place(x = 0,y = 0) 


#ventanas
frame_desayuno = Frame(ventana_principal)
frame_desayuno.config(bg = "black", width = 260 , height = 510 )
frame_desayuno.place(x = 75, y = 55)

frame_desayuno1 = Frame(ventana_principal)
frame_desayuno1.config(bg = "white", width = 250 , height = 500 )
frame_desayuno1.place(x = 80, y = 60)

frame_almuerzo = Frame(ventana_principal)
frame_almuerzo.config(bg = "black", width = 260 , height = 510 )
frame_almuerzo.place(x = 395, y = 55)

frame_almuerzo = Frame(ventana_principal)
frame_almuerzo.config(bg = "white", width = 250 , height = 500 )
frame_almuerzo.place(x = 400, y = 60)

frame_comida = Frame(ventana_principal)
frame_comida.config(bg = "black", width = 260 , height = 510 )
frame_comida.place(x = 715, y=55)

frame_comida = Frame(ventana_principal)
frame_comida.config(bg = "white", width = 250 , height = 500 )
frame_comida.place(x = 720, y=60)

titulo = Label(ventana_principal, text= "PROYECTO SEAT")
titulo.config(bg="black", fg="white", font=("Arial",20))
titulo.place(x=350,y=10, width=400, height=40)

#BOTONES DESAYUNO

bt_desayunos1 = Button(ventana_principal,text="Tortillas con queso y hierbas.", command=dsy1)
bt_desayunos1.place(x=120, y=300, width=160, height=30)
        
bt_desayunos2 = Button(ventana_principal,text="Panquecas de platano.", command=dsy2)
bt_desayunos2.place(x=120, y=350, width=160, height=30)
        
bt_desayunos3 = Button(ventana_principal,text="Batido de papaya y piña", command=dsy3)
bt_desayunos3.place(x=120, y=400, width=160, height=30)

#BOTONES ALMUERZO

bt_almuerzo1 = Button(ventana_principal,text="Tortillas con queso y hierbas.", command=alm1)
bt_almuerzo1.place(x=250, y=50, width=160, height=30)

bt_almuerzo2 = Button(ventana_principal,text="Tortillas con queso y hierbas.", command=alm2)
bt_almuerzo2.place(x=250, y=100, width=160, height=30)

bt_almuerzo3 = Button(ventana_principal,text="Tortillas con queso y hierbas.", command=alm3)
bt_almuerzo3.place(x=250, y=150, width=160, height=30)

#BOTONES COMIDA
bt_comida1 = Button(ventana_principal,text="Tortillas con queso y hierbas.", command=cmd1)
bt_comida1.place(x=450, y=50, width=160, height=30)

bt_comida2 = Button(ventana_principal,text="Tortillas con queso y hierbas.", command=cmd2)
bt_comida2.place(x=450, y=100, width=160, height=30)

bt_comida3 = Button(ventana_principal,text="Tortillas con queso y hierbas.", command=cmd3)
bt_comida3.place(x=450, y=150, width=160, height=30)


gg= PhotoImage(file="foto/y.png")
label3= Label(frame_desayuno1, image=gg)
label3.place(x=10, y=10)
#detalles
ventana_principal.mainloop()

#marcos
