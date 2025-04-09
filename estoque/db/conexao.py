import psycopg2

#Conexão com banco de dados Postgress
def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="sistema_db",
            user="postgres",           
            password="q1w2e3", 
            host="localhost",
            port="5432"
        )
        print("[OK] Conexão estabelecida com sucesso!")
        return conexao
    except Exception as e:
        print(f"[ERRO] Falha na conexão: {e}")
        return None
