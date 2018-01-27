import sqlite3


class BancoDeDados:
    '''
    Classe que representa o banco de dados (database) da aplicação
    '''

    def __init__(self, nome='ProjetoSQlite_AndersonMatheus/banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        '''
        Conecta passando o nome do arquivo
        '''
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        '''
        Desconecta do Banco
        '''
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas(self):
        '''
        Cria as tabelas do banco
        '''
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    cpf VARCHAR(11) UNIQUE NOT NULL,
                    email TEXT NOT NULL
                );
            """)
        except AttributeError:
            print('Faça a conexão do banco de dados antes de criar as tabelas')

    def inserir_cliente(self, nome, cpf, email):
        '''
        Insere cliente no Banco
        '''
        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute("""
                    INSERT INTO clientes (name,
                                          cpf,
                                          email) VALUES (?, ?, ?);
                """, (nome, cpf, email))
            except sqlite3.IntegrityError:
                print('O cpf %s já existe!' % cpf)
            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão do banco de dados antes de inserir clientes')

    def buscar_cliente(self, cpf):
        '''
        Busca um cliente pelo cpf
        '''
        try:
            cursor = self.conexao.cursor()
            # obtém todos os clientes
            cursor.execute("""
                SELECT * FROM clientes;
            """)

            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print('Cliente %s encontrado.' % linha[1])
                    break
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes')

    def remover_cliente(self, cpf):
        '''
        Remove um cliente pelo cpf
        '''
        try:
            cursor = self.conexao.cursor()
            result = cursor.execute("""
                DELETE FROM clientes WHERE cpf=(?)
            """, (cpf,)).rowcount
            self.conexao.commit()
            if result > 0:
                print('O usuário do cpf %s foi removido com sucesso' % cpf)
            else:
                print('O usuário do cpf %s não foi encontrado para remoção'
                      % cpf)
        except AttributeError:
            print('Faça a conexão do banco antes de remover um cliente')

    def buscar_cliente_email(self, email):
        '''
        Busca um cliente pelo email
        '''
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                SELECT * FROM clientes WHERE email=(?)
            """, (email,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                for user in rows:
                    print('Usuário encontrado: Nome %s ; email %s'
                          % (user[1], user[3]))
            else:
                print('Não foi encontrado nenhum usuário com este email')
        except AttributeError:
            print('Faça a conexão do banco aantes de buscar um cliente')
