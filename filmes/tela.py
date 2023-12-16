from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# cores ---------------------
co0 = "#2e2d2b"  # Preto
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul

# Criando Janela
janela = Tk()
janela.title("")
janela.geometry('460x560')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames -----------------
frameCima = Frame(janela,width=450, height=50, bg=co0, relief="flat")
frameCima.grid(row=0, column=0)

framePergunta = Frame(janela, width=450, height=60, bg=co1, relief="solid")
framePergunta.grid(row=1, column=0, padx=5, sticky=NSEW)

frameMeio = Frame(janela, width=450, height=90, bg=co1, relief="solid")
frameMeio.grid(row=2, column=0, padx=5, sticky=NSEW)

frameBaixo = Frame(janela, width=300, height=460, bg=co1, relief="raised")
frameBaixo.grid(row=3, column=0, sticky=NSEW)

# Logo

#abrindo imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_nome = Label(frameCima, text='O chatbot de recomendacao de filmes', compound=LEFT, padx=5, relief=FLAT,
                 anchor=NW,font=('Verdana 15'), bg=co6, fg=co1)
app_nome.place(x=50, y=7)

# l_linha = Label(frameCima, width=450, height=1, anchor=NW,font=('Verdana 1'), bg=co3, fg=co1)
# l_linha.place(x=0, y=47)

# Pergunta ---------------------------------------

app_ = Label(framePergunta, text='Olá, como está se sentindo hoje ? ', width=45, height=2, wraplength=320,
             justify='center', compound=CENTER, padx=5, relief=FLAT, anchor=NW,font=('Verdana 11'), bg=co1, fg=co0)
app_.place(x=0, y=7)
l_linha = Label(framePergunta, width=450, height=1, anchor=NW,font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=57)

janela.mainloop()