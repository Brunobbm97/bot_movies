from tkinter.ttk import *
from tkinter import *
from tkinter import ttk

# cores ---------------------
co0 = "#2e2d2b"  # Preto
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 = "#6e8faf"  #
co11 = "#f2f4f2"

# Criando Janela
janela = Tk()
janela.title("")
janela.geometry('460x560')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames -----------------
frameCima = Frame(janela,width=450, height=50, bg=co6, relief="flat")
frameCima.grid(row=0, column=0)

frameAsk = Frame(janela, width=450, height=60, bg=co1, relief="solid")
frameAsk.grid(row=1, column=0, padx=5, sticky=NSEW)

frameMeio = Frame(janela, width=450, height=90, bg=co1, relief="solid")
frameMeio.grid(row=2, column=0, padx=5, sticky=NSEW)

frameBaixo = Frame(janela, width=300, height=460, bg=co1, relief="raised")
frameBaixo.grid(row=3, column=0, sticky=NSEW)

janela.mainloop()