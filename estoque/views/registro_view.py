from tkinter import Label, Entry, Button
from auth.registro import registrar_usuario

def tela_registro(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    janela.title("Cadastro de Usuário")

    Label(janela, text="Nome").pack()
    nome_entry = Entry(janela)
    nome_entry.pack()

    Label(janela, text="Usuário").pack()
    usuario_entry = Entry(janela)
    usuario_entry.pack()

    Label(janela, text="Senha").pack()
    senha_entry = Entry(janela, show="*")
    senha_entry.pack()

    Button(janela, text="Cadastrar", command=lambda: registrar_usuario(
        nome_entry.get(),
        usuario_entry.get(),
        senha_entry.get()
    )).pack(pady=10)

    # Botão para voltar ao login
    from views.login_view import exibir_tela_login
    Button(janela, text="Voltar ao login", command=lambda: exibir_tela_login(janela)).pack()
