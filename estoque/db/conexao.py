import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="estoque_db",
            user="postgres",           
            password="q1w2e3", 
            host="localhost",
            port="5432"
        )
        print("[OK] Conexão estabelecida com sucesso!")
        conexao.close()
    except Exception as e:
        print(f"[ERRO] Falha na conexão: {e}")

conectar()
