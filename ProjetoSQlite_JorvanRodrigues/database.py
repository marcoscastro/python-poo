import sqlite3


class BancoDeDados:
	"""Classe que representa o banco de dados da aplicação"""


	def __init__(self, nome='banco.db'):
                
		self.nome, self.conexao = nome, None


	def conecta(self):
		"""Conecta passando o nome do arquivo"""
		
		self.conexao = sqlite3.connect(self.nome)


	def desconecta(self):
		"""Desconecta do banco"""
		
		try:
			self.conexao.close()

		except AttributeError:
			print('Conecte ao banco primeiro.')


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
			print('Faça a conexão do banco antes de criar as tabelas.')


	def inserir_cliente(self, nome, cpf, email):
		"""Insere cliente no banco"""

		try:
			cursor = self.conexao.cursor()
			try:
				cursor.execute("""
					INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)

				""", (nome, cpf, email))
				self.conexao.commit()

			except sqlite3.IntegrityError:
				print('O CPF %s ja existe para o(a) cliente %s.' % (cpf, nome))

		except AttributeError:
			print('Faça a conexão do banco antes de inserir clientes.')


	def buscar_cliente(self, cpf):
		"""Localiza um cliente pelo CPF"""
		
		try:
			cursor = self.conexao.cursor()
			# Obtém todos os dados.
			cursor.execute("""SELECT * FROM clientes;""")

			for linha in cursor.fetchall():
				if linha[2] == cpf:
					print('Cliente %s encontrado' % linha[1])
					return linha[1]
					break

		except AttributeError:
			print('Faça a conexão do banco antes de buscar clientes.')


	def remover_cliente(self, cpf):
		"""Rmove um cliente do banco pelo CPF"""
		
		try:
			cursor = self.conexao.cursor()
			cli = self.buscar_cliente(cpf)			
			cursor.execute("""DELETE FROM clientes WHERE cpf = %d""" % int(cpf))
			self.conexao.commit()

			if self.buscar_cliente(cpf) != 'None':
				print('O cliente %s foi removido com sucesso.' % cli)
			else:
				print('O CPF %s nao esta cadastrado no banco.' % cpf)

		except AttributeError:
			'Faça a conexão do banco antes de remover um cliente.'


	def buscar_email(self, email):
		"""Localiza um cliente pelo email"""
		
		try:
			cursor = self.conexao.cursor()

			# Obtém todos os dados.
			cursor.execute("""SELECT * FROM clientes;""")

			for linha in cursor.fetchall():
				if linha[3] == email:					
					return True					
			return False
		
		except AttributeError:
			print('Faça a conexão do banco antes de buscar clientes.')




