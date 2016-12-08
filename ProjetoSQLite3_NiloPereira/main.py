from db import DataBase


if __name__ == "__main__":
    db = DataBase()
    db.conn()
    #db.create_table(name='clientes')
    clients = ({'nome': 'Nilo', 'cpf': '11111111111', 'email': 'nilo@teste.com'},
               {'nome': 'Marcos', 'cpf': '22222222222', 'email': 'marcos@teste.com'},
    )
    #for c in clients:
    #    db.insert_client(table_name='clientes', **c)
    c = db.search_client_by_cpf('11111111111')
    print(c)
    c = db.search_client_by_email('marcos@teste.com')
    print(c)
    #db.remove_client(cpf='22222222222')
