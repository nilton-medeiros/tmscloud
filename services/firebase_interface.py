import os
import firebase_admin
from firebase_admin import auth, credentials, exceptions

from utils.field_validation_functions import format_phone_number

# Obtém o caminho absoluto para o arquivo de credenciais
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'serviceAccountKey.json')

# Inicializa o aplicativo Firebase apenas se ainda não estiver inicializado
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)
        print(" ")
        print("INTERFACE: Firebase inicializado com sucesso!")
        print(" ")
    except FileNotFoundError:
        print(f"INTERFACE: Erro: Arquivo de credenciais não encontrado em {CREDENTIALS_PATH}")

def signup_fb(user_data: dict):

    # Verifica se o Firebase SDK foi inicializado
    print(" ")
    print("Firebase inicializado:", firebase_admin._apps)
    print(" ")

    try:
        # Formatar o número de telefone para o padrão E.164
        formatted_phone = format_phone_number(user_data['phone'])

        # Criar usuário no Firebase Authentication
        user = auth.create_user(
            email=user_data['email'],
            password=user_data['password'],
            display_name=user_data['name'],
            phone_number=formatted_phone
        )

        # Aqui você pode adicionar mais lógica, como salvar dados adicionais
        # no Firestore ou Realtime Database

        return user
    except exceptions.FirebaseError as error:
        print(f"Erro de autenticação: {error}")
        return None



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
