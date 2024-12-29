from src.db.firebase.firebase_user_repository import FirebaseUserRepository
from src.domain.models.nome_pessoa import NomePessoa
from src.domain.models.phone_number import PhoneNumber
from src.domain.models.user import User
from src.services.user_service import UserService


async def handle_save_user(email, first_name, last_name, phone, profile, password):
  '''
  handle_save_user: Manipula a operação salvar usuário (Controller)
  Salva um novo usuário ou altera se existir no Firebase Firestore

  Parâmetros:
    email: (str)
    first_name: (str)
    last_name: (str)
    phone: (str)

    profile: (str) Lista de perfis permitidos:
      {"admin", "emissor", "atendente", "financeiro", "cobrança", "pagamento", "representante", "cliente"}
    password: (str) A criptografia fica por conta do Google Authorization (Firebase),
      se mudar para outro banco de dados, usar src/utils/encrypt_password.py em 'outro_banco_user_repository.py'

    Retorno: Tupla (str, bool) Mensagem de sucesso ou erro, True ou False para error
  '''
  try:
      # Cria o objeto User com os dados do formulário
      user = User(
          id=None,
          email=email,
          display_name=NomePessoa(first_name, last_name),
          phone_number=PhoneNumber(phone),
          profile=profile
      )

      # Inicializa o repositório e o service
      # Firebase Firestore é usado como repositório padrão
      # Se mudar para outro banco de dados, usar src/db/OutroBancoUserRepository.py
      # e alterar src/services/user_service.py para usar o novo repositório e service apropriado
      repository = FirebaseUserRepository(password)
      user_service = UserService(repository)

      # Salva o usuário
      saved_user = await user_service.create_user(user)
      return f"Usuário salvo com sucesso. ID: {saved_user.id}", False

  except ValueError as e:
      return f"Erro de validação: {str(e)}", True
  except Exception as e:
      return f"Erro ao salvar usuário: {str(e)}", True
