import sqlite3

class BancoDeDados:
    """Classe que representa o banco de dados"""

    def __init__( self,nome = 'BancoClientes.db' ):
        self.nome,self.conexao = nome,None

    def conecta( self ):
        self.conexao = sqlite3.connect( self.nome )

    def desconecta( self ):

        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas( self ):

        try:
            cursor = self.conexao.cursor()

            cursor.execute( """
            create table if not exists clientes(
            id integer not null primary key autoincrement,
            nome text not null,
            cpf varchar(11) unique not null,
            email text not null
            );
                """ )

        except AttributeError:
            print( 'realize a conexão antes de criar as tabelas.' )

    def inserir_cliente( self, nome, cpf, email ):
        """Insere cliente no banco"""
        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute( """Insert into clientes (nome, cpf, email) values (?,?,?)""",( nome,cpf,email ) )
            except sqlite3.IntegrityError:
                print( 'O CPF %s já existe ' % cpf )
            else:
                self.conexao.commit()
                print( 'Cliente inserido com sucesso.' )

        except AttributeError:
            print( 'Faça a conexão no banco antes de inserir os dados' )

    def buscar_cliente( self,cpf ):
        """Bucar o cliente direto pelo cpf"""
        try:
            cursor = self.conexao.cursor()
            for linha in cursor.execute( """ select * from clientes where cpf =""" + cpf ):
                print( 'Cliente %s encontrado' % linha[1] )

        except AttributeError:
            print( 'Faça a conexão no banco antes de buscar os dados' )

    def excluir_clientes( self,cpf ):

        try:
            cursor = self.conexao.cursor()
            """Valido o se o cliente existe antes da excluir"""
            for linha in cursor.execute( """ select * from clientes where cpf =""" + cpf ):
                cursor.execute( """ delete from clientes where cpf =""" + linha[2] )
                print( 'Cliente %s excluido com sucesso.' % linha[1] )
                self.conexao.commit()

        except AttributeError:

            print( 'Faça a conexão no banco antes de buscar os dados' )

    def buscar_email( self, email ):
        email_existe = False
        try:
            cursor = self.conexao.cursor()
            for linha in cursor.execute( """ select * from clientes """ ):
                if linha[3] == email:
                    email_existe = True
            return email_existe
        except AttributeError:
            print( 'Faça a conexão no banco antes de buscar os dados' )
