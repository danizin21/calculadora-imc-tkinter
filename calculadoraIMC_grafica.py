#biblioteca do python para criar interfaces gráficas
import tkinter as tk
from tkinter import Frame,Entry, Label,Button

def calcula_imc():
    imc = float(peso.get()) / (float(altura.get()) ** 2)
    resultado['text'] = f"o seu IMC eh {imc:.2f}"
    
#cria a janela principal e funciona através da classe Tk
janela = tk.Tk()
#cria um frame dentro da janela principal, serve basicamente para encapsular outros widgets dentro dele
frame = Frame(janela,padx=40,pady=40)
frame.grid(column=1,row=1) 

Label(frame,text='para saber seu IMC,digite os valores abaixo:',pady=40,font=('Arial',13)).grid(column=1,row=1,columnspan=2) 
Label(frame,text = 'qual o seu peso em kg?',font=('Arial',13),anchor='w',width=30).grid(column=1,row=2)

peso = Entry(frame)
peso.grid(column=2,row=2)

Label(frame,text = 'qual a sua altura em metros?',font=('Arial',13),anchor='w',width=30).grid(column=1,row=3)
altura = Entry(frame)
altura.grid(column=2,row=3)

Button(frame,text='calcular IMC',command=calcula_imc).grid(column=2,row=4)
resultado = Label (frame,font=('Arial',12))
resultado.grid(column=1,row=5,columnspan=2)


janela.title("Calculadora de IMC")

janela.mainloop()
