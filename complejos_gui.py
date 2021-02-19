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
espacioDebajo = 100

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
	x = int(z.real*10 + cWidth//2)
	y = int(-z.imag*10 + cHeight//2)

	return x, y

# Manejo de eventos de la gui
def dibujarEntrada(event):
	cEntrada.create_rectangle(event.x-1, event.y-1, event.x+1, event.y+1, outline='#55f', fill='#55f', tag='dibujo')

def dibujarSalida(event):
	z = coord2complex(event.x, event.y)
	w = m.exp(z)/100
	x, y = complex2coord(w)

	cSalida.create_rectangle(x-1, y-1, x+1, y+1, outline='#f77', fill='#f77', tag='dibujo')
	cursorSalida(event)

def cursorSalida(event):
	cSalida.delete('x')

	z = coord2complex(event.x, event.y)
	w = m.exp(z)/100
	x, y = complex2coord(w)

	cSalida.create_line(x-6, y-6, x+6, y+6, width=3, fill='black', tag='x')
	cSalida.create_line(x-6, y+6, x+6, y-6, width=3, fill='black', tag='x')

def dibujar(event):
	dibujarEntrada(event)
	dibujarSalida(event)

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

cEntrada.bind("<Motion>", cursorSalida)
cEntrada.bind("<B1-Motion>", dibujar)


# Salida

# Titulo
lSalida = tk.Label(text="Salida", font=f"Default {tamnTitulo}", pady=4)
lSalida.grid(row=0,column=1)

# Gráfico
cSalida = Grafico(root, cursor='X_cursor')
cSalida.grid(row=1, column=1, sticky = NE)


# Controles de abajo

# Contenedor
contenedorControles = tk.Frame(root)
contenedorControles.grid(row=2, column=0, columnspan=2, sticky=NSEW)

bBorrar = tk.Button(contenedorControles, text='Borrar', command=borrar)
bBorrar.grid(row=1, column = 5)




# Loop principal del programa
root.mainloop()
