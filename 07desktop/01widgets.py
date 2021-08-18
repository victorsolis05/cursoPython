from tkinter import Button, Entry, Tk, Label

def miFuncion():
    print("Hola desde mi funcion")

ventana = Tk()
ventana.title("HOla mundo")
ventana.geometry("400x200")

lbl = Label(ventana, text= "Esto es un label")
lbl.pack()

btn = Button(ventana, text="Presionar", command=lambda : print("Hola"))
btn = Button(ventana, text="Presionar", command=miFuncion)
btn.pack()

txt1 = Entry(ventana)
txt1.pack()

ventana.mainloop()