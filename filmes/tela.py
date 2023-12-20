from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from datetime import datetime

#importanto a funcao principal
from main import *

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


# Fruncao resoltado
def resultado(i):
    global capa_1, capa_2, capa_3

    # filmes sugeridos
    sugeridos = suggest_movies(i)

    titles = sugeridos[0]
    poster = sugeridos[1]
    data = sugeridos[2]
    votos = sugeridos[3]

    # Limpando o frame baixo
    for widget in frameBaixo.winfo_children():
        widget.destroy()

    # ---------- Criando Frame para cada filme---------
    # filme 1
    frame_1 = Frame(frameBaixo, width=150, height=400, bg=co1)
    frame_1.grid(row=0, column=0, sticky=NSEW, pady=5)

    # nome
    nome = Label(frame_1, text=f'{titles[0]}',height=2, padx=10,pady=5, wraplength=100, justify='left',
                 relief=SOLID, anchor=NW, font=('Ivy 9 bold'), bg=co1, fg=co0, bd=1, highlightbackground='white')
    nome.place(x=7, y=260)

    # Data
    data_string_1 = f'{data[0]}'
    data_1 = datetime.strptime(data_string_1, '%Y-%m-%d')
    data_formatada = data_1.strftime('%B %Y')

    l_data_1 = Label(frame_1, text=f'Lançamento: {data_formatada}',
                     anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_data_1.place(x=5, y=310)

    # Voto
    l_voto_1 = Label(frame_1, text=f'Media de votos: {votos[0]/10}',
                     anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_voto_1.place(x=5, y=330)






# Frame Meio --------------------------------

# configurando botoes

img_1 = Image.open('image/happy.png')
img_1 = img_1.resize((28,28))
img_1 = ImageTk.PhotoImage(img_1)

b_1 = Button(frameMeio,command=lambda:resultado('well'), image=img_1, compound=LEFT, width=100, text=' OK ', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)

img_2 = Image.open('image/angry.png')
img_2 = img_2.resize((28,28))
img_2 = ImageTk.PhotoImage(img_2)

b_1 = Button(frameMeio,command=lambda:resultado('Anger'), image=img_2, compound=LEFT, width=100, text=' Anger ', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)

img_3 = Image.open('image/happy.png')
img_3 = img_3.resize((28,28))
img_3 = ImageTk.PhotoImage(img_3)

b_1 = Button(frameMeio,command=lambda:resultado('happy'), image=img_3, compound=LEFT, width=100, text=' Happy ', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)

img_4 = Image.open('image/angry.png')
img_4 = img_4.resize((28,28))
img_4 = ImageTk.PhotoImage(img_4)

b_1 = Button(frameMeio,command=lambda:resultado('gratitude'), image=img_4, compound=LEFT, width=100, text='Gratidao', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=0, column=3, sticky=NSEW, pady=2, padx=2)

img_5 = Image.open('image/happy.png')
img_5 = img_5.resize((28,28))
img_5 = ImageTk.PhotoImage(img_5)

b_1 = Button(frameMeio,command=lambda:resultado('frustration'), image=img_5, compound=LEFT, width=100, text='Frustracao', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)

img_6 = Image.open('image/angry.png')
img_6 = img_6.resize((28,28))
img_6 = ImageTk.PhotoImage(img_6)

b_1 = Button(frameMeio,command=lambda:resultado('ansiedade'), image=img_6, compound=LEFT, width=100, text=' Ansiedade ', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2)

img_7 = Image.open('image/happy.png')
img_7 = img_7.resize((28,28))
img_7 = ImageTk.PhotoImage(img_7)

b_1 = Button(frameMeio,command=lambda:resultado('prazer'), image=img_7, compound=LEFT, width=100, text=' Prazer ', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=1, column=2, sticky=NSEW, pady=2, padx=2)

img_8 = Image.open('image/angry.png')
img_8 = img_8.resize((28,28))
img_8 = ImageTk.PhotoImage(img_8)

b_1 = Button(frameMeio,command=lambda:resultado('horror'), image=img_8, compound=LEFT, width=100, text=' Horror ', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=1, column=3, sticky=NSEW, pady=2, padx=2)






janela.mainloop()


















