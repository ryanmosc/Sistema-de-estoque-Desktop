from db.conexao import conectar
import bcrypt
from tkinter import messagebox
from views.home_view import criar_tela_inicial

#Login
def verificar_login(nome_usuario, senha, janela):
    if not nome_usuario or not senha:
        messagebox.showerror("Erro", "Nome de usuário e senha são obrigatórios!")
        return False

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT usuario, senhas FROM usuarios WHERE usuario = %s", (nome_usuario,))
        resultado = cursor.fetchone()

        if not resultado:
            messagebox.showerror("Erro", "Usuário não encontrado.")
            return False

        _, hash_armazenado = resultado
        senha_bytes = senha.encode('utf-8')

        if isinstance(hash_armazenado, str):
            hash_armazenado = hash_armazenado.encode('utf-8')

        if bcrypt.checkpw(senha_bytes, hash_armazenado):
            janela.destroy()  
            criar_tela_inicial() 
        else:
            messagebox.showerror("Erro", "Senha incorreta.")
            return False

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao verificar login: {e}")
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if conexao: conexao.close()

