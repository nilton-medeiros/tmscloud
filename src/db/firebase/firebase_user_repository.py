# db/firebase/firebase_user_repository.py
from firebase_admin import auth
from firebase_admin import firestore
from firebase_admin import exceptions

from src.domain.models.user import User
from src.domain.models.nome_pessoa import NomePessoa
from src.domain.models.phone_number import PhoneNumber
from src.db.interfaces.user_repository import UserRepository
from src.utils.deep_translator import deepl_translator
from src.utils.field_validation_functions import get_first_and_last_name


class FirebaseUserRepository(UserRepository):
    '''
    Firebase user repository:
    Utiliza Google Authorization para autenticar e salvar os dados dos usuários.
    Nota: Esta classe Herda da classe abstrata UserRepository as especificações para
    implementar todos os métodos em conformidade com UserRepository.

    Args:
        password (str): Senha do usuário no Google Authorization
        db (firestore.Client): Objeto do Firestore

    Methods:
        save: Salva usuário no Google Authorization e no Firestore (inclui ou altera)
        find_by_id: Busca um usuário pelo id
        find_by_email: Busca um usuário pelo email
        find_all: Busca todos os usuários da empresa logada
        find_by_profile: Busca um usuários por perfil
        delete: Deleta um usuário do Firestore e do Google Authorization
        count: Retorna o número total de usuários da empresa logada
        exists_by_email: Verifica se existe um usuário com o email especificado
        update_profile: Atualiza o perfil de um usuário
        find_by_name: Busca usuários da empresa logada que contenham o nome especificado

    deepl_translator: Traduz os erros em inglês recebidos do Firebase para o português brasil
    '''

    def __init__(self, password: str):
        self.db = firestore.client()
        self.collection = self.db.collection('users')
        self.password = None

        if password is not None and password != "":
            self.password = password

    async def save(self, user: User) -> User:
        try:
            # Converte o objeto User para um dicionário que o Firestore aceita
            user_dict = {
                'email': user.email,
                'display_name': user.display_name.nome_completo,
                'phone_number': user.phone_number.get_e164(),
                'profile': user.profile
            }

            if user.id:
                # Update
                self.collection.document(user.id).set(user_dict)
            else:
                # 1. Criar usuário no Firebase Authentication
                user_db = auth.create_user(
                    email=user.email,
                    password=self.password,
                    display_name=user.display_name.nome_completo,
                    phone_number=user.phone_number.get_e164()
                )

                # 2. Cria usuário no Firestore
                user.id = user_db.uid
                doc_ref = self.db.collection('users').document(user.id)
                doc_ref.set(user_dict)

            return user
        except exceptions.FirebaseError as e:
            translated_error = deepl_translator(str(e))
            raise Exception(f"Erro ao salvar usuário: {translated_error}")
        except Exception as e:
            raise Exception(f"Erro inesperado ao salvar usuário: {str(e)}")

    async def find_by_email(self, email: str) -> User:
        try:
            query = self.collection.where('email', '==', email).limit(1)
            docs = query.stream()

            for doc in docs:
                data = doc.to_dict()
                full_name = get_first_and_last_name(data['display_name'])
                return User(
                    id=doc.id,
                    email=data['email'],
                    display_name=NomePessoa(full_name),
                    phone_number=PhoneNumber(data['phone_number']),
                    profile=data['profile']
                )
            return None
        except exceptions.FirebaseError as e:
            translated_error = deepl_translator(str(e))
            raise Exception(
                f"Erro ao buscar usuário pelo email '{email}': {translated_error}")
        except Exception as e:
            raise Exception(
                f"Erro inesperado ao buscar usuário pelo email '{email}': {str(e)}")

    async def delete(self, user_id: str) -> None:
        """
        Deleta um usuário do Firestore e do Firebase Authentication.
        """
        try:
            # Deleta do Firebase Authentication
            auth.delete_user(user_id)
            # Deleta do Firestore
            self.collection.document(user_id).delete()
        except exceptions.FirebaseError as e:
            translated_error = deepl_translator(str(e))
            raise Exception(
                f"Erro ao deletar usuário com ID '{user_id}': {translated_error}")
        except Exception as e:
            raise Exception(
                f"Erro inesperado ao deletar usuário com ID '{user_id}': {str(e)}")

    async def find_by_id(self, user_id: str) -> User:
        """
        Busca um usuário pelo ID no Firestore.
        """
        try:
            doc = self.collection.document(user_id).get()
            if doc.exists:
                data = doc.to_dict()
                full_name = get_first_and_last_name(data['display_name'])
                return User(
                    id=user_id,
                    email=data['email'],
                    display_name=NomePessoa(full_name),
                    phone_number=PhoneNumber(data['phone_number']),
                    profile=data['profile']
                )
            return None
        except exceptions.FirebaseError as e:
            translated_error = deepl_translator(str(e))
            raise Exception(
                f"Erro ao buscar usuário com ID '{user_id}': {translated_error}")
        except Exception as e:
            raise Exception(
                f"Erro inesperado ao buscar usuário com ID '{user_id}': {str(e)}")
