import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `projsoft`;")

cursor.execute("CREATE DATABASE `projsoft`;")

cursor.execute("USE `projsoft`;")

# criando tabelas
TABLES = {}

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(20) NOT NULL,
      `idade` int(150) NOT NULL,
      `email` varchar(256) NOT NULL,
      `senha` varchar(100) NOT NULL,
      `tipoUsuario` int(5) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Produtos'] = ('''
      CREATE TABLE `produtos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `descricao` varchar(100) NOT NULL,
      `valor` int(5000) NOT NULL,
      `usuarioId` int(11) NOT NULL,
      `avaliacao` int(11) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (usuarioId) REFERENCES Usuarios(id)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Pedido'] = ('''
      CREATE TABLE `produtos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `total` int(5000) NOT NULL,
      `status` varchar(50) NOT NULL,
      `usuarioId` int(11) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (usuarioId) REFERENCES Usuarios(id)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Pagamento'] = ('''
      CREATE TABLE `produtos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `formaDePagamento` int(2) NOT NULL,
      `status` varchar(50) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Carrinho'] = ('''
      CREATE TABLE `produtos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `quantidade` int(100) NOT NULL,
      `subTotal` float(5000.0) NOT NULL,
      `status` varchar(50) NOT NULL,
      `usuarioId` int(11) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (usuarioId) REFERENCES Usuarios(id)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Lucas Couto", "Lucao", generate_password_hash("123456").decode('utf-8')),
      ("Lucas Pimenta", "Pimenta", generate_password_hash("Pimenta@123").decode('utf-8')),
      ("User Projeto", "user", generate_password_hash("123456").decode('utf-8'))
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from projsoft.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo produtos
produtos_sql = 'INSERT INTO produtos (nome, categoria, console) VALUES (%s, %s, %s)'
produtos = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(produtos_sql, produtos)

cursor.execute('select * from projsoft.produtos')
print(' -------------  Produtos:  -------------')
for produto in cursor.fetchall():
    print(produto[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()