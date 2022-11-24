from tkinter import *
from tkinter import messagebox
from math import trunc

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


ventana_principal.mainloop()