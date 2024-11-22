import fdb

# Configurações do banco de dados
database_path = "C:/aspec/db/CHAVAL-ENVIAR-230390701.FDB"
user = "sysdba"  
password = "masterkey"
host = "localhost"  
charset = "UTF8"  

try:
    # Conectando ao banco de dados
    connection = fdb.connect(
        dsn=f"{host}:{database_path}",
        user=user,
        password=password,
        charset=charset
    )
    print("Conexão bem-sucedida ao banco de dados!")

    # Criando um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Executando uma consulta simples
    cursor.execute("SELECT * FROM funcionario")  
    rows = cursor.fetchall()

    # Imprimindo os resultados
    for row in rows:
        print(row)

    # Fechando a conexão
    cursor.close()
    connection.close()

except fdb.DatabaseError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
