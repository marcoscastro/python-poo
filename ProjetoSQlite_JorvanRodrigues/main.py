from database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_cliente('Jorvan', 11111111111, 'jrbsolucoes@gmail.com')
	banco.inserir_cliente('Daniel', 22222222222, 'daniel@gmail.com')
	banco.inserir_cliente('Jessica', 33333333333, 'jessica@gmail.com')
	banco.buscar_cliente('11111111111')
	banco.remover_cliente('11111111111')	
	print(banco.buscar_email('daniel@gmail.com'))
	print(banco.buscar_email('dan@gmail.com'))
	banco.desconecta()
