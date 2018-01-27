import sqlite3


class Database(object):
    """
    Class representing the application database
    """

    def __init__(self, name='sqlite.db'):
        """
        Constructor that create a database.
        """

        self.name = name
        self.connection = None

    def connect(self):
        """
        Connect with database by passing the filename.
        """

        self.connection = sqlite3.connect(self.name)

    def disconnect(self):
        """
        Close connection
        """

        try:
            self.connection.close()
        except AttributeError:
            print("The connection is not open.")

    def create_table(self):
        """
        Create database tables.
        """

        try:
            cursor = self.connection.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL
            )
            """)

        except AttributeError:
            print("The connection is not open.")

    def insert_client(self, name, cpf, email):
        """
        Insert client into the database.
        """

        try:
            cursor = self.connection.cursor()

            cursor.execute(
                """
                INSERT INTO clients (name, cpf, email) VALUES (?,?,?)
                """,
                (name, cpf, email)
            )

            # save the changes
            self.connection.commit()

        except AttributeError:
            print("The connection is not open.")

        except sqlite3.IntegrityError:
            print("The cpf %s already exists." % cpf)

    def search_client(self, search):
        """
        Search client by cpf or email.
        """

        try:

            cursor = self.connection.cursor()

            # Get all data
            cursor.execute(
                """
                SELECT * FROM clients WHERE cpf=? OR email=?;
                """,
                (search, search)
            )

            success = False

            for line in cursor.fetchall():
                success = self.__print(line, search)

            if not success:
                print("Client %s not found" % search)

        except AttributeError:
            print("The connection is not open.")

    def __print(self, line, search):
        """
        Find a specific client.
        """

        ID = 0
        NAME = 1
        CPF = 2
        EMAIL = 3

        # Get the result of select
        print("Client [%d] found." % line[ID])
        print("NAME:", line[NAME])
        print("CPF:", line[CPF])
        print("EMAIL:", line[EMAIL])
        success = True

        return success

    def remove_client(self, cpf):
        """
        Remove client from database.
        """

        try:

            cursor = self.connection.cursor()

            # Get all data
            cursor.execute(
                """
                DELETE FROM clients WHERE cpf = ?
                """,
                (cpf,)
            )

            # save the changes
            self.connection.commit()

        except AttributeError:
            print("The connection is not open.")
