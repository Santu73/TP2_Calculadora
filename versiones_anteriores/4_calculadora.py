import tkinter as tk
import math

ventana = tk.Tk()
ventana.geometry("320x470")
ventana.title("Calculadora")

result = ""
value = tk.StringVar()
value.set("0")

def actualizar(digit):
    current = value.get()
    if current == "0" or current == "Error":
        value.set(digit)
    else:
        value.set(current + digit)

def limpiar():
    value.set("0")

def calcular():
    global result
    current = value.get()
    try:
        
        if "√" in current:
            num = float(current[1:])
            if num < 0:
                raise ValueError
            result = math.sqrt(num)
        elif "^" in current:
            nums = current.split("^")
            base = float(nums[0])
            exponente = float(nums[1])
            result = pow(base, exponente)
        elif "⅟ⅹ" in current:
            num = float(current[:-2])
            if num == 0:
                raise ZeroDivisionError
            result = 1 / num
        elif "%" in current:
            nums = current.split("%")
            valor = float(nums[0])
            porcentaje = float(nums[1])
            result = (valor * porcentaje) / 100
        elif "/" in current:
            nums = current.split("/")
            numerador = float(nums[0])
            denominador = float(nums[1])
            if denominador == 0:
                raise ZeroDivisionError
            result = numerador / denominador
        elif "*" in current:
            nums = current.split("*")
            num1 = float(nums[0])
            num2 = float(nums[1])
            result = num1 * num2
        elif "-" in current:
            nums = current.split("-")
            num1 = float(nums[0])
            num2 = float(nums[1])
            result = num1 - num2
        elif "+" in current:
            nums = current.split("+")
            num1 = float(nums[0])
            num2 = float(nums[1])
            result = num1 + num2
        else:
            result = float(current)
        
        value.set(str(result))
        
    except (ValueError, ZeroDivisionError):
        value.set("Error")

def borrar():
    current = value.get()
    if current != "0" and current != "Error":
        updated = current[:-1]
        if len(updated) == 0:
            value.set("0")
        else:
            value.set(updated)

def agregar_coma():
    current = value.get()
    if "." not in current:
        value.set(current + ".")

def cambiar_signo():
    current = value.get()
    if current != "0" and current != "Error":
        if current[0] == "-":
            value.set(current[1:])
        else:
            value.set("-" + current)

label = tk.Label(ventana, textvariable=value, font=("lucida console", 42, "bold"), anchor="e")
label.grid(row=1, column=1, columnspan=4, sticky="nsew")

botones = []
for i in range(10):
    boton = tk.Button(ventana, text=str(i), width=8, height=1, bg='white',fg='black', font=("cambria", 15, "bold"), command=lambda x=i: actualizar(str(x)))
    botones.append(boton)

boton_mas_menos = tk.Button(ventana, text="±", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("-" if value.get() != "0" else ""))
boton_coma = tk.Button(ventana, text=",", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("."))
boton_igual = tk.Button(ventana, text="=", width=8, height=1, bg='#006bb3', fg='white', font=("cambria", 16, "bold"), command=calcular)
boton_mas = tk.Button(ventana, text="+", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("+"))
boton_menos = tk.Button(ventana, text="–", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("-"))
boton_mult = tk.Button(ventana, text="×", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("*"))
boton_div = tk.Button(ventana, text="÷", width=8, height=1, font=("cambria", 17), command=lambda: actualizar("/"))
boton_borrar = tk.Button(ventana, text=chr(9003), width=8, height=1, font=("cambria", 16), command=borrar)
boton_limpia = tk.Button(ventana, text="CE", width=8, height=1, font=("cambria", 16), command=limpiar)
boton_raiz = tk.Button(ventana, text="√x", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("√"))
boton_potencia = tk.Button(ventana, text="^", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("^"))
boton_algo = tk.Button(ventana, text="⅟ⅹ", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("⅟ⅹ"))
boton_porcent = tk.Button(ventana, text="%", width=8, height=1, font=("cambria", 16), command=lambda: actualizar("%"))

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
