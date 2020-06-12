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
    window2.title("Tela de Opções")
    window2.geometry("500x300+%d+%d" % (posx, posy))

    #Criação de duas novas labels com seus respectivos botoes do lado
    lblwin2_1 = Label(window2, text="CADASTRAR CLIENTE", padx=50, pady=20, font="arial")
    lblwin2_1.grid(row=0, stick=W)

    lblwin2_2 = Label(window2, text="CONSULTAR CLIENTES:", padx=50, pady=20, font="arial")
    lblwin2_2.grid(row=1, stick=W)

    #Comando cadastrar cliente
    def cadastrar():
        messagebox.showinfo('OK', 'Vamos começar!!')

        #Criação de uma janela paralela
        window3 = Tk()
        window3.title("Cadastro de pessoas")
        window3.geometry("500x300+%d+%d" % (posx, posy))

        #Nome e entry
        lbtop1 = Label(window3, text='NOME')
        lbtop1.place(x=10, y=10)
        lbtop1_entry = Entry(window3)
        lbtop1_entry.place(x=60, y=10)

        #CPF e entry
        lbtop2 = Label(window3, text='CPF')
        lbtop2.place(x=10, y=40)
        lbtop2_entry = Entry(window3)
        lbtop2_entry.place(x=60, y=40)

        #Variavel utilizada para guardar o sexo
        valor_a = IntVar()

        #Funções para o sexo
        def masculino():
            valor_a.set(1)

        def feminino():
            valor_a.set(2)

        #Sexo e opções do sexo
        lbtop3 = Label(window3, text="SEXO")
        lbtop3.place(x=200, y=10)

        ra_1 = Radiobutton(window3, text='MASCULINO', variable=valor_a, value=1, command=masculino)
        ra_2 = Radiobutton(window3, text='FEMININO', variable=valor_a, value=2, command=feminino)

        ra_1.place(x=250, y=10)
        ra_2.place(x=250, y=30)

        #Estado e spinbox
        lbtop5 = Label(window3, text="ESTADO")
        lbtop5.place(x=200, y=70)

        spin1 = Spinbox(window3, values=('Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo',
                                    'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba',
                                    'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul',
                                    'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'), wrap=True)

        
        spin1.place(x=250, y=70)


        #Endereço e entry
        lbtop4 = Label(window3, text='RUA')
        lbtop4.place(x=10, y=70)
        lbtop4_entry = Entry(window3)
        lbtop4_entry.place(x=60, y=70)

        #Número da rua
        lbtop5 = Label(window3, text='N°')
        lbtop5.place(x=10, y=100)
        lbtop5_entry = Entry(window3)
        lbtop5_entry.place(x=60, y=100)

        #Cidade
        lbtop6 = Label(window3, text='CIDADE')
        lbtop6.place(x=10, y=130)
        lbtop6_entry = Entry(window3)
        lbtop6_entry.place(x=60, y=130)

        #Bairro
        lbtop7 = Label(window3, text='BAIRRO')
        lbtop7.place(x=10, y=160)
        lbtop7_entry = Entry(window3)
        lbtop7_entry.place(x=60, y=160)

        #Telefone
        lbtop8 = Label(window3, text='FONE')
        lbtop8.place(x=10, y=190)
        lbtop8_entry = Entry(window3)
        lbtop8_entry.place(x=60, y=190)

        #RG
        lbtop9 = Label(window3, text='RG')
        lbtop9.place(x=200, y=110)
        lbtop9_entry = Entry(window3)
        lbtop9_entry.place(x=250, y=110)

        #CEP
        lbtop10 = Label(window3, text='CEP')
        lbtop10.place(x=200, y=150)
        lbtop10_entry = Entry(window3)
        lbtop10_entry.place(x=250, y=150)

        #Email
        lbtop11 = Label(window3, text='E-MAIL')
        lbtop11.place(x=200, y=190)
        lbtop11_entry = Entry(window3)
        lbtop11_entry.place(x=250, y=190)
        


        #Limpar os entry após o cadastro
        def limpar():
            lbtop1_entry.delete(0, END)
            lbtop2_entry.delete(0, END)
            #valor_a.delete(0, END)
            #spin1.delete(0, END)
            lbtop4_entry.delete(0, END)
            lbtop5_entry.delete(0, END)
            lbtop6_entry.delete(0, END)
            lbtop7_entry.delete(0, END)
            lbtop8_entry.delete(0, END)
            lbtop9_entry.delete(0, END)
            lbtop10_entry.delete(0, END)
            lbtop11_entry.delete(0, END)
            messagebox.showinfo("OK", "Cliente cadastrado")

        #Função para armazenar o valor dos dados fornecidos e guardar em um arquivo
        def getallvalues():
            getNome = lbtop1_entry.get()
            getCpf = lbtop2_entry.get()
            getSexo = valor_a.get()
            getEstado = spin1.get()
            getEndereco = lbtop4_entry.get()
            getRua = lbtop5_entry.get()
            getCidade = lbtop6_entry.get()
            getBairro = lbtop7_entry.get()
            getFone = lbtop8_entry.get()
            getRG = lbtop9_entry.get()
            getCEP = lbtop10_entry.get()
            getEmail = lbtop11_entry.get

            #Transferindo os dados cadastrados para um arquivo com o nome do cpf do cliente
            with open('{}.txt'.format(lbtop2_entry.get()), 'w+') as abrir:
                abrir.write("NOME: {}\n".format(lbtop1_entry.get()))
                abrir.write("CPF: {}\n".format(lbtop2_entry.get()))
                abrir.write("SEXO: {}\n".format(valor_a.get()))
                abrir.write("ESTADO: {}\n".format(spin1.get()))
                abrir.write("RUA: {}\n".format(lbtop4_entry.get()))
                abrir.write("N°: {}\n".format(lbtop5_entry.get()))
                abrir.write("CIDADE: {}\n".format(lbtop6_entry.get()))
                abrir.write("BAIRRO: {}\n".format(lbtop7_entry.get()))
                abrir.write("TELEFONE: {}\n".format(lbtop8_entry.get()))
                abrir.write("RG: {}\n".format(lbtop9_entry.get()))
                abrir.write("CEP: {}\n".format(lbtop10_entry.get()))
                abrir.write("EMAIL: {}\n".format(lbtop11_entry.get()))

                #abrir.seek(0)
                #print(abrir.read())

                limpar()

        #Botão confirmar tudo
        btnAll = Button(window3, text='Confirmar tudo', command=getallvalues)
        btnAll.place(x=200, y=240)

    #Função para consultar o cpf do cliente e informar seus dados cadastrados
    def consultar():
        window4 = Tk()
        window4.title("Consultar cliente")
        window4.geometry("500x300+%d+%d" % (posx, posy))

        lblBusca = Label(window4, text="INFORME O CPF", padx=165, pady=40, font="arial")
        lblBusca_entry = Entry(window4, font="arial")

        lblBusca.grid(row=0, column=0)
        lblBusca_entry.grid(row=1, column=0)

        lblpulalinha = Label(window4)
        lblpulalinha.grid(row=3, column=0)

        #Função para buscar o cpf e abrir o arquivo de acordo com o cpf do cliente
        def buscar():
            getBuscar = lblBusca_entry.get()

            window5 = Tk()
            window5.geometry("500x300+%d+%d" % (posx, posy))
            lblDados = Label(window5, text=' ', justify=LEFT)
            lblDados.grid()

            #Abrir arquivo selecionado atraves do cpf e mostrar ao usuario atraves do for
            #Tratamento de erro caso o cpf digitado nao exista
            try:
                f = open("{}.txt".format(lblBusca_entry.get()), 'r')
                dados = ""

                for i in f:
                    dados += "{}".format(i)
                    lblDados['text'] = dados
                    lblDados['font'] = 'arial'

                f.close()

            except IOError:
                messagebox.showerror('ERRO', 'CPF não encontrado \nCliente não cadastrado!')
                window5.destroy()


        #botão para buscar cpf
        btBusca = Button(window4, text="Buscar", command=buscar)
        btBusca.grid(row=4, column=0)


    #Botoes
    btn_lblwin2_1 = Button(window2, text="Continuar", command=cadastrar)
    btn_lblwin2_1.grid(row=0, column=1)

    btn_lblwin2_2 = Button(window2, text="Continuar", command=consultar)
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