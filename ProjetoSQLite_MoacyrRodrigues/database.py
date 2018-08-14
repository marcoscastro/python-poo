import sqlite3


class BancoDeDados:
    """
Classe que representa o banco de dados (database)
da aplicação

"""

    def __init__(self, nome='banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        """Conecta passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Desconeta do banco """
        try:
            self.conexao.close()

        except AttributeError:
            pass

    def criar_tabelas(self):
        """Cria as tabelas do banco"""
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
            print("Faça a conexão do banco antes de criar as tabelas")

    def inserir_cliente(self, nome, cpf, email):
        """Inserir cliente no banco"""
        try:
            cursor = self.conexao.cursor()

            try:
                cursor.execute("""
                    INSERT INTO clientes (nome, cpf, email) VALUES (?, ?, ?)
                """, (nome, cpf, email))

            except sqlite3.IntegrityError:
                print('O cpf %s já existe' % cpf)

            self.conexao.commit()

        except AttributeError:
            print("Faça a conexão do banco antes de inserir clientes.")

    def buscar_cliente(self, cpf):
        """Busca um cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                SELECT * FROM clientes WHERE cpf=?
            """, (cpf,))
            result = cursor.fetchone()

            if result:
                print('Cliente %s encontrado.' % result[1])

            else:
                print('Cliente com o CPF %s não localizado' % cpf)

        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes')

    def remover_cliente(self, cpf):
        """Remover cliente pelo CPF"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                DELETE FROM clientes WHERE cpf=?
            """, (cpf,))
            self.conexao.commit()
            print('Cliente com CPF %s removido.' % cpf)

        except AttributeError:
            print('Faça a conexão com o banco para remover clientes')

    def buscar_email(self, email):
        """Busca cliente pelo email"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                SELECT * FROM clientes WHERE email=?
            """, (email,))
            result = cursor.fetchall()

            if result and len(result) == 1:
                print('Cliente %s encontrado' % result[0][1])

            elif result and len(result) > 1:
                print('Mais de um cliente foi encontrado com esse email')

                for cliente in result:
                    print('    Cliente %s encontrado' % cliente[1])

            else:
                print('Nenhum cliente encontrado com o email %s' % email)

        except AttributeError:
            print('Faça a conexão com o banco antes de buscar clientes')
