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
        self.pantalla.grid(row=0, column=0, padx=5,columnspan=5, ipadx=10, ipady=10, pady= 5 )
        self.botonones()  
           
    def botonones(self):
        """Los botones"""
        boton_9 = tk.Button(self, text="9", command=lambda: self.boton_presionado("9"))
        boton_9.grid(row=1, column=2)

        boton_8 = tk.Button(self, text="8", command=lambda: self.boton_presionado("8"))
        boton_8.grid(row=1, column=1)

        boton_7 = tk.Button(self, text="7", command=lambda: self.boton_presionado("7"))
        boton_7.grid(row=1, column=0)

        boton_AC = tk.Button(self, text="AC", command=lambda: self.boton_presionado("AC"))
        boton_AC.grid(row=1, column=3)

        boton_menos = tk.Button(self, text="-", command=lambda: self.boton_presionado("-"))
        boton_menos.grid(row=3, column=3)

        boton_suma = tk.Button(self, text="+", command=lambda: self.boton_presionado("+"))
        boton_suma.grid(row=2, column=3)

        boton_igual = tk.Button(self, text="=", command=lambda: self.boton_presionado("="))
        boton_igual.grid(row=4, column=3)

        boton_mult = tk.Button(self, text="*", command=lambda: self.boton_presionado("*"))
        boton_mult.grid(row=4, column=1)

        boton_4 = tk.Button(self, text="4", command=lambda: self.boton_presionado("4"))
        boton_4.grid(row=2, column=0)

        boton_5 = tk.Button(self, text="5", command=lambda: self.boton_presionado("5"))
        boton_5.grid(row=2, column=1)

        boton_6 = tk.Button(self, text="6", command=lambda: self.boton_presionado("6"))
        boton_6.grid(row=2, column=2)

        boton_1 = tk.Button(self, text="1", command=lambda: self.boton_presionado("1"))
        boton_1.grid(row=3, column=0)

        boton_2 = tk.Button(self, text="2", command=lambda: self.boton_presionado("2"))
        boton_2.grid(row=3, column=1)

        boton_3 = tk.Button(self, text="3", command=lambda: self.boton_presionado("3"))
        boton_3.grid(row=3, column=2)

        botno_0 = tk.Button(self,text="0", command=lambda: self.boton_presionado("0"))
        botno_0.grid(row=4, column=0)

        botno_dividir = tk.Button(self,text="/", command=lambda: self.boton_presionado("/"))
        botno_dividir.grid(row=4, column=2)


    def boton_presionado(self,numero):
        """Lógica para lo que ocurre cuando se presiona un botón"""
        actual = self.pantalla.get()

        if numero == "AC":
            self.pantalla.delete(0, tk.END)  # Limpiar la pantalla
        elif numero == "=":
            try:
                resultado = eval(actual)  # Evaluar la expresión matemática
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, str(resultado))
            except Exception as e:
                messagebox.showerror("Error", f"Error en la operación: {e}")
        else:
            self.pantalla.insert(tk.END, numero)
        



app = Aplication()
app.mainloop()
