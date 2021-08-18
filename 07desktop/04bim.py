from tkinter import *
from tkinter import messagebox


def calcular_bmi():
    #TODO: Formula bmi
    kg = int(peso_entry.get())
    m= int(altura_entry.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_status(bmi)

def bmi_status(bmi):
    resultado = ""
    if bmi > 30 :
        resultado = "Obesidad"
    elif bmi > 25:
        resultado = "Sobrepeso"
    elif bmi > 18.5:
        resultado = "Normal"
    elif bmi < 18.5:
        resultado = "Bajo de peso"
    messagebox.showinfo("Resultado", f"{bmi} es {resultado}")

def reset_entry():
    edad_entry.delete(0, "end")
    peso_entry.delete(0, "end")
    altura_entry.delete(0, "end")


ws = Tk()
ws.title("Calculadora BMI")
ws.geometry("400x300")
ws.config(bg="#2e4057")

frame = Frame(
    ws,
    padx=10,
    pady=10,
)

frame.pack(expand=True)

#input de edad
edad_lb = Label(frame, text="Ingresa edad:")
edad_lb.grid(row=1, column=1)
edad_entry = Entry(frame)
edad_entry.grid(row=1, column=2)

#input de Genero
gen_lb= Label(frame, text="Ingresa género")
gen_lb.grid(row=2, column=1)
gen_frame=Frame(frame)
gen_frame.grid(row=2, column=2)

var = IntVar()
hombre_rb = Radiobutton(gen_frame, text="Hombre", variable=var, value=1)
hombre_rb.pack(side=LEFT)
mujer_rb = Radiobutton(gen_frame, text="Mujer", variable=var, value=2)
mujer_rb.pack(side=RIGHT)

#input altura
altura_lb = Label(frame, text="Ingresa tu altura(cm):")
altura_lb.grid(row=3, column=1)
altura_entry = Entry(frame)
altura_entry.grid(row=3, column=2)

#input peso

peso_lb = Label(frame, text="Ingresa peso(kg):")
peso_lb.grid(row=4, column=1)
peso_entry = Entry(frame)
peso_entry.grid(row=4, column=2)

#Botones

btn_frame = Frame(frame)
btn_frame.grid(row=5, columnspan=3)

cal_btn = Button(btn_frame, text="Calcular", command=calcular_bmi)
reset_btn = Button(btn_frame, text="Reset", command=reset_entry)
salir_btn = Button(btn_frame, text="Salir", command=lambda: ws.destroy() )

cal_btn.pack(side=LEFT)
reset_btn.pack(side=LEFT)
salir_btn.pack(side=LEFT)

ws.mainloop()

#pyinstaller 07desktop/04bim.py --onefile