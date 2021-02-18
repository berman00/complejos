'''
Valentin Berman - 18/02/20

Programa para visualizar transformaciones en el plano complejo
'''

from tkinter import *

root = Tk()
winWidth = 800
winHeight = 400
root.geometry('%dx%d' % (winWidth, winHeight))
root.resizable(False, False)

cWidth = winWidth//2-5
cHeight = winHeight-30

# Funciones

def igual(event):
	cSalida.delete('x')
	cSalida.create_line(event.x-6, event.y-6, event.x+6, event.y+6, width=3, fill='black', tag='x')
	cSalida.create_line(event.x-6, event.y+6, event.x+6, event.y-6, width=3, fill='black', tag='x')

def dibujar(event):
	cSalida.create_rectangle(event.x-1, event.y-1, event.x+1, event.y+1, outline='#f77', fill='#f77', tag='dibujo')
	cEntrada.create_rectangle(event.x-1, event.y-1, event.x+1, event.y+1, outline='#55f', fill='#55f', tag='dibujo')
	igual(event)

def borrar(event):
	cEntrada.delete('dibujo')
	cSalida.delete('x','dibujo')

# Entrada
lEntrada = Label(text="Entrada", font="Default 16")
lEntrada.grid(row=0, column=0)
cEntrada = Canvas(root, bg = 'grey', width = cWidth, height = cHeight, cursor='cross')
cEntrada.grid(row=1, column=0, sticky = NW)

	# Creo la grilla
cEntrada.create_line(cWidth//2,cHeight+10,cWidth//2,0,fill='black')
cEntrada.create_line(0,cHeight//2,cWidth+10,cHeight//2, fill='black')

cEntrada.bind("<Motion>", igual)
cEntrada.bind("<B1-Motion>", dibujar)

# Salida
lSalida = Label(text="Salida", font="Default 16")
lSalida.grid(row=0,column=1)

cSalida = Canvas(root, bg = 'grey', width = cWidth, height = cHeight, cursor='X_cursor')
cSalida.grid(row=1, column=1, sticky = NE)

	# Creo grilla
cSalida.create_line(cWidth//2,cHeight+10,cWidth//2,0,fill='black')
cSalida.create_line(0,cHeight//2,cWidth+10,cHeight//2, fill='black')

cSalida.bind("<Double-Button-1>", borrar)

root.mainloop()