from database import BancoDeDados

if __name__ == '__main__':
    banco = BancoDeDados()
    banco.conecta()
    banco.criar_tabelas()

    banco.inserir_cliente('Lucas Henry Freitas',
                          '69824857818',
                          'llucashenryfreitas@djapan.com.br')
    banco.inserir_cliente('Enrico Raul Pedro Barbosa',
                          '25909656210',
                          'eenricoraulpedrobarbosa@dc4.com.br')
    banco.inserir_cliente('Joaquim Guilherme Rodrigues',
                          '91436687470',
                          'eenricoraulpedrobarbosa@dc4.com.br')

    banco.buscar_cliente('25909656210')

    cpf = '69824857818'
    remover = banco.remover_cliente(cpf)

    email = 'eenricoraulpedrobarbosa@dc4.com.br'
    buscar = banco.buscar_cliente_email(email)
    banco.desconecta()
