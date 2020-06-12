from tkinter import *
from tkinter import messagebox

#Criando a janela
window = Tk()
window.title("Login")

#Dimensoes da janela
largura = 500
altura = 300

#Resolução do nosso sistema
largura_screen = window.winfo_screenwidth()
altura_screen = window.winfo_screenheight()


#Posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2


window.geometry("500x300+%d+%d" % (posx, posy))

#Função para criação da segunda janela
def criaJanela2():
    window.destroy()
    window2 = Tk()
    window2.title("Cadastro de produtos")
    window2.geometry("500x300+%d+%d" % (posx, posy))

    #Criação de duas novas labels com seus respectivos botoes do lado
    lblwin2_1 = Label(window2, text="CADASTRAR CLIENTE", padx=50, pady=20, font="arial")
    lblwin2_1.grid(row=0, stick=W)

    lblwin2_2 = Label(window2, text="CONSULTAR CLIENTES:", padx=50, pady=20, font="arial")
    lblwin2_2.grid(row=1, stick=W)

    #Botoes
    btn_lblwin2_1 = Button(window2, text="Continuar")
    btn_lblwin2_1.grid(row=0, column=1)

    btn_lblwin2_2 = Button(window2, text="Continuar")
    btn_lblwin2_2.grid(row=1, column=1)


#Função para o botao login da primeira janela, apos logar, abre a 2 janela
def botao():
    valorSenha = passwordEntry.get()
    valorUser = userEntry.get().lower()
    if valorSenha == '1234' and valorUser == 'adm':
        messagebox.showinfo("INFO", "Voce esta logado")
        criaJanela2()
    else:
        messagebox.showerror("ERROR", "tente de novo")

#Labels da janela 1
lbl1 = Label(window, text="User:", anchor=N, padx=50, pady=20, font="arial 20")
lbl1.grid(row=0, stick=W)

lbl2 = Label(window, text="Password:", anchor=N, padx=50, pady=20, font="arial 20")
lbl2.grid(row=1, stick=W)

#Entrys da janela 1
userEntry = Entry(window, font="arial 16")
userEntry.grid(row=0, column=1)
userEntry.focus()

valorUsuario = userEntry.get()

passwordEntry = Entry(window, font="arial 16", show='*')
passwordEntry.grid(row=1, column=1)

#Botaõ da janela 1
bt1 = Button(window, text='Login', command=botao, font="arial 16")
bt1.grid(row=2, column=1, stick=E)



window.mainloop()