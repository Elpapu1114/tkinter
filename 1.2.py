import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Alineación táctica")
ventana.geometry("600x770")
ventana.resizable(False, False)

imagenes = []

img = Image.open("assets/cancha.png")
img = img.resize((600, 770))
cancha_img = ImageTk.PhotoImage(img)
imagenes.append(cancha_img)

fondo = tk.Label(ventana, image=cancha_img)
fondo.place(x=0, y=0)

def hacer_movible(widget):
    def iniciar_mov(event):
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def mover(event):
        x = widget.winfo_x() + event.x - widget._drag_start_x
        y = widget.winfo_y() + event.y - widget._drag_start_y
        widget.place(x=x, y=y)

    widget.bind("<Button-1>", iniciar_mov)
    widget.bind("<B1-Motion>", mover)

def cargar_jugador(ruta, x, y):
    img = Image.open(ruta)
    img = img.resize((100, 106))
    
    img = img.rotate(90, expand=True)

    img_tk = ImageTk.PhotoImage(img)
    imagenes.append(img_tk)

    label = tk.Label(ventana, image=img_tk, bd=0)
    label.place(x=x, y=y)

    hacer_movible(label)

cargar_jugador("assets/courtois.png", 50, 330)

cargar_jugador("assets/nuno.png", 150, 120)
cargar_jugador("assets/saliba.png", 150, 260)
cargar_jugador("assets/gabriel.png", 150, 400)
cargar_jugador("assets/hakimi.png", 150, 540)

cargar_jugador("assets/pedri.png", 270, 250)
cargar_jugador("assets/valverde.png", 270, 420)

cargar_jugador("assets/yamal.png", 400, 120)
cargar_jugador("assets/olise.png", 400, 330)
cargar_jugador("assets/mbappe.png", 400, 540)

cargar_jugador("assets/kane.png", 520, 330)

ventana.mainloop()