#GENERIS_APP
# Las dos líneas siguientes son necesarias para hacer 
# compatible la interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 
from tkinter import messagebox
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk, font  # Carga ttk (para widgets nuevos 8.5+)
import getpass
import tkinter as tk #en lugar de escibir tkinter siempre solo se pone tk
class app():
    def __init__(self):
        self.app = Tk()
        self.app.title("Acceso") #Nombre del menu de app
        self.app.resizable(0,0)
        fuente = font.Font(weight='bold')# Da geometria de la pantalla de la app cuando se abre




#tk.Button( 
 #   app,
 #   text="Informacion",
 #   font= ("Arial, 14"),
 #   bg= "#38B6FF",
 #   fg="white",
#).pack(
#)# de tk button hastaa aqui es un ejemplo del formato para crear botones















app.mainloop()#Mantiene en constante actualizacion la app 
