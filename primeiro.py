#import psycopg2

#conn = psycopg2.connect(host='localhost', port= '5432', user='postgres', password='1771')

#cur = conn.cursor()
#
#conn.set_session(autocommit = True)

#try:
 #   cur.execute('''CREATE DATABASE musica''')
#except psycopg2.Error as e:
 #   print(e)*/

#import psycopg2

#try:
 #   # Conectar ao banco de dados 'musica'
 #   conn = psycopg2.connect(host='localhost', port='5432', database='musica', user='postgres', password='1771')
 #   cur = conn.cursor()
#
 #   # Comando SQL para inserir um novo artista
  #  insert_query = """
 #       INSERT INTO artista (nome, genero)
   #     VALUES (%s, %s)
 #   """
  #  # Dados do novo artista
  #  nome_artista = 'mateus'
  #  genero_artista = 'Pop'

    # Executar o comando SQL de inserção
  #  cur.execute(insert_query, (nome_artista, genero_artista))
 
    # Confirmar a transação
  #  conn.commit()
  #  print("Dados inseridos com sucesso!")

#except psycopg2.Error as e:
 #   print("Erro ao conectar ao banco de dados ou ao executar a inserção:", e)

#finally:
    # Fechar o cursor e a conexão
    #if cur:
   #     cur.close()
  #  if conn:
   #     conn.close()

import psycopg2

try:
    # Conectar ao banco de dados 'musica'
    conn = psycopg2.connect(host='localhost', port='5432', database='musica', user='postgres', password='1771')
    cur = conn.cursor()

    # Executar uma consulta SELECT
    cur.execute('SELECT * FROM artista')

    # Recuperar todos os resultados da consulta
    rows = cur.fetchall()

    # Exibir os resultados
    for row in rows:
        print(f"ID: {row[0]}, Nome: {row[1]}, Gênero: {row[1]}")

except psycopg2.Error as e:
    print("Erro ao conectar ao banco de dados ou ao executar a consulta:", e)

finally:
    # Fechar o cursor e a conexão
    if cur:
        cur.close()
    if conn:
        conn.close()





