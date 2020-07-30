from database import BancoDeDados 

if __name__ == "__main__":
        
        banco = BancoDeDados()
        banco.conecta()
        banco.criar_tabelas()

        banco.inserir_cliente('Leonardo', '11111111111', 'leonardomelo@unifei.edu.br')
        banco.inserir_cliente('Ezeq', '22222222222', 'ezeq_maluco@congo.com.br') 

        banco.buscar_cliente('22222222222')
        banco.buscar_email('leonardomelo@unifei.edu.br')
        banco.remover_cliente('22222222222')
        #Tentativa de Encontrar o cliente apos a remocao 
        banco.buscar_cliente('22222222222')

        banco.desconecta()
