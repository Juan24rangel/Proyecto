from tkinter import *
from tkinter import messagebox
from math import trunc
c = Canvas
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

frame_desayuno = Frame(ventana_principal)
frame_desayuno.config(bg = "white", width = 250 , height = 500 )
frame_desayuno.place(x = 80, y = 60)

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

ventana_principal.mainloop()

#marcos
