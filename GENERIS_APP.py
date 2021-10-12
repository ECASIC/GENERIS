#GENERIS_APP
# Las dos líneas siguientes son necesarias para hacer 
# compatible la interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 
from tkinter import messagebox
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk, font  # Carga ttk (para widgets nuevos 8.5+)
import getpass
import tkinter as tk #en lugar de escibir tkinter siempre solo se pone tk
from tkinter import ImageTk, Image
img_logo = ImageTk.PhotoImage(Image.open("app.png"))
class aplicacion():
    def __init__(self):
        self.app = Tk()
        self.app.title("Generis") #Nombre del menu de app
        self.app.resizable(0,0)
        fuente = font.Font(weight='bold')# Da geometria de la pantalla de la app cuando se abre
    # Define un widget de tipo 'Frame' (marco) que será el
        # contenedor del resto de widgets. El marco se situará 
        # en la ventana 'self.raiz' ocupando toda su extensión.
        # El marco se define con un borde de 2 píxeles y la
        # opción 'relief' con el valor 'raised' (elevado) añade
        # un efecto 3D a su borde. 
        # La opción 'relief' permite los siguientes valores:
        # FLAT (llano), RAISED (elevado), SUNKEN (hundido),
        # GROOVE (hendidura) y RIDGE (borde elevado).
        # La opción 'padding' añade espacio extra interior para
        # que los widgets no queden pegados al borde del marco.
          
        self.marco = ttk.Frame(self.app, borderwidth=2,
                               relief="raised", padding=(50,150))
                               
        # Define el resto de widgets pero en este caso el primer 
        # paràmetro indica que se situarán en el widget del 
        # marco anterior 'self.marco'.
                               
        self.etiq1 = ttk.Label(self.marco, text="Usuario:", 
                               font=fuente, padding=(5,5))
                               
        self.etiq2 = ttk.Label(self.marco, text="Contraseña:",
                               font=fuente, padding=(5,5))
                               
        # Define variables para las opciones 'textvariable' de
        # cada caja de entrada 'ttk.Entry()'.
        
        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set(getpass.getuser())        
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.usuario, 
                                width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.clave, 
                                show="*", 
                                width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar", 
                                 padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar", 
                                 padding=(5,5), command=quit)
        
        # Define la ubicación de cada widget en el grid.
        # En este ejemplo en realidad hay dos grid (cuadrículas):
        # Una cuadrícula de 1fx1c que se encuentra en la ventana 
        # que ocupará el Frame; y otra en el Frame de 5fx3c para
        # el resto de controles.
        # La primera fila y primera columna serán la número 0.
        # La opción 'column' indica el número de columna y la
        # opción 'row' indica el número de fila donde hay que 
        # colocar un widget. 
        # La opción 'columnspan' indica al gestor que el 
        # widget ocupará en total un número determinado de
        # columnas. Las cajas para entradas 'self.ctext1' y
        # 'self.ctext2' ocuparán dos columnas y la barra
        # de separación 'self.separ1' tres.
        
        self.marco.grid(column=0, row=0)
        self.etiq1.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.etiq2.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)

        # Establece el foco en la caja de entrada de la
        # contraseña.

        self.ctext2.focus_set()
        self.app.mainloop()
    
    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contraseña:", self.ctext2.get())
        else:
            print("Acceso denegado")
            self.clave.set("")
            self.ctext2.focus_set()

def main():
    mi_app = aplicacion()
    return 0

if __name__ == '__main__':
    main()