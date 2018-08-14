from database import BancoDeDados

if __name__ == "__main__":
    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()

#   Inserir clientes
    print('Inserir Cliente')
    banco.inserir_cliente('Marcos', '11111111111', 'mcastrosouza@live.com')
    banco.inserir_cliente('Thomas', '22222222222', 'thomas@gmail.com')
    banco.inserir_cliente('Thomas 2', '33333333333', 'thomas@gmail.com')

#   Busca por email
    print('\nBusca Cliente por email')
    banco.buscar_email('thomas@gmail.com')
    banco.buscar_email('mcastrosouza@live.com')

#   Busca por CPF
    print('\nBusca Cliente por CPF')
    banco.buscar_cliente('22222222222')
    banco.buscar_cliente('44444444444')

#   Remover cliente
    print('\nRemove Cliente pelo CPF')
    banco.remover_cliente('22222222222')
    # banco.buscar_cliente('22222222222')

    banco.desconecta()
