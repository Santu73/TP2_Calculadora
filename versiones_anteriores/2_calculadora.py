
# Importar la librería tkinter
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("320x470")
ventana.title("Calculadora")

# Crear una variable para almacenar el valor actual
value = tk.StringVar()
value.set("0")

# Crear una función para actualizar el valor cuando se presiona un botón
def actualizar(digit):
    # Obtener el valor actual
    current = value.get()
    # Si es cero, reemplazarlo por el dígito
    if current == "0":
        value.set(digit)
    # Si no es cero, añadir el dígito al final
    else:
        value.set(current + digit)

# Crear una función para borrar el valor
def limpiar():
    value.set("0")

# Crear una función para evaluar la expresión matemática
def evaluar():
    # Obtener el valor actual
    current = value.get()
    # Intentar evaluarlo como una expresión matemática
    try:
        result = eval(current)
        value.set(str(result))
    # Si hay un error, mostrar un mensaje de error
    except:
        value.set("Error")

# Crear una etiqueta para mostrar el valor
label = tk.Label(ventana, textvariable=value, font=("lucida console", 42, "bold"), anchor="e")
label.grid(row=1, column=1, columnspan=4, sticky="nsew")

# Crear los botones numéricos
botones = []
for i in range(10):
    boton = tk.Button(ventana, text=str(i), width=8, height=1,font=("cambria", 15, "bold"), command=lambda x=i: actualizar(str(x)))
    botones.append(boton)


# Crear los botones de operaciones
boton_limpia = tk.Button(ventana, text="C", width=8, height=1,font=("cambria", 15),command=limpiar)
boton_igual = tk.Button(ventana, text="=", width=8, height=1, bg='#006bb3',fg='white',font=("cambria", 16, "bold"),command= evaluar)
boton_mas = tk.Button(ventana, text="+", width=8, height=1, font=("cambria", 16),command=lambda: actualizar("+"))
boton_menos = tk.Button(ventana, text="–", width=8, height=1, font=("cambria", 16),command=lambda: actualizar("-"))
boton_mult = tk.Button(ventana, text="×", width=8, height=1, font=("cambria", 16),command=lambda: actualizar("*"))
boton_div = tk.Button(ventana, text="÷", width=8, height=1, font=("cambria", 17),command=lambda: actualizar("/"))
boton_mas_menos = tk.Button(ventana, text="+/-", width=8, height=1,font=("cambria",16),command=lambda: actualizar(""))
boton_coma = tk.Button(ventana, text=",", width=8, height=1,font=("cambria",16),command=lambda: actualizar(","))
boton_raiz = tk.Button(ventana, text="√x", width=8, height=1,font=("cambria",16),command=lambda: actualizar(""))
boton_potencia = tk.Button(ventana, text="x b", width=8, height=1,font=("cambria",16),command=lambda: actualizar(""))
boton_algo = tk.Button(ventana, text="⅟ⅹ", width=8, height=1,font=("cambria",16),command=lambda: actualizar(""))
boton_borra1 = tk.Button(ventana, text="⊠", width=8, height=1,font=("cambria",16),command=lambda: actualizar(""))
boton_borra2 = tk.Button(ventana, text="CE", width=8, height=1,font=("cambria",16),command=lambda: actualizar(""))
boton_porcent = tk.Button(ventana, text="%", width=8, height=1,font=("cambria",16),command=lambda: actualizar(""))

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