'''
Valentin Berman - 18/02/20

Programa para visualizar transformaciones en el plano complejo
'''

import cmath as m
import tkinter as tk
from tkinter.constants import *

#############
# Parametros
#############

# Tamaño de las gráficas
cWidth = 400
cHeight = 400

# Espacio debajo para controles
espacioDebajo = 120

# Tamaño de los títulos
tamnTitulo = 16



##########
# Clases
##########

class Grafico(tk.Canvas):
	'''
	Clase para crear los canvas sobre que hacen de entrada y salida
	'''

	def __init__(self, master, cursor='cross'):
		super().__init__(master,
			# Opciones
			cursor=cursor, 
			bg = 'grey', 
			width = cWidth, 
			height = cHeight)
		
		# Grafica los ejes
		self.create_line(cWidth//2,cHeight+10,cWidth//2,0,fill='black')
		self.create_line(0,cHeight//2,cWidth+10,cHeight//2, fill='black')


#############
# Funciones
#############

# Funciones matemáticas

def exponencial(z):
	return m.exp(z)/100

def logaritmo(z):
	try:
		return m.log(z)*5
	except ValueError:
		return m.nan

def lineal(z):
	# obtinen los valores de Alpha y Beta del 'spinbox'
	r=float(eAlphaR.get())
	theta=float(eAplhaTheta.get())
	alpha = r*m.exp(theta*1j)

	return alpha*z

def seno(z):
	return m.sin(z)* 5

# Funcion por defecto
funcActual = lineal

def cambFuncActual(nuevaFunc):
	'''Cambia la funcion actual'''
	global funcActual
	funcActual = nuevaFunc
	borrar()

# Lógica del programa
def coord2complex(x,y,cWidth=cWidth,cHeight=cHeight):
	'''
	Convierte coordenadas dadas por tkinter en un número complejo
	'''
	a = (x - cWidth//2)/10
	b = -(y - cHeight//2)/10

	return complex(a,b)


def complex2coord(z, cWidth=cWidth, cHeight=cHeight):
	'''
	Convierte un numero complejo en coordenadas que puede usar tkinter
	'''
	try:
		x = int(z.real*10 + cWidth//2)
		y = int(-z.imag*10 + cHeight//2)
	except OverflowError:				# En caso de que sea float('inf)
		x = cWidth + 100				# Manda el cursor fuera de la vista
		y = cHeight + 100
	except ValueError:					# En caso de que sea float('nan')
		x = cWidth + 100				# Manda el cursor fuera de la vista
		y = cHeight + 100


	return x, y

# Manejo de eventos de la gui
def dibujarEntrada(event):
	cEntrada.create_rectangle(event.x-1, event.y-1, event.x+1, event.y+1, outline='#55f', fill='#55f', tag='dibujo')

def dibujarSalida(event, funcion):
	z = coord2complex(event.x, event.y)
	w = funcion(z)
	x, y = complex2coord(w)

	cSalida.create_rectangle(x-1, y-1, x+1, y+1, outline='#f77', fill='#f77', tag='dibujo')
	cursorSalida(event, funcion)

def cursorSalida(event, funcion):
	cSalida.delete('x')

	z = coord2complex(event.x, event.y)
	w = funcion(z)
	x, y = complex2coord(w)

	cSalida.create_line(x-6, y-6, x+6, y+6, width=3, fill='black', tag='x')
	cSalida.create_line(x-6, y+6, x+6, y-6, width=3, fill='black', tag='x')

def dibujar(event, funcion):
	dibujarEntrada(event)
	dibujarSalida(event, funcion)

def borrar():
	cEntrada.delete('dibujo')
	cSalida.delete('x','dibujo')


#######
# GUI
#######

# Inicio

root = tk.Tk()

# Configura el tamaño de la ventana
winWidth = cWidth*2 + 10
winHeight = cHeight + espacioDebajo + tamnTitulo + 8 # 8 incluye el tamaño del espaciado del título
root.geometry('%dx%d' % (winWidth, winHeight))
root.resizable(False, False)

# Título
root.title("Visuaizador complejos")

# Entrada

# Titulo
lEntrada = tk.Label(text="Entrada", font=f"Default {tamnTitulo}", pady=4)
lEntrada.grid(row=0, column=0)

# Gráfico
cEntrada = Grafico(root)
cEntrada.grid(row=1, column=0, sticky = NW)

cEntrada.bind("<Motion>", lambda event: cursorSalida(event, funcActual))
cEntrada.bind("<B1-Motion>", lambda event: dibujar(event, funcActual))


# Salida

# Titulo
lSalida = tk.Label(text="Salida", font=f"Default {tamnTitulo}", pady=4)
lSalida.grid(row=0,column=1)

# Gráfico
cSalida = Grafico(root, cursor='X_cursor')
cSalida.grid(row=1, column=1, sticky = NE)


# Controles de abajo

# Contenedor
cont = tk.Frame(root)
cont.grid(row=2, column=0, columnspan=2, sticky=NSEW)

# Lineal

# Boton
bLineal = tk.Button(cont, text='Lineal', command= lambda: cambFuncActual(lineal))
bLineal.grid(row=0, column=0)

# Descripción
descLineal = tk.Label(cont, text="⍺z+β")
descLineal.grid(row=1, column=0)

# Alpha
contAlpha = tk.Frame(cont)
contAlpha.grid(row=2,column=0)

lAlpha1 = tk.Label(contAlpha, text="⍺ = ")
lAlpha1.pack(side=LEFT)

eAlphaR = tk.Spinbox(contAlpha, width = 3, from_=-100, to=100)
eAlphaR.pack(side=LEFT)

lAlpha2 = tk.Label(contAlpha, text=" *e^ ")
lAlpha2.pack(side=LEFT)

eAplhaTheta = tk.Spinbox(contAlpha, width = 3, from_=-100, to=100)
eAplhaTheta.pack(side=LEFT)

lAlpha3 = tk.Label(contAlpha, text="i")
lAlpha3.pack(side=LEFT)

# Beta
contBeta = tk.Frame(cont)
contBeta.grid(row=3, column=0)

lBeta = tk.Label(contBeta, text="β =")
lBeta.pack(side=LEFT)

# Botón exponencial
bExp = tk.Button(cont, text='Exp', command= lambda: cambFuncActual(exponencial))
bExp.grid(row=0, column=1)

# Botón logaritmo
bLog = tk.Button(cont, text='Log', command= lambda: cambFuncActual(logaritmo))
bLog.grid(row=0,column=2)

# Botón seno
bSeno = tk.Button(cont, text='Seno', command= lambda: cambFuncActual(seno))
bSeno.grid(row=0, column=3)

# Botón borrar
bBorrar = tk.Button(cont, text='Borrar', command=borrar)
bBorrar.grid(row=0, column = 5)




# Loop principal del programa
root.mainloop()
