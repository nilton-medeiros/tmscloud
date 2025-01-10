# db/mysql/mysql_user_repository.py
import mysql.connector
from mysql.connector import Error

from src.domain.models.user import User
from src.domain.models.nome_pessoa import NomePessoa
from src.domain.models.phone_number import PhoneNumber
from src.db.interfaces.user_repository import UserRepository

# REFATORAR ANTES DE UTILIZAR ESTE MÓDULO

# BIBLIOTECA RECOMENDADA!
# pip install mysql-connector-python
# pip update mysql-connector-python
# pip show mysql-connector-python

# Alternativa: pymysql
# pip install pymysql


'''
As principais diferenças em relação à implementação MariaDB são:

Uso do pacote mysql-connector ao invés de mariadb
Uso de %s como placeholder nas queries ao invés de ?
Algumas pequenas diferenças na configuração da conexão
'''


class MySQLUserRepository(UserRepository):
    def __init__(self):
        # Configuração da conexão
        self.config = {
            'host': 'localhost',
            'user': 'seu_usuario',
            'password': 'sua_senha',
            'database': 'seu_banco'
        }

    def get_connection(self):
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            raise Exception(f"Erro ao conectar ao MySQL: {e}")

    async def save(self, user: User) -> User:
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            if user.id:
                # Update
                query = """
                    UPDATE users
                    SET email = %s,
                        primeiro_nome = %s,
                        sobrenome = %s,
                        phone_number = %s,
                        profile = %s
                    WHERE id = %s
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
                    VALUES (%s, %s, %s, %s, %s)
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
            query = "SELECT * FROM users WHERE email = %s"
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