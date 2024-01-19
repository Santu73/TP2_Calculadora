import tkinter as tk
from tkinter import ttk
from math import *

ventana = tk.Tk()
ventana.geometry("320x470")
ventana.title("Calculadora")

ecuacion = "0"
rp = 0
def actualizar(digito):
   global ecuacion
   texto = ecuacion
   if texto == "0":
        ecuacion=digito
        label.config(text=ecuacion)
   else:
        ecuacion+=digito
        label.config(text=ecuacion)


def operar(op):
    global ecuacion, rp
    texto = ecuacion
    
    if op == "=":
        try:
            # Usar la función eval para calcular el resultado de la ecuación, QUÉ ESTOO? CAMBIAR SANTINAA!!
            
            result = str(rp)
            label.config(text=result)
        except:
            ecuacion = "Error"
            label.config(text=ecuacion)
    
  
    elif op == "C":
        ecuacion = "0"
        label.config(text=ecuacion)

    elif op == chr(9003):
        if len(texto) > 1:
            ecuacion = texto[:-1]
            label.config(text=ecuacion)
        else:
            ecuacion = "0"
            label.config(text=ecuacion)

    elif op == "+/-":
        try:
            num = float(texto)
            num *= -1
            ecuacion = str(num)
            label.config(text=ecuacion)
        except:
            pass

    elif op == "√x":
        try:
            num = float(texto)
            if num >= 0:
                ecuacion += ")"
                ecuacion = "sqrt(" + ecuacion
                label.config(text=ecuacion)
        except:
            pass

    elif op == "⅟ⅹ":
        try:
            num = float(texto)
            if num != 0:
                ecuacion += ")"
                ecuacion = "(1/" + ecuacion + ")"
                label.config(text=ecuacion)
        except:
            pass

    elif op == "%":
        try:
            num = float(texto)
            ecuacion += ")"
            ecuacion = "(" + ecuacion + "/100)"
            label.config(text=ecuacion)
        except:
            pass

    elif op == "^":
        try:
            num = float(texto)
            ecuacion += "**"
            label.config(text=ecuacion)
        except:
            pass

    elif op == "+":
        try:
            ecuacion.set()
            rp = rp + int(ecuacion.text)
            label.config(text=ecuacion)
        except:
            pass
    elif op == "-":
        try:
            num = float(texto)
            ecuacion += "-"
            label.config(text=ecuacion)
        except:
            pass
    elif op == "*":
        try:
            num = float(texto)
            ecuacion += "*"
            label.config(text=ecuacion)
        except:
            pass
    elif op == "/":
        try:
            num = float(texto)
            ecuacion += "/"
            label.config(text=ecuacion)
        except:
            pass

    else:
        try:
            num = float(texto)
            ecuacion += op
            label.config(text=ecuacion)
        except:
            pass

# Crear una etiqueta para mostrar el valor
label = tk.Label(ventana, text=ecuacion, font=("lucida console", 42, "bold"), anchor="e")
label.grid(row=1, column=1, columnspan=4, sticky="nsew")

# Crear los botones numéricos
botones = []
for i in range(10):
    boton = tk.Button(ventana, text=str(i), width=8, height=1, bg='white',fg='black',font=("cambria", 15, "bold"), command=lambda x=i: actualizar(str(x)))
    botones.append(boton)

# Crear los botones de operaciones
boton_mas = tk.Button(ventana, text="+", width=8, height=1, font=("cambria", 16),command=lambda: operar("+"))
boton_menos = tk.Button(ventana, text="–", width=8, height=1, font=("cambria", 16),command=lambda: operar("-"))
boton_mult = tk.Button(ventana, text="×", width=8, height=1, font=("cambria", 16),command=lambda: operar("*"))
boton_div = tk.Button(ventana, text="÷", width=8, height=1, font=("cambria", 17),command=lambda: operar("/"))
boton_mas_menos = tk.Button(ventana, text="+/-", width=8, height=1, font=("cambria", 16),command=lambda: operar("+/-"))
boton_coma = tk.Button(ventana, text=",", width=8, height=1,font=("cambria",16),command=lambda: actualizar(","))
boton_igual = tk.Button(ventana, text="=", width=8, height=1, bg='#006bb3',fg='white',font=("cambria", 16, "bold"),command=lambda: operar("="))
boton_borrar = tk.Button(ventana, text="C", width=8, height=1, font=("cambria", 16),command=lambda: operar("C"))
boton_borrar_uno = tk.Button(ventana, text=chr(9003), width=8, height=1, font=("cambria", 16),command=lambda: operar(chr(9003)))
boton_borra2 = tk.Button(ventana, text="CE", width=8, height=1,font=("cambria",16),command=lambda:operar(""))
boton_raiz = tk.Button(ventana, text="√x", width=8, height=1, font=("cambria", 16),command=lambda: operar("√x"))
boton_inversa = tk.Button(ventana, text="⅟ⅹ", width=8, height=1, font=("cambria", 16),command=lambda: operar("⅟ⅹ"))
boton_porcentaje = tk.Button(ventana, text="%", width=8, height=1, font=("cambria", 16),command=lambda: operar("%"))
boton_potencia = tk.Button(ventana, text="^", width=8, height=1, font=("cambria", 16),command=lambda: operar("^"))

# Colocar los botones en la ventana
botones[1].grid(row=6, column=0, sticky="nsew")
botones[2].grid(row=6, column=1, sticky="nsew")
botones[3].grid(row=6, column=2, sticky="nsew")
botones[4].grid(row=5, column=0, sticky="nsew")
botones[5].grid(row=5, column=1, sticky="nsew")
botones[6].grid(row=5, column=2, sticky="nsew")
botones[7].grid(row=4, column=0, sticky="nsew")
botones[8].grid(row=4, column=1, sticky="nsew")
botones[9].grid(row=4, column=2, sticky="nsew")
botones[0].grid(row=7, column=1, sticky="nsew")

boton_mas_menos.grid(row=7, column=0, sticky="nsew")
boton_coma.grid(row=7, column=2, sticky="nsew")
boton_igual.grid(row=7, column=3, sticky="nsew")
boton_mas.grid(row=6, column=3, sticky="nsew")
boton_menos.grid(row=5, column=3, sticky="nsew")
boton_mult.grid(row=4, column=3, sticky="nsew")
boton_div.grid(row=3, column=3, sticky="nsew")
boton_raiz.grid(row=3, column=2, sticky="nsew")
boton_potencia.grid(row=3, column=1, sticky="nsew")
boton_inversa.grid(row=3, column=0, sticky="nsew")
boton_borrar_uno.grid(row=2, column=3, sticky="nsew")
boton_borrar.grid(row=2, column=2, sticky="nsew")
boton_borra2.grid(row=2, column=1, sticky="nsew")
boton_porcentaje.grid(row=2, column=0, sticky="nsew")


# Ajustar el tamaño de la ventana según los botones
for i in range(8):
    ventana.rowconfigure(i, weight=1)
for i in range(4):
    ventana.columnconfigure(i, weight=1)

ventana.mainloop()