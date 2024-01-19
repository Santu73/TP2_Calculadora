import tkinter as tk
from tkinter import ttk
import math

ventana = tk.Tk()
ventana.geometry("428x500")
ventana.title("Calculadora")


calculadora = tk.Frame(ventana)
calculadora.grid()

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
    if operador == "+" or operador == "-" or operador == "*" or operador == "/" or operador == "^" or operador == "√" or operador == "=" or operador == "±" or operador == "⅟ⅹ" or operador == "%":
        historial.set(historial.get() + operador)
    historial.set(historial.get() + digit)

def calcular(op):
    global rp, operador, primer_numero
    current = float(value.get())
    if operador:
        try:
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
            elif operador == "√":
                num = current
                if num < 0:
                    raise ValueError
                else:
                    aprox = num/2.0
                    mejor_aprox = (aprox + num/aprox)/2.0
                    while mejor_aprox != aprox:
                        aprox = mejor_aprox
                        mejor_aprox = (aprox + num/aprox)/2.0
                    rp = aprox
            elif operador == "±":
                rp = current * -1
            elif operador == "⅟ⅹ":
                if num == 0:
                    raise ZeroDivisionError
                rp = 1 / current
            elif operador == "%":
                rp = current / 100
            elif operador == chr(9003):
                rp = current[:-1]
        except (ValueError, ZeroDivisionError):
            value.set("Error")
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

botones = []
for i in range(10):
    boton = ttk.Button(ventana, text=str(i), style='RoundedButton.TButton', command=lambda x=i: actualizar(str(x)))
    botones.append(boton)

botones[0].grid(row=7, column=1, sticky="nsew")
botones[1].grid(row=6, column=0, sticky="nsew")
botones[2].grid(row=6, column=1, sticky="nsew")
botones[3].grid(row=6, column=2, sticky="nsew")
botones[4].grid(row=5, column=0, sticky="nsew")
botones[5].grid(row=5, column=1, sticky="nsew")
botones[6].grid(row=5, column=2, sticky="nsew")
botones[7].grid(row=4, column=0, sticky="nsew")
botones[8].grid(row=4, column=1, sticky="nsew")
botones[9].grid(row=4, column=2, sticky="nsew")

botones_estandar = []
boton_mas = tk.Button(ventana, text="+", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("+"))
botones_estandar.append(boton_mas)
boton_menos = tk.Button(ventana, text="–", width=8, height=1,borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("-"))
botones_estandar.append(boton_menos)
boton_mult = tk.Button(ventana, text="×", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("*"))
botones_estandar.append(boton_mult)
boton_div = tk.Button(ventana, text="÷", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 17), command=lambda: calcular("/"))
botones_estandar.append(boton_div)
boton_mas_menos = tk.Button(ventana, text="±", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("±"))
botones_estandar.append(boton_mas_menos)
boton_coma = tk.Button(ventana, text=",", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(value.get() + "."))
botones_estandar.append(boton_coma)
boton_raiz = tk.Button(ventana, text="√", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("√"))
botones_estandar.append(boton_raiz)
boton_potencia = tk.Button(ventana, text="^", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("^"))
botones_estandar.append(boton_potencia)
boton_algo = tk.Button(ventana, text="⅟ⅹ", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("⅟ⅹ"))
botones_estandar.append(boton_algo)
boton_borrar = tk.Button(ventana, text=chr(9003), width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular(chr(9003)))
botones_estandar.append(boton_borrar)
boton_limpia = tk.Button(ventana, text="C", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 15), command=limpiar)
botones_estandar.append(boton_limpia)
boton_porcent = tk.Button(ventana, text="%", width=8, height=1, borderwidth=0, relief="flat", bg='#ecebfc', fg='#2b1057', font=("cambria", 16), command=lambda: calcular("%"))
botones_estandar.append(boton_porcent)
boton_igual = tk.Button(ventana, text="=", width=8, height=1, borderwidth=3, relief="ridge", bg='#d6d4ff', fg='#2b1057', font=("cambria", 16, "bold"), command=lambda: calcular("="))
botones_estandar.append(boton_igual)

botones_estandar[0].grid(row=6, column=3, sticky="nsew") # mas
botones_estandar[1].grid(row=5, column=3, sticky="nsew") # menos
botones_estandar[2].grid(row=4, column=3, sticky="nsew") # mult
botones_estandar[3].grid(row=3, column=3, sticky="nsew") # div
botones_estandar[4].grid(row=2, column=0, sticky="nsew") # mas menos
botones_estandar[5].grid(row=7, column=0, sticky="nsew") # coma
botones_estandar[6].grid(row=3, column=2, sticky="nsew") # raiz
botones_estandar[7].grid(row=3, column=1, sticky="nsew") # pot
botones_estandar[8].grid(row=3, column=0, sticky="nsew") # algo
botones_estandar[9].grid(row=2, column=3, sticky="nsew") # borrar
botones_estandar[10].grid(row=2, column=2, sticky="nsew") # limpia
botones_estandar[11].grid(row=2, column=1, sticky="nsew") # porcent
botones_estandar[12].grid(row=7, column=2, sticky="nsew", columnspan=2) # igual


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


def estandar():
    ventana.geometry("428x500")
    for boton in botones_cientifica:
        boton.grid_forget()
    for boton in botones_estandar:
        boton.grid(row=boton.grid_info()['row'], column=boton.grid_info()['column'], sticky="nsew")

botones_cientifica = []
def cientifica():
    boton_pi = tk.Button(ventana, text="π", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.pi)))
    botones_cientifica.append(boton_pi)
    boton_log = tk.Button(ventana, text="log", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.log10(float(value.get())))))
    botones_cientifica.append(boton_log)
    boton_ln = tk.Button(ventana, text="ln", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.log(float(value.get())))))
    botones_cientifica.append(boton_ln)
    boton_sin = tk.Button(ventana, text="sin", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.sin(math.radians(float(value.get()))))))
    botones_cientifica.append(boton_sin)
    boton_cos = tk.Button(ventana, text="cos", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.cos(math.radians(float(value.get()))))))
    botones_cientifica.append(boton_cos)
    boton_tan = tk.Button(ventana, text="tan", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.tan(math.radians(float(value.get()))))))
    botones_cientifica.append(boton_tan)

    boton_e = tk.Button(ventana, text="e", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.e)))
    botones_cientifica.append(boton_e)
    boton_exp = tk.Button(ventana, text="exp", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.exp(float(value.get())))))
    botones_cientifica.append(boton_exp)
    boton_asin = tk.Button(ventana, text="asin", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.degrees(math.asin(float(value.get()))))))
    botones_cientifica.append(boton_asin)
    boton_acos = tk.Button(ventana, text="acos", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.degrees(math.acos(float(value.get()))))))
    botones_cientifica.append(boton_acos)
    boton_atan = tk.Button(ventana, text="atan", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.degrees(math.atan(float(value.get()))))))
    botones_cientifica.append(boton_atan)
    boton_sinh = tk.Button(ventana, text="sinh", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.sinh(float(value.get())))))
    botones_cientifica.append(boton_sinh)
    boton_cosh = tk.Button(ventana, text="cosh", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.cosh(float(value.get())))))
    botones_cientifica.append(boton_cosh)
    boton_tanh = tk.Button(ventana, text="tanh", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.tanh(float(value.get())))))
    botones_cientifica.append(boton_tanh)
    boton_fact = tk.Button(ventana, text="fact", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.factorial(int(value.get())))))
    botones_cientifica.append(boton_fact)
    boton_log_extra = tk.Button(ventana, text="log(x+1)", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.log1p(float(value.get())))))
    botones_cientifica.append(boton_log_extra)
    boton_raiz_cub = tk.Button(ventana, text="∛x", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.cbrt(float(value.get())))))
    botones_cientifica.append(boton_raiz_cub)
    boton_pow_raro = tk.Button(ventana, text="10^x", width=8, height=1, borderwidth=0, relief="flat", bg='#b5aabf', fg='#2b1057', font=("cambria", 16), command=lambda: value.set(str(math.pow(10,float(value.get())))))
    botones_cientifica.append(boton_pow_raro)
    
    botones_cientifica[0].grid(row=7, column=4, sticky="nsew") # pi  --
    botones_cientifica[1].grid(row=5, column=4, sticky="nsew") # log --
    botones_cientifica[2].grid(row=5, column=5, sticky="nsew") # ln --
    botones_cientifica[3].grid(row=2, column=4, sticky="nsew") # sin --
    botones_cientifica[4].grid(row=2, column=5, sticky="nsew") # cos -- 
    botones_cientifica[5].grid(row=2, column=6, sticky="nsew") # tan --

    botones_cientifica[6].grid(row=6, column=5, sticky="nsew") # e --
    botones_cientifica[7].grid(row=6, column=4, sticky="nsew") # exp --
    botones_cientifica[8].grid(row=3, column=4, sticky="nsew") # asin --
    botones_cientifica[9].grid(row=3, column=5, sticky="nsew") # acos --
    botones_cientifica[10].grid(row=3, column=6, sticky="nsew") # atan --
    botones_cientifica[11].grid(row=4, column=4, sticky="nsew") # sinh --
    botones_cientifica[12].grid(row=4, column=5, sticky="nsew") # cosh --
    botones_cientifica[13].grid(row=4, column=6, sticky="nsew") # tanh --
    botones_cientifica[14].grid(row=7, column=6, sticky="nsew") # fact --
    botones_cientifica[15].grid(row=5, column=6, sticky="nsew") # log_extra --
    botones_cientifica[16].grid(row=7, column=5, sticky="nsew") # raiz_cub --
    botones_cientifica[17].grid(row=6, column=6, sticky="nsew") # pow_raro --
    
    
    ventana.columnconfigure(4, weight=1)
    ventana.columnconfigure(5, weight=1)
    ventana.columnconfigure(6, weight=1)

    ventana.geometry("944x568")
    for boton in botones_cientifica:
        boton.grid(row=boton.grid_info()['row'], column=boton.grid_info()['column'], sticky="nsew")


label_historial = tk.Label(ventana, textvariable=historial, font=("lucida console", 14), anchor="e")
label_historial.config(foreground="grey")



label = tk.Label(ventana, textvariable=value, font=("lucida console", 42, "bold"), anchor="e")


style = ttk.Style()
style.configure('RoundedButton.TButton', borderwidth=0, relief="flat", background="white",
                foreground="#2b1057", width=8, height=1, font=("cambria", 15, "bold"))

        
menu_bar = tk.Menu(calculadora)

opcion = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Modo",menu=opcion)
opcion.add_command(label="Estándar", command=estandar)
opcion.add_command(label="Científica", command=cientifica)
if opcion == estandar:
    label_historial.grid(row=0, column=0, columnspan=4, sticky="nsew")
    label.grid(row=1, column=1, columnspan=4, sticky="nsew")
else:
    label_historial.grid(row=0, column=0, columnspan=6, sticky="nsew")
    label.grid(row=1, column=1, columnspan=6, sticky="nsew")

ventana.config(menu=menu_bar)

ventana.mainloop()