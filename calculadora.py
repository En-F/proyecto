"""
Hacer Calculadora
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Aplication(tk.Tk):
    """La Calculadora"""
    
    
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.option_add("*Font", ("Arial", 18))
        
        self.pantalla = tk.Entry(self, justify="right")
        self.pantalla.grid(row=0, column=0, padx=5,columnspan=4, ipadx=10, ipady=10, pady= 5 )
        


def calcular(self, event=None) -> None:
    """Calcula el resultado"""
    pass


app = Aplication()
app.mainloop()