import tkinter as tk
from tkinter import ttk
import math

ventana = tk.Tk()
ventana.geometry("320x470")
ventana.title("Calculadora")

historial = tk.StringVar()
historial.set("")

value = tk.StringVar()
value.set("0")

rp = 0
operador = None
primer_numero = True

def actualizar(digit):
    global primer_numero, operador
    if value.get() == "0" or value.get() == "Error" or primer_numero:
        value.set(digit)
        primer_numero = False
    else:
        value.set(value.get() + digit)
    label.config(text=value)

    # Sustituir operadores con símbolos en el historial
    if operador == "+" or operador == "-" or operador == "*" or operador == "/" or operador == "^" or operador == "√" or operador == "=":
        historial.set(historial.get() + operador)
    historial.set(historial.get() + digit)

def calcular(op):
    global rp, operador, primer_numero
    current = float(value.get())
    if operador:
        if operador == "+" :
            rp += current
        elif operador == "-":
            rp -= current
        elif operador == "*":
            rp *= current
        elif operador == "/":
            try:
                rp /= current
            except ZeroDivisionError:
                value.set("Error")
                return
        elif operador == "^":
            rp **= current
    else:
        rp = current
    operador = op
    primer_numero = True

    if op == "=":
        value.set(str(rp))

def limpiar():
    global rp, operador, primer_numero
    value.set("0")
    historial.set("")
    rp = 0
    operador = None
    primer_numero = True


label_historial = tk.Label(ventana, textvariable=historial, font=("lucida console", 14), anchor="e")
label_historial.config(foreground="grey")
label_historial.grid(row=0, column=0, columnspan=4, sticky="nsew")

label = tk.Label(ventana, textvariable=value, font=("lucida console", 42, "bold"), anchor="e")
label.grid(row=1, column=1, columnspan=4, sticky="nsew")

style = ttk.Style()
style.configure('RoundedButton.TButton', borderwidth=0, relief="flat", background="white",
                foreground="#2b1057", width=8, height=1, font=("cambria", 15, "bold"))

botones = []
for i in range(10):
    boton = ttk.Button(ventana, text=str(i), style='RoundedButton.TButton', command=lambda x=i: actualizar(str(x)))
    botones.append(boton)

boton_mas = tk.Button(ventana, text="+", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("+"))
boton_menos = tk.Button(ventana, text="–", width=8, height=1,borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("-"))
boton_mult = tk.Button(ventana, text="×", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("*"))
boton_div = tk.Button(ventana, text="÷", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 17), command=lambda: calcular("/"))
boton_mas_menos = tk.Button(ventana, text="±", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(float(value.get()) * -1)))
boton_coma = tk.Button(ventana, text=",", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(value.get() + "."))
boton_raiz = tk.Button(ventana, text="√", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.sqrt(float(value.get())))))
boton_potencia = tk.Button(ventana, text="^", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("^"))
boton_algo = tk.Button(ventana, text="⅟ⅹ", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(1 / float(value.get()))))
boton_borrar = tk.Button(ventana, text=chr(9003), width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(value.get()[:-1]))
boton_limpia = tk.Button(ventana, text="C", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 15), command=limpiar)
boton_porcent = tk.Button(ventana, text="%", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(float(value.get()) / 100)))
boton_igual = tk.Button(ventana, text="=", width=8, height=1, borderwidth=3, relief="ridge", bg='#d6d4ff', fg='#2b1057', font=("cambria", 16, "bold"), command=lambda: calcular("="))

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

boton_mas_menos.grid(row=2, column=0, sticky="nsew")
boton_coma.grid(row=7, column=0, sticky="nsew")
boton_igual.grid(row=7, column=2, sticky="nsew", columnspan=2)
boton_mas.grid(row=6, column=3, sticky="nsew")
boton_menos.grid(row=5, column=3, sticky="nsew")
boton_mult.grid(row=4, column=3, sticky="nsew")
boton_div.grid(row=3, column=3, sticky="nsew")
boton_raiz.grid(row=3, column=2, sticky="nsew")
boton_potencia.grid(row=3, column=1, sticky="nsew")
boton_algo.grid(row=3, column=0, sticky="nsew")
boton_borrar.grid(row=2, column=3, sticky="nsew")
boton_limpia.grid(row=2, column=2, sticky="nsew")
boton_porcent.grid(row=2, column=1, sticky="nsew")

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)
ventana.rowconfigure(7, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

ventana.mainloop()
