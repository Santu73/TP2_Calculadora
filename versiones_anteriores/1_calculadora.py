import tkinter as tk
from tkinter import ttk
from math import *

ventana = tk.Tk()
ventana.geometry("320x470")
ventana.title("Calculadora")

"""menu = ttk.Combobox(
    state="readonly",
    values=["Estándar", "Científica"])
menu.place(x=0, y=0)"""

"""valor = tk.StringVar()
valor.set("0")"""

rp = 0
ecuacion = tk.StringVar()
ecuacion.set("0")

# Crear una función para actualizar el valor cuando se presiona un botón
def actualizar(digito):
   texto = ecuacion.get()
   if texto == "0":
        ecuacion=digito
        label.config(text=ecuacion)
   else:
        ecuacion+=digito
        label.config(text=ecuacion)

   """# Obtener el valor actual
   texto = valor.get()
   # Si es cero, reemplazarlo por el dígito
   if texto == "0":
      valor.set(digito)
   # Si no es cero, añadir el dígito al final
   else:
      valor.set(texto + digito)"""

# Crear una función para evaluar la expresión matemática o borrar el valor
def operar(op):
    global rp, ecuacion
    # Obtener el valor actual
    texto = ecuacion.get()
    try: 
        # Si la operación es igual, intentar evaluarla como una expresión matemática
        if op == "=":
            try:
                
                ecuacion.set(str(rp))
            # Si hay un error, mostrar un mensaje de error
            except:
                ecuacion.set("Error")
        
        # Si la operación es suma, sumar numero
        elif op == "+":
            rp += texto
        # Si la operación es resta, restar numero
        elif op == "-":
            rp -= texto
        # Si la operación es multipl, multiplicar numero
        elif op == "*":
            rp *= texto
        # Si la operación es division, dividir numero
        elif op == "/":
            rp /= texto

        # Si la operación es limpiar, borrar el valor
        elif op == "C":
            ecuacion = ""
            label.config(text=ecuacion)
        # Si la operación es borrar un carácter, eliminar el último dígito
        elif op == chr(9003):
            ecuacion.set(texto[:-1])
            label.config(text=ecuacion)

        # Si la operación es cambiar de signo, multiplicar por -1
        elif op == "+/-":
            rp = str(-1 * texto)
        # Si la operación es raíz cuadrada, calcularla usando la función sqrt
        elif op == "√x":
            rp = str(sqrt(texto))
        # Si la operación es inversa, calcularla usando la división 1/x
        elif op == "⅟ⅹ":
            rp = str(1 / texto)
        # Si la operación es porcentaje, calcularla usando la división x/100
        elif op == "%":
            rp = str(texto / 100)
        # Si la operación es potencia, añadir el símbolo ** al final
        elif op == "^":
            rp = texto + "^"
        # Si la operación es otra, añadirla al final del valor
        else:
            ecuacion.set(texto + op)
    except:
        # Si hay un error, mostrar un mensaje de error
        ecuacion.set("Error")
    

# Crear una etiqueta para mostrar el valor
label = tk.Label(ventana, textvariable=ecuacion, font=("lucida console", 42, "bold"), anchor="e")
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
boton_mas_menos = tk.Button(ventana, text="+/-", width=8, height=1,font=("cambria",16),command=lambda: operar("+/-"))
boton_coma = tk.Button(ventana, text=",", width=8, height=1,font=("cambria",16),command=lambda: actualizar(","))
boton_raiz = tk.Button(ventana, text="√x", width=8, height=1,font=("cambria",16),command=lambda: operar("√x"))
boton_potencia = tk.Button(ventana, text="x b", width=8, height=1,font=("cambria",16),command=lambda: operar("x b"))
boton_algo = tk.Button(ventana, text="⅟ⅹ", width=8, height=1,font=("cambria",16),command=lambda: operar("⅟ⅹ"))
boton_borra1 = tk.Button(ventana, text=chr(9003), width=8, height=1,font=("cambria",16),command=lambda:operar(chr(9003)))
boton_limpia = tk.Button(ventana, text="C", width=8, height=1,font=("cambria", 15),command=lambda: operar("C"))
boton_borra2 = tk.Button(ventana, text="CE", width=8, height=1,font=("cambria",16),command=lambda:operar(""))
boton_porcent = tk.Button(ventana, text="%", width=8, height=1,font=("cambria",16),command=lambda:operar("%"))
boton_igual = tk.Button(ventana, text="=", width=8, height=1, bg='#006bb3',fg='white',font=("cambria", 16, "bold"),command=lambda: operar("="))

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
boton_algo.grid(row=3, column=0, sticky="nsew")
boton_borra1.grid(row=2, column=3, sticky="nsew")
boton_limpia.grid(row=2, column=2, sticky="nsew")
boton_borra2.grid(row=2, column=1, sticky="nsew")
boton_porcent.grid(row=2, column=0, sticky="nsew")


# Ajustar el tamaño de la ventana según los botones
for i in range(8):
    ventana.rowconfigure(i, weight=1)
for i in range(4):
    ventana.columnconfigure(i, weight=1)

ventana.mainloop()
