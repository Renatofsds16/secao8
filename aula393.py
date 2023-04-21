import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
TABLE_NAME = ROOT_DIR/'basedados.db'


conexao = sqlite3.connect('basedados.db')
cursor = conexao.cursor()


cursor.execute('DELETE FROM clientes WHERE id=4')
conexao.commit()
cursor.execute('select * FROM clientes')
cursor.execute('UPDATE clientes SET name="yasmim" where id=3')
conexao.commit()
for row in cursor.fetchall():
    id, name, peso = row
    print(id, name, peso)


cursor.close()
conexao.close()
