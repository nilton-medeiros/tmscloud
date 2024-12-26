import os
import firebase_admin
from firebase_admin import credentials

# Obtém o caminho absoluto para o arquivo de credenciais
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'serviceAccountKey.json')

# Inicializa o aplicativo Firebase apenas se ainda não estiver inicializado
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)
        print("Firebase inicializado com sucesso!")
    except FileNotFoundError:
        print(f"Erro: Arquivo de credenciais não encontrado em {CREDENTIALS_PATH}")
