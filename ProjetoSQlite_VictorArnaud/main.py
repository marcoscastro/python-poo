from database import Database


def main():
    """
    Função principal
    """

    database = Database()
    database.connect()
    database.create_table()
    database.insert_client('Marcos', '111111111', 'marcos@gmail.com')
    database.insert_client('Tomas', '111122222', 'tomas@gmail.com')
    database.search_client('111122222')
    database.remove_client('111122222')
    database.search_client('111122222')
    database.disconnect()


if __name__ == "__main__":
    main()
