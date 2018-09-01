from database import BancoDeDados

if __name__ == "__main__":
	
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_cliente('Tony Stark', 'jarvis', '44444444444', 'tony@starkindustries.com')
	banco.inserir_cliente('Black Widow', 'banner', '55555555555', 'widow@gmail.com')
	banco.inserir_cliente('Doctor Strange', 'strange', '66666666666', 'doctor@strange.com')
	banco.remover_cliente('44444444444')
	banco.buscar_email('tony@starkindustries.com')
	print(banco.login('joao','ruby'))
	banco.desconecta()