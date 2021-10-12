#GENERIS_APP
# Las dos líneas siguientes son necesarias para hacer 
# compatible la interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import tkinter as tk #en lugar de escibir tikinter siempre solo se pone tk
app= tk.Tk() #Nombre del menu de app
app.geometry("400x400") # Da geometria de la pantalla de la app cuando se abre
app.configure(background="beige") #Da color al fondo de la app
tk.Wm.wm_title(app,"Generis") #Titulo a app cuando se abre 
Label(app, text="Nombre:").grid(pady=5, row=0, column=0)
Button(app, text="Nombre:").grid(pady=5, row=0, column=1)
#tk.Button( 
 #   app,
 #   text="Informacion",
 #   font= ("Arial, 14"),
 #   bg= "#38B6FF",
 #   fg="white",
#).pack(
#)# de tk button hastaa aqui es un ejemplo del formato para crear botones















app.mainloop()#Mantiene en constante actualizacion la app 
