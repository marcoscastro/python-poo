from database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_cliente('Marcos', '11111111111', 'mcastrosouza@live.com')
	banco.inserir_cliente('Thomas', '22222222222', 'thomas@gmail.com')
	banco.buscar_cliente('22222222222')
	banco.buscar_email('thomas@gmail.com')
	banco.buscar_email('thomas@gma23il.com')
	banco.remover_cliente(11111111111)
	
	banco.desconecta()