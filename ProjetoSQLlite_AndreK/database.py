import sqlite3

class BancoDeDados:
	"""classe que representa o banco de dados"""

	def __init__(self,nome='banco.db'):
		self.nome,self.conexao=nome,None

	def conecta(self):
		"""conecta passando o nome do arquivo"""
		self.conexao=sqlite3.connect(self.nome)

	def desconecta(self):
		"""desconecta do banco"""
		try:
		 	self.conexao.close()
		except AttributeError:
			pass

	def criar_tabelas(self):
		"""cria as tabelas do banco"""
		try:
			cursor=self.conexao.cursor()
			cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes(
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				nome TEXT NOT NULL,
				cpf VARCHAR(11) UNIQUE NOT NULL,
				email TEXT NOT NULL
			);

			""")


		except AttributeError:
			print("faca a conexao do banco")

	def inserir_clientes(self,nome,cpf,email):
		"""inseri cliente no banco"""
		try:
			cursor=self.conexao.cursor()
			try:

				cursor.execute("""
					INSERT INTO clientes (nome,cpf,email) VALUES (?,?,?)
				""",(nome,cpf,email))
				print("cliente %s inserido com sucesso" %nome)
			except sqlite3.IntegrityError:
				print("o cpf %s ja existe " %cpf)

			self.conexao.commit()

		except AttributeError:
			print ("faca a conexao antes de inserir clientes")

	def buscar_clientes(self,cpf):
		""" busca um cliente pelo cpf"""
		try:
			cursor=self.conexao.cursor()
			#obtem todos os dados
			cursor.execute("""SELECT * FROM CLIENTES;""")

			for linha in cursor.fetchall():
				if linha[2]==cpf:
					print("cliente %s encontrado" %linha[1])
				else:
					print("cliente %s NAO encontrado" %cpf)

		except AttributeError:
			print ("conecte o banco antes de buscar o cliente")

	def deletar_clientes(self,cpf):
		"""deleta um cliente pelo cpf"""
		try:

			cursor=self.conexao.cursor()
			#obtem todos os dados
			cursor.execute("""SELECT * FROM CLIENTES;""")

			for linha in cursor.fetchall():
				if linha[2]==cpf:
					cursor.execute("""DELETE from CLIENTES where cpf=%s"""%cpf)
					print("cliente %s excluido com sucesso" %cpf)
				
		except AttributeError:
			print("conecte antes de deletar")

		self.conexao.commit()

	def buscar_email(self,email):
		""" busca um cliente pelo email"""
		try:
			cursor=self.conexao.cursor()
			#obtem todos os dados
			cursor.execute("""SELECT * FROM CLIENTES;""")

			for linha in cursor.fetchall():
				if linha[3]==email:
					
					return True
				else:
					return False

		except AttributeError:
			print ("conecte o banco antes de buscar o cliente")