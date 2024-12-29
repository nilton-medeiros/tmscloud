import mariadb
from mariadb import Error
from src.domain.models.user import User
from src.domain.models.nome_pessoa import NomePessoa
from src.domain.models.phone_number import PhoneNumber
from src.db.interfaces.user_repository import UserRepository

# REFATORAR ANTES DE UTILIZAR ESTE MÓDULO

# BIBLIOTECA RECOMENDADA!
# pip install mariadb
# pip update mariadb

# Alternativa: pymysql
# pip install pymysql

'''
As principais diferenças em relação à implementação MySQL são:

Uso do pacote mariadb ao invés de mysql-connector
Uso de ? como placeholder nas queries ao invés de %s
Algumas pequenas diferenças na configuração da conexão
'''


class MariaDBUserRepository(UserRepository):
    '''
    Repositório de usuários para a persistência utilizando MariaDB.
    Utiliza a biblioteca mariadb para conectar com o banco de dados MariaDB.
    ATENÇÃO: REFATORAR ANTES DE UTILIZAR ESTE MÓDULO
    '''
    def __init__(self):
        # Configuração da conexão MariaDB
        self.config = {
            'host': 'localhost',
            'user': 'seu_usuario',
            'password': 'sua_senha',
            'database': 'seu_banco',
            'port': 3306
        }

    def get_connection(self):
        try:
            return mariadb.connect(**self.config)
        except Error as e:
            raise Exception(f"Erro ao conectar ao MariaDB: {e}")

    async def save(self, user: User) -> User:
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            if user.id:
                # Update
                query = """
                    UPDATE users
                    SET email = ?,
                        primeiro_nome = ?,
                        sobrenome = ?,
                        phone_number = ?,
                        profile = ?
                    WHERE id = ?
                """
                values = (
                    user.email,
                    user.display_name.primeiro_nome(),
                    user.display_name.sobrenome(),
                    str(user.phone_number),
                    user.profile,
                    user.id
                )
                cursor.execute(query, values)

            else:
                # Insert
                query = """
                    INSERT INTO users
                    (email, primeiro_nome, sobrenome, phone_number, profile)
                    VALUES (?, ?, ?, ?, ?)
                """
                values = (
                    user.email,
                    user.display_name.primeiro_nome(),
                    user.display_name.sobrenome(),
                    str(user.phone_number),
                    user.profile
                )
                cursor.execute(query, values)
                user.id = str(cursor.lastrowid)  # Atualiza o ID do usuário

            connection.commit()
            return user

        except Error as e:
            connection.rollback()
            raise Exception(f"Erro ao salvar usuário: {e}")

        finally:
            cursor.close()
            connection.close()

    async def find_by_email(self, email: str) -> User:
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            query = "SELECT * FROM users WHERE email = ?"
            cursor.execute(query, (email,))
            result = cursor.fetchone()

            if result:
                return User(
                    id=str(result['id']),
                    email=result['email'],
                    display_name=NomePessoa(
                        result['primeiro_nome'],
                        result['sobrenome']
                    ),
                    phone_number=PhoneNumber(result['phone_number']),
                    profile=result['profile']
                )
            return None

        except Error as e:
            raise Exception(f"Erro ao buscar usuário: {e}")

        finally:
            cursor.close()
            connection.close()