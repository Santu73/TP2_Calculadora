import tkinter as tk
import math

ventana = tk.Tk()
ventana.geometry("320x470")
ventana.title("Calculadora")

value = tk.StringVar()
value.set("0")
rp = 0

def actualizar(digit):
    current = value.get()
    if current == "0" or current == "Error":
        value.set(digit)
    else:
        value.set(current + digit)
    label.config(text=value)

def calcular(op):
    global rp
    current = value.get()
    try:
        if "+" == op:
            rp += float(current)
        elif "-" == op:
            rp -= float(current)
        elif "*" == op:
            rp *= float(current)
        elif "/" == op:
            if current == 0:
                raise ZeroDivisionError
            rp /= float(current)
        elif "√" == op:
            num = float(current[1:])
            if num < 0:
                raise ValueError
            else:
                aprox = num/2.0
                mejor_aprox = (aprox + num/aprox)/2.0
                while mejor_aprox != aprox:
                    aprox = mejor_aprox
                    mejor_aprox = (aprox + num/aprox)/2.0
                rp = aprox
        elif "^" == op:
            nums = current.split("^")
            base = float(nums[0])
            exponente = float(nums[1])
            rp = base**exponente
        elif "⅟ⅹ" == op:
            num = float(current[:-2])
            if num == 0:
                raise ZeroDivisionError
            rp = 1 / num
        elif "%" == op:
            nums = current.split("%")
            valor = float(nums[0])
            porcentaje = float(nums[1])
            rp = (valor * porcentaje) / 100
        elif "+/-" == op:
            if current != "0" and current != "Error":
                if current[0] == "-":
                    value.set(current[1:])
                else:
                    value.set("-" + current)
        elif "," == op:
            value.set(current + ",")
        elif chr(9003) == op:
            if current != "0" and current != "Error":
                updated = current[:-1]
                if len(updated) == 0:
                    value.set("0")
                else:
                    value.set(updated)
        elif "C" == op:
            value.set("0")
        elif "=" == op:
            result = str(rp)
            label.config(text=result)
    
    except (ValueError, ZeroDivisionError):
        value.set("Error")


label = tk.Label(ventana, textvariable=value, font=("lucida console", 42, "bold"), anchor="e")
label.grid(row=1, column=1, columnspan=4, sticky="nsew")

botones = []
for i in range(10):
    boton = tk.Button(ventana, text=str(i), width=8, height=1, bg='white', fg='black', font=("cambria", 15, "bold"), command=lambda x=i: actualizar(str(x)))
    botones.append(boton)

boton_mas = tk.Button(ventana, text="+", width=8, height=1, font=("cambria", 16),command=lambda: calcular("+"))
boton_menos = tk.Button(ventana, text="–", width=8, height=1, font=("cambria", 16),command=lambda: calcular("-"))
boton_mult = tk.Button(ventana, text="×", width=8, height=1, font=("cambria", 16),command=lambda: calcular("*"))
boton_div = tk.Button(ventana, text="÷", width=8, height=1, font=("cambria", 17),command=lambda: calcular("/"))
boton_mas_menos = tk.Button(ventana, text="±", width=8, height=1,font=("cambria",16),command=lambda: calcular("+/-"))
boton_coma = tk.Button(ventana, text=",", width=8, height=1,font=("cambria",16),command=lambda: actualizar(","))
boton_raiz = tk.Button(ventana, text="√x", width=8, height=1,font=("cambria",16),command=lambda: calcular("√"))
boton_potencia = tk.Button(ventana, text="^", width=8, height=1,font=("cambria",16),command=lambda: calcular("^"))
boton_algo = tk.Button(ventana, text="⅟ⅹ", width=8, height=1,font=("cambria",16),command=lambda: calcular("⅟ⅹ"))
boton_borrar = tk.Button(ventana, text=chr(9003), width=8, height=1,font=("cambria",16),command=lambda:calcular(chr(9003)))
boton_limpia = tk.Button(ventana, text="C", width=8, height=1,font=("cambria", 15),command=lambda: calcular("C"))
boton_porcent = tk.Button(ventana, text="%", width=8, height=1,font=("cambria",16),command=lambda:calcular("%"))
boton_igual = tk.Button(ventana, text="=", width=8, height=1, bg='#006bb3',fg='white',font=("cambria", 16, "bold"),command=lambda: calcular("="))


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
