import sqlite3

class BancoDeDados:
	"""Classe que representa o banco de dados (database) da aplicação"""

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
			pass

	def criar_tabelas(self):
		"""Cria as tabelas do banco"""
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					nome TEXT NOT NULL,
					senha VARCHAR(20) NOT NULL,
					cpf VARCHAR(11) UNIQUE NOT NULL,
					email TEXT NOT NULL
			);
			""")

		except AttributeError:
			print('Faça a conexão do banco antes de criar as tabelas.')

	def inserir_cliente(self, nome, senha, cpf, email):
		"""Insere cliente no banco"""
		try:
			cursor = self.conexao.cursor()

			try:
				cursor.execute("""
					INSERT INTO clientes (nome, senha, cpf, email) VALUES (?,?,?,?)
				""", (nome, senha, cpf, email))
			except sqlite3.IntegrityError:
				print('O cpf %s já existe!' % cpf)

			self.conexao.commit()

		except AttributeError:
			print('Faça a conexão do banco antes de inserir clientes.')

	def buscar_cliente(self, cpf):
		"""Busca um cliente pelo cpf"""
		try:
			cursor = self.conexao.cursor()

			# obtém todos os dados
			cursor.execute("SELECT * FROM clientes WHERE cpf=?", [(cpf)])

			cliente = cursor.fetchone()
			
			if cliente:
				return True
			return False
		except AttributeError:
			print('Faça a conexão do banco antes de buscar clientes.')


	def login(self, username, senha):
		
		try:
			cursor = self.conexao.cursor()
			sql = 'SELECT * FROM clientes WHERE nome=? and senha=?'
			cliente = cursor.execute(sql, [username, senha]).fetchone()

			if cliente:
				return True
			return False

		except AttributeError:
			print('Faça a conexão do banco.')

	def remover_cliente(self, cpf):

		try:
			cursor = self.conexao.cursor()
			sql1 = "SELECT * FROM clientes WHERE CPF = ?"
			sql2 = "DELETE FROM clientes where CPF = ?"
			cliente = False

			cliente = cursor.execute(sql1,(cpf,)).fetchone()

			if cliente:
				cursor.execute(sql2,(cpf,))
				print('Cliente removido com sucesso!')
			else:
				print('Cliente com o cpf {} não foi encontrado.'.format(cpf))
		except AttributeError:
			print('Faça a conexão do banco')		
		

	def buscar_email(self, email):
		
		try:
			cursor = self.conexao.cursor()
			sql = "SELECT * FROM clientes WHERE email = ?"
			cliente = False

			cliente = cursor.execute(sql,(email,)).fetchone()

			if cliente:
				print("Cliente encontrado!")
			else:
				print("Nenhum cliente encontrado com o email: {}".format(email))

		except AttributeError:
			print('Faça a conexão do banco')