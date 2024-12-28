from firebase_admin import auth
from firebase_admin import firestore
from firebase_admin import exceptions

from services.firebase_initialize import get_firebase_app
from utils.field_validation_functions import format_phone_number


# Conecta ao Firebase admin
firebase_app = get_firebase_app()


# Registra usuário no Google Authentication
def signup_fb(user_data: dict):

    try:
        # Formatar o número de telefone para o padrão E.164
        formatted_phone = format_phone_number(user_data['phone_number'])

        # Criar usuário no Firebase Authentication
        user = auth.create_user(
            email=user_data['email'],
            password=user_data['password'],
            display_name=user_data['name'],
            phone_number=formatted_phone
        )

        user_uid = user.uid
        user_data['uid'] = user_uid
        user_data['phone_number'] = formatted_phone

        # Inicializa o cliente do Firestore
        db = firestore.client()

        # Adicione o usuário à coleção `users`
        doc_ref = db.collection('users').document(user_uid)
        doc_ref.set(user_data)

        return user_data
    except exceptions.FirebaseError as error:
        print(f"Erro de autenticação: {error}")
        return error



def login_fb(email: str, password: str):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Usuário logado com sucesso:", user.uid)
        # Aqui você pode redirecionar o usuário para outra página ou mostrar uma mensagem de sucesso
        return user
    except auth.AuthError as error:
        print(f"Erro de autenticação: {error}")
        # Exibir uma mensagem de erro para o usuário
        return None
