import random
import string
from tkinter import *
from tkinter.ttk import Notebook
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox
from tkinter import simpledialog

# codigo simples para geração de senha


def gerar_senha(tamanho=10):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres)
                    for _ in range(tamanho))
    return senha

# geração de email


def gerar_email(tamanho=10):
    letras = string.ascii_letters + string.digits
    usuario = ''.join(random.choice(letras)
                      for _ in range(tamanho))
    return usuario + '@gmail.com'

# gerar arquivo com emails e senhas


def gerar_e_escrever_arquivo(novo_arquivo, num):
    with open(novo_arquivo, 'w') as arq:
        for i in range(num):
            tamanho_do_email = random.randint(15, 26)
            tamanho_da_senha = random.randint(9, 15)
            novo_email = gerar_email(tamanho_do_email)
            nova_senha = gerar_senha(tamanho_da_senha)
            linha = f'{i+1}. Email: {novo_email}, Senha: {nova_senha}\n'
            arq.write(linha)

# função para gerar a quantidade de emails e senha digitados


def gerar_senhas_emails():
    num = simpledialog.askinteger("Quantidade de Senhas e Emails",
                                  "Digite quantos emails e senhas você quer!\n OBS: Não coloque acima de 10 mil, isso pode travar seu computador!")
    if num is not None:
        novo_arquivo = 'Senhas_e_Emails.txt'

        gerar_e_escrever_arquivo(novo_arquivo, num)
        print(f'O arquivo "{novo_arquivo}" foi criado com sucesso!')

        lb2.after(1, lambda: lb2.config(
            text='Para gerar seus emails e senhas \n clique no botão acima!', bg='gray', start=1))

        tela.after(1, lambda: lb2.config(
            text='Emails e senhas gerados com sucesso!', bg='green'))

        # muda a palavra email, e senha para uma cor definida
        with open(novo_arquivo, 'r') as arq:
            conteudo = arq.read()
            texto.config(state='normal')
            texto.delete(1.0, END)
            texto.insert(END, conteudo)
            texto.config(state='disabled')
            # email
            texto.tag_configure("email", foreground="green")
            start = "1.0"
            while True:
                start = texto.search("Email", start, stopindex=END)
                if not start:
                    break
                end = f"{start}+{len('Email')}c"
                texto.tag_add("email", start, end)
                start = end
            # senha
            texto.tag_configure("senha", foreground="green")
            start = "1.0"
            while True:
                start = texto.search("Senha", start, stopindex=END)
                if not start:
                    break
                end = f"{start}+{len('Senha')}c"
                texto.tag_add("senha", start, end)
                start = end

# codigo para download de música


def baixar_musica(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download('estudos')
        # acho que o nome ja explica né...
        messagebox.showinfo("Sucesso", "Sua música foi baixada com sucesso!")
    except Exception as e:
        messagebox.showerror(
            "Erro", f"Ocorreu um erro ao baixar a música: {e}")

# codigo para download de vídeo


def baixar_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        # mesma coisa do outro
        messagebox.showinfo("Sucesso", "Vídeo baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo: {e}")

# selecionador de opção; mp3, mp4


def selecionar_opcao():
    selected_opcao = var.get()
    url = Ent.get()
    if selected_opcao == "mp3":
        baixar_musica(url)
    elif selected_opcao == "mp4":  # opções de qualidade
        baixar_video(url)

# texto que aparece na informação


def texto_da_info():
    texto2.config(state='normal')
    texto2.delete(1.0, END)
    texto2.insert(END, "Este aplicativo é capaz de gerar até 150 emails e senhas aleatórios\n e fazer o download de vídeos e músicas."
                  "Ele foi criado por um adoslecente de 14 anos, em 29/03/2024\n espero que gostem!")
    texto2.config(state='disabled')

    lb2.after(3000, lambda: texto2.config(state='normal',
              text='Para ver as informações, clique no botão acima!'))  # texto da informação
    texto2.after(3000, lambda: texto2.config(state='disabled'))
    return


# codígo para fazer a interface ser criada
tela = Tk()
tela.title('Senhas, Emails, Vídeos e Músicas')
tela.geometry('400x500')
tela.config(bg='black')


notebook = Notebook(tela)

# abas que podem ser acessadas dentro da interface
tab_gerar = ttk.Frame(notebook)
tab_baixar = ttk.Frame(notebook)
tab_info = ttk.Frame(notebook)
tab_anotaçoes = ttk.Frame(notebook)

notebook.add(tab_gerar, text="Gerar Senhas e Emails")
notebook.add(tab_baixar, text="Baixar Vídeos e Músicas")
notebook.add(tab_info, text='Informações')
notebook.add(tab_anotaçoes, text='Anotações')

notebook.pack(expand=1, fill="both")

# função para guardar os itens dentro de uma pasta


def salvar_anotacoes():
    with open('anotacoes.txt', 'w') as arquivo:
        anotacoes = lb4.get("1.0", END)
        arquivo.write(anotacoes)


# Botão que sempre que clicado, guarda as anotações
bt_salvar = Button(tab_anotaçoes, text="Salvar Anotações",
                   command=salvar_anotacoes)
bt_salvar.pack()


lb3 = Label(tab_anotaçoes, text='Faça suas anotações aqui',
            bg='black', fg='white')
lb3.pack()
lb4 = Text(tab_anotaçoes, width=50, height=30,
           wrap=WORD, bg='black', fg='white')
lb4.pack()

lb1 = Label(tab_baixar, text='Digite o URL da música/vídeo: ',
            bg='black', fg='white')
lb1.pack()

Ent = Entry(tab_baixar, width=30)
Ent.pack()

# opções de música e vídeo
opcoes = ['mp3', 'mp4']
var = StringVar(tab_baixar)
var.set(opcoes[0])
opcao_menu = OptionMenu(tab_baixar, var, *opcoes)
opcao_menu.pack()

btn_selecionar = Button(tab_baixar, text="Selecionar",
                        command=selecionar_opcao)
btn_selecionar.pack()

# labels e botões finais, varios dos labels e botões são sobre as abas
bt1 = Button(tab_gerar, bg='#80B460', width=20, height=2,
             text='Gerar senhas e emails.', font=('Bodoni', 14), command=gerar_senhas_emails)
bt1.grid(row=0, column=0)

texto = Text(tab_gerar, width=50, height=20, wrap=WORD, bg='black', fg='white')
texto.grid(row=1, column=0, padx=10, pady=1)
texto.config(state='disabled')

lb2 = Label(tab_gerar, width=35, height=5, bg='gray', font=('Arial', 14))
lb2.grid(row=2, column=0)

bt2 = Button(tab_info, bg='#80B460', width=20, height=2,
             text='Ver informações', font=('Bodoni', 14), command=texto_da_info)
bt2.grid(row=0, column=0, padx=10, pady=1)

texto2 = Text(tab_info, width=50, height=20, wrap=WORD, bg='black', fg='red')
texto2.grid(row=1, column=0, padx=10, pady=1)
texto2.config(state='disabled')


if __name__ == '__main__':
    tela.mainloop()
