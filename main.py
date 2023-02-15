from tkinter import *

janela = Tk()
janela.title('Ola mundo')
janela.geometry('600x250')
janela.config(bg='#03a5fc')

janela.resizable(width=False, height=False)

nome = Label(janela, width=10, height=2, text='Ola')
nome.grid(row=0, column=0)

janela.mainloop()
