import tkinter as tk
from tkinter import ttk, messagebox
import json  # Para guardar y cargar datos

archivo = "inventario.json"  # Nombre del archivo JSON

inventario = []  # Lista de productos

# =========================
# FUNCIONES JSON
# =========================

def cargar_datos():
    global inventario
    try:
        with open(archivo, "r") as f:
            inventario = json.load(f)
    except:
        inventario = []

def guardar_datos():
    with open(archivo, "w") as f:
        json.dump(inventario, f, indent=4)

# =========================
# VENTANA
# =========================

root = tk.Tk()
root.title("Sistema de Inventario")
root.geometry("900x400")

# =========================
# PANEL IZQUIERDO
# =========================

frame_izq = ttk.LabelFrame(root, text="Panel de Operaciones")
frame_izq.pack(side="left", fill="y", padx=10, pady=10)

ttk.Label(frame_izq, text="Código").grid(row=0, column=0)
ttk.Label(frame_izq, text="Nombre").grid(row=1, column=0)
ttk.Label(frame_izq, text="Precio").grid(row=2, column=0)
ttk.Label(frame_izq, text="Cantidad").grid(row=3, column=0)
ttk.Label(frame_izq, text="Categoría").grid(row=4, column=0)

entry_cod = ttk.Entry(frame_izq)
entry_nom = ttk.Entry(frame_izq)
entry_pre = ttk.Entry(frame_izq)
spin_cant = ttk.Spinbox(frame_izq, from_=0, to=1000)
entry_cat = ttk.Entry(frame_izq)

entry_cod.grid(row=0, column=1)
entry_nom.grid(row=1, column=1)
entry_pre.grid(row=2, column=1)
spin_cant.grid(row=3, column=1)
entry_cat.grid(row=4, column=1)

# =========================
# PANEL DERECHO
# =========================

frame_der = ttk.LabelFrame(root, text="Inventario")
frame_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

columnas = ("codigo", "nombre", "precio", "cantidad", "categoria")

tree = ttk.Treeview(frame_der, columns=columnas, show="headings")

for col in columnas:
    tree.heading(col, text=col.capitalize())
    tree.column(col, width=120, anchor="center")

scroll = ttk.Scrollbar(frame_der, orient="vertical", command=tree.yview)
tree.configure(yscroll=scroll.set)

tree.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

# =========================
# FUNCIONES
# =========================

def limpiar_campos():
    entry_cod.delete(0, tk.END)
    entry_nom.delete(0, tk.END)
    entry_pre.delete(0, tk.END)
    spin_cant.delete(0, tk.END)
    entry_cat.delete(0, tk.END)

def refrescar_tabla():
    for fila in tree.get_children():
        tree.delete(fila)

    for prod in inventario:
        tree.insert("", tk.END, values=(
            prod["codigo"],
            prod["nombre"],
            prod["precio"],
            prod["cantidad"],
            prod["categoria"]
        ))

def guardar():
    try:
        codigo = int(entry_cod.get())
        nombre = entry_nom.get()
        precio = float(entry_pre.get())
        cantidad = int(spin_cant.get())
        categoria = entry_cat.get()

        if nombre == "" or categoria == "":
            raise ValueError

        for prod in inventario:
            if prod["codigo"] == codigo:
                messagebox.showerror("Error", "Código ya existe")
                return

        nuevo = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }

        inventario.append(nuevo)
        guardar_datos()  # 💾 guarda en JSON
        refrescar_tabla()
        limpiar_campos()

    except:
        messagebox.showerror("Error", "Datos inválidos")

def seleccionar(event):
    item = tree.selection()
    if item:
        datos = tree.item(item)["values"]

        entry_cod.delete(0, tk.END)
        entry_nom.delete(0, tk.END)
        entry_pre.delete(0, tk.END)
        spin_cant.delete(0, tk.END)
        entry_cat.delete(0, tk.END)

        entry_cod.insert(0, datos[0])
        entry_nom.insert(0, datos[1])
        entry_pre.insert(0, datos[2])
        spin_cant.insert(0, datos[3])
        entry_cat.insert(0, datos[4])

tree.bind("<ButtonRelease-1>", seleccionar)

def modificar():
    try:
        codigo = int(entry_cod.get())

        for prod in inventario:
            if prod["codigo"] == codigo:
                prod["nombre"] = entry_nom.get()
                prod["precio"] = float(entry_pre.get())
                prod["cantidad"] = int(spin_cant.get())
                prod["categoria"] = entry_cat.get()

        guardar_datos()  # 💾 guarda cambios
        refrescar_tabla()

    except:
        messagebox.showerror("Error", "Error al modificar")

def borrar():
    try:
        codigo = int(entry_cod.get())

        for i in range(len(inventario)):
            if inventario[i]["codigo"] == codigo:
                del inventario[i]
                break

        guardar_datos()  # 💾 guarda cambios
        refrescar_tabla()
        limpiar_campos()

    except:
        messagebox.showerror("Error", "Error al borrar")

# =========================
# BOTONES
# =========================

ttk.Button(frame_izq, text="Guardar", command=guardar).grid(row=5, column=0, pady=5)
ttk.Button(frame_izq, text="Modificar", command=modificar).grid(row=5, column=1)
ttk.Button(frame_izq, text="Borrar", command=borrar).grid(row=6, column=0, columnspan=2)

# =========================
# INICIO
# =========================

cargar_datos()  # Carga JSON al iniciar
refrescar_tabla()  # Muestra datos

root.mainloop()