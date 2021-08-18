from tkinter import Button, Entry, Frame, StringVar, Tk, Label 
from tkinter.constants import LEFT, RIGHT, X, YES

def suma():
    n1 = entrada1.get()
    n2 = entrada2.get()
    respuesta = int(n1) + int(n2)
    entrada3.delete(0, "end")
    entrada3.insert(0, respuesta)
    labelRespuesta = Label(root, text=respuesta, bg="yellow")
    labelRespuesta.pack()

root = Tk()
root.title("Ejemplo de Suma con posicion Pack")
root.geometry("400x200")

row = Frame(root)
row.pack(fill=X)
label1 = Label(row, text="Primer numero", bg="green")
label1.pack(side=LEFT)

entrada1 = Entry(row, bg="pink")
entrada1.pack(side=RIGHT, fill=X, expand=YES)

#TODO: Etiqueta y entrada del número 2

row2 = Frame(root)
row2.pack(fill=X)
label2 = Label(row2, text="Segundo numero", bg="blue")
label2.pack(side=LEFT)

entrada2 = Entry(row2, bg="pink")
entrada2.pack(side=RIGHT, fill=X, expand=YES)

row3 = Frame(root)
row3.pack(fill=X)
label3 = Label(row3, text="Resultado", bg="yellow")
label3.pack(side=LEFT)

entrada3 = Entry(row3, bg="yellow")
entrada3.pack(side=RIGHT, fill=X, expand=YES)

btn = Button(root, text="Sumar", command=suma)

btn.pack()

root.mainloop()