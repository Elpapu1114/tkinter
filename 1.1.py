import tkinter as tk
from tkinter import messagebox
import math

def click(valor):
    entrada_actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, entrada_actual + str(valor))

def limpiar():
    pantalla.delete(0, tk.END)

def calcular():
    try:
        expresion = pantalla.get()
        
        for c in expresion:
            if c.isalpha():
                raise ValueError("Entrada inválida")

        resultado = eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))

    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero")
        limpiar()

    except:
        messagebox.showerror("Error", "Entrada inválida")
        limpiar()

def raiz():
    try:
        valor = float(pantalla.get())
        if valor < 0:
            raise ValueError
        resultado = math.sqrt(valor)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))

    except:
        messagebox.showerror("Error", "No se puede calcular la raíz")
        limpiar()

ventana = tk.Tk()
ventana.title("Calculadora")

pantalla = tk.Entry(ventana, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
pantalla.pack(fill="both", padx=10, pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack()

botones = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
    ('C', 4, 0), ('^', 4, 1), ('√', 4, 2)
]

for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(frame_botones, text=texto, width=5, height=2, command=calcular)
    elif texto == "C":
        boton = tk.Button(frame_botones, text=texto, width=5, height=2, command=limpiar)
    elif texto == "√":
        boton = tk.Button(frame_botones, text=texto, width=5, height=2, command=raiz)
    elif texto == "^":
        boton = tk.Button(frame_botones, text=texto, width=5, height=2, command=lambda: click("**"))
    else:
        boton = tk.Button(frame_botones, text=texto, width=5, height=2, command=lambda t=texto: click(t))
    
    boton.grid(row=fila, column=columna, padx=5, pady=5)

ventana.mainloop()