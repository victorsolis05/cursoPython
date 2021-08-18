from tkinter import Button, Entry, Tk, Label

def suma():
    n1 = entrada1.get()
    n2 = entrada2.get()
    respuesta = int(n1) + int(n2)
    entrada3.delete(0, "end")
    entrada3.insert(0, respuesta)
    labelRespuesta = Label(root, text=respuesta, bg="yellow")
    labelRespuesta.place(x=10, y=150, width=100, height=30)

root = Tk()
root.title("Ejemplo de Suma con posicion Place")
root.geometry("400x200")

label1 = Label(root, text="Primer numero", bg="green")
label1.place(x=10,y=10, width=100, height=30)

entrada1 = Entry(root, bg="pink")
entrada1.place(x=120, y=10, width=100, height=30)

#TODO: Etiqueta y entrada del número 2


label2 = Label(root, text="Segundo numero", bg="blue")
label2.place(x=10,y=50, width=100, height=30)

entrada2 = Entry(root, bg="pink")
entrada2.place(x=120, y=50, width=100, height=30)

label3 = Label(root, text="Resultado", bg="yellow")
label3.place(x=10,y=120, width=100, height=30)

entrada3 = Entry(root, bg="yellow")
entrada3.place(x=120, y=120, width=100, height=30)

btn = Button(root, text="Sumar", command=suma)

btn.place(x=10, y=85, width=100, height=30)

root.mainloop()