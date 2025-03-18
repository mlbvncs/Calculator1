from tkinter import *
from tkinter import ttk

#cores
cor1 = "#171616" #preto
cor2 = "#adada8" #cinza
cor3 = "#112836" #azul
cor4 = "#e3e020" #amarelo

#janela
janela = Tk()
janela.title("CALCULADORA")
janela.geometry("258x278") #larguraxcomprimento
janela.config(bg=cor1)

#frames
frame_tela = Frame(janela, width=258, height=50, bg=cor3) #largura, comprimento e cor
frame_tela.grid(row=0, column=0) #linha, coluna

frame_corpo = Frame(janela, width=258, height=228, bg=cor1) #largura, comprimento e cor
frame_corpo.grid(row=1, column=0) #linha, coluna

#função
valores = ''
def entrada(valor):
    global valores  #variável global, para sempre que usar a função ela manter os valores adquiridos anteriormente
    valores = valores + str(valor)
    texto.set(valores) #passando valor pra tela

def saida():
    global valores #variável global, para sempre que usar a função ela manter os valores adquiridos anteriormente
    resultado = eval(valores) #exemplo: "5+5" vira 10, transfoma string em conta
    valores = str(resultado)
    texto.set(resultado) #passando valor pra tela

def limpar():
    global valores #variável global, para sempre que usar a função ela manter os valores adquiridos anteriormente
    valores = ""
    texto.set("")  #passando valor pra tela

#label
texto = StringVar() #transforma em string

label = Label(frame_tela, textvariable=texto, width=33, height=2, bg=cor2, padx=5, anchor="e", justify=RIGHT) #texto, largura, comprimento, cor, espaço dos números, resultado no canto da tela e tudo na direita
label.place(x=7, y=7)

#botões

botao_parenteses1 = Button(frame_corpo,  command=lambda: entrada('('), text="(", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_parenteses1.place(x=6, y=6) #horizontal, vertical
botao_parenteses2 = Button(frame_corpo, command=lambda: entrada(')'),  text=")", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_parenteses2.place(x=69, y=6) #horizontal, vertical
botao_percent = Button(frame_corpo, command=lambda: entrada('%'), text="%", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_percent.place(x=132, y=6) #horizontal, vertical
botao_div = Button(frame_corpo, command=lambda: entrada('/'),  text="/", width=7, height=2, bg=cor4) #função, texto, largura, comprimento, cor
botao_div.place(x=195, y=6) #horizontal, vertical

botao_7 = Button(frame_corpo,  command=lambda: entrada('7'), text="7", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_7.place(x=6, y=50) #horizontal, vertical
botao_8 = Button(frame_corpo, command=lambda: entrada('8'),  text="8", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_8.place(x=69, y=50) #horizontal, vertical
botao_9 = Button(frame_corpo, command=lambda: entrada('9'),  text="9", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_9.place(x=132, y=50) #horizontal, vertical
botao_x = Button(frame_corpo, command=lambda: entrada('*'),  text="*", width=7, height=2, bg=cor4) #função, texto, largura, comprimento, cor
botao_x.place(x=195, y=50) #horizontal, vertical

botao_4 = Button(frame_corpo, command=lambda: entrada('4'),  text="4", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_4.place(x=6, y=94) #horizontal, vertical
botao_5 = Button(frame_corpo, command=lambda: entrada('5'),  text="5", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_5.place(x=69, y=94) #horizontal, vertical
botao_6 = Button(frame_corpo, command=lambda: entrada('6'),  text="6", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_6.place(x=132, y=94) #horizontal, vertical
botao_sub = Button(frame_corpo, command=lambda: entrada('-'),  text="-", width=7, height=2, bg=cor4) #função, texto, largura, comprimento, cor
botao_sub.place(x=195, y=94) #horizontal, vertical

botao_1 = Button(frame_corpo, command=lambda: entrada('1'),  text="1", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_1.place(x=6, y=138) #horizontal, vertical
botao_2 = Button(frame_corpo, command=lambda: entrada('2'),  text="2", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_2.place(x=69, y=138) #horizontal, vertical
botao_3 = Button(frame_corpo, command=lambda: entrada('3'),  text="3", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_3.place(x=132, y=138) #horizontal, vertical
botao_soma= Button(frame_corpo, command=lambda: entrada('+'),  text="+", width=7, height=2, bg=cor4) #função, texto, largura, comprimento, cor
botao_soma.place(x=195, y=138) #horizontal, vertical

botao_0 = Button(frame_corpo, command=lambda: entrada('0'),  text="0", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, cor
botao_0.place(x=6, y=182) #horizontal, vertical
botao_AC = Button(frame_corpo,  command= limpar, text="AC", width=7, height=2, bg=cor2) #texto, largura, comprimento, cor
botao_AC.place(x=69, y=182) #horizontal, vertical
botao_ponto = Button(frame_corpo, command=lambda: entrada('.'),  text=".", width=7, height=2, bg=cor2) #função, texto, largura, comprimento, corr
botao_ponto.place(x=132, y=182) #horizontal, vertical
botao_igual = Button(frame_corpo, command=saida, text="=", width=7, height=2, bg=cor4) #função, texto, largura, comprimento, cor
botao_igual.place(x=195, y=182) #horizontal, vertical

#aplicação
janela.mainloop() #método que permite ver a janela