import sqlite3 

class BancoDeDados:
        """Classe que representa o banco de dados (database) da aplicacao"""

        def __init__(self, nome='banco.db'):
                self.nome, self.conexao = nome, None
                
        def conecta(self):
                """Conecta passando o nome do arquivo"""
                self.conexao = sqlite3.connect(self.nome) 

        def desconecta(self):
                """Desconecta do banco de dados"""
                try:
                        self.conexao.close()
                except AttributeError:
                        pass

        def criar_tabelas(self):
                """Cria as tabelas do Banco"""
                try:
                        cursor = self.conexao.cursor()
                        
                        cursor.execute("""
                                CREATE TABLE IF NOT EXISTS clientes (
                                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        nome TEXT NOT NULL,
                                        cpf VARCHAR(11) UNIQUE NOT NULL, 
                                        email TEXT NOT NULL
                                );     
                        """)                        
                        
                except AttributeError:
                        print("Faça a conexao do banco antes de criar as tabelas")

        def inserir_cliente(self, nome, cpf, email):
                """Insere Cliente no banco """
                try:
                        try:
                                cursor = self.conexao.cursor()
                                
                                cursor.execute("""
                                        INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)
                                """, (nome, cpf, email))
                        except sqlite3.IntegrityError:
                                print('O cpf %s já existe!' % cpf)
                                
                        
                        self.conexao.commit()
                except AttributeError:
                       print("Faça a conexão do banco antes de inserir clientes")
        
        def buscar_cliente(self, cpf):
                """Buscar um cliente pelo cpf"""
                try:
                        cursor = self.conexao.cursor()

                        #Obtém todos os dados 
                        cursor.execute(""" SELECT * FROM clientes;""")

                        for linha in cursor.fetchall():
                                if linha[2] == cpf:
                                        print('Cliente %s encontrado.' % linha[1])
                                        break 
                except AttributeError:
                        print("Faça a conexão do banco de dados antes de buscar clientes")

        def remover_cliente(self, cpf):
                """Remover um cliente pelo seu cpf"""
                try:
                        cursor = self.conexao.cursor()
                        cursor.execute("""DELETE FROM clientes WHERE cpf=(?)""", (cpf,))
                        self.conexao.commit()
                except AttributeError:
                        print("Faça a conexão do banco de dados antes de remover clientes")
       
        def buscar_email(self, email):
                "Buscar um cliente pelo seu email""" 
                try:
                        cursor = self.conexao.cursor()

                        #Obtém todos os dados 
                        cursor.execute(""" SELECT * FROM clientes;""")

                        for linha in cursor.fetchall():
                                if linha[3] == email:
                                        print('Cliente %s encontrado.' % linha[1])
                                        break 
                except AttributeError:
                        print("Faça a conexão do banco de dados antes de buscar clientes")

        
