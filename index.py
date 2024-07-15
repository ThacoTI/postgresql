import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1771",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_table(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100)
            )
        """)
        conn.commit()

def insert_user(conn, name, email):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO users (name, email) VALUES (%s, %s)
        """, (name, email))
        conn.commit()

def get_users(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()
        return users

def update_user(conn, user_id, name, email):
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE users SET name = %s, email = %s WHERE id = %s
        """, (name, email, user_id))
        conn.commit()

def delete_user(conn, user_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()

if __name__ == "__main__":
    conn = connect()
    
    if conn:
        # Criar tabela
        create_table(conn)

        # Inserir um usuário
        insert_user(conn, "João Silva", "joao@example.com")

        # Ler usuários
        users = get_users(conn)
        for user in users:
            print(user)

        # Atualizar um usuário
        update_user(conn, 5, "João Silva Atualizado", "joao_atualizado@example.com")

        # Excluir um usuário
        delete_user(conn, 6)

        # Fechar a conexão
        conn.close()
