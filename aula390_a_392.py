import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'basedados.db'
DB_FILE = ROOT_DIR/DB_NAME
TABLE_NAME = 'clientes'
conexao = sqlite3.connect(DB_FILE)
cursor = conexao.cursor()
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(''id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name text,'
    'weitgh REAL'')'
    )
conexao.commit()
cursor.execute(f'DELETE FROM {TABLE_NAME}')
conexao.commit()
#cursor.execute(f'INSERT INTO {TABLE_NAME} (name, weitgh) '
#               'VALUES'
#                '("nice", 10), ("taty", 68.6)'
#                )
#conexao.commit()
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"' )
conexao.commit()
sql = f'INSERT INTO {TABLE_NAME} (name, weitgh) VALUES (:nome, :peso)'

cursor.executemany(sql, [
    {'nome':'rian', 'peso':6},
    {'nome':'elias','peso': 7},
    {'nome':'julia', 'peso': 9},
    {'nome':'yasmi', 'peso': 9}
    ]
    )
conexao.commit()


print(sql)

cursor.close()
conexao.close()
