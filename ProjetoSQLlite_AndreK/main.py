from database import BancoDeDados


if __name__ =="__main__":
	
	banco=BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_clientes('marcos','1111111111','madsf@fsdfsdc.com')
	banco.inserir_clientes('thomas','222222222','sddds@fsdfsdc.com')
	banco.buscar_clientes('1111111111')
	banco.deletar_clientes('1111111111')
	banco.buscar_clientes('1111111111')
	print(banco.buscar_email('sddds@fsdfsdc.com'))
	banco.desconecta() 