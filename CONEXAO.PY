import mysql.connector


def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Root',
            database='P1'
        )
        cursor = conexao.cursor()
        print("Conexão bem-sucedida!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

conectar_banco()