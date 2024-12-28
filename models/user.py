from typing import Optional
from dataclasses import dataclass, field

from models.nome_pessoa import NomePessoa
from models.phone_number import PhoneNumber


@dataclass
class User:
    id: Optional[str] = field(default=None)
    email: str
    display_name: NomePessoa
    phone_number: PhoneNumber
    profile: str

    # Lista de perfis permitidos
    ALLOWED_PROFILES = {"admin", "emissor", "atendente", "financeiro",
                        "cobrança", "pagamento", "representante", "cliente"}

    def __post_init__(self):
        # Validação do campo 'id'
        if not self.id:
            raise ValueError("O campo 'id' é obrigatório.")

        # Validação do campo 'display_name'
        if not self.display_name.primeiro_nome():
            raise ValueError("O campo 'display_name' é obrigatório.")

        # Validação do campo 'email'
        self.email = self.email.strip()
        if not self.email or "@" not in self.email:
            raise ValueError("O campo 'email' deve ser válido.")

        # Validação do campo 'profile'
        if self.profile not in self.ALLOWED_PROFILES:
            raise ValueError(
                f"O perfil '{self.profile}' não é permitido. Perfis permitidos: {', '.join(self.ALLOWED_PROFILES)}.")


# Exemplo de uso
'''
# INSERT: Criando um novo usuário (sem id ainda) com validações
try:
    user = User(
        email="email@example.com",
        display_name=NomePessoa("Nome", "Sobrenome"),
        phone_number=PhoneNumber("+5511999999999"),
        profile="admin"  # Obrigatório e válido
    )
except ValueError as e:
    print("Erro:", e)

# UPDATE: Atualizando um usuário já existente (com id já fornecido)
user.id = "12345"
user.email = "novo_email@example.com"
user.display_name = NomePessoa("Novo", "Nome")
user.phone_number = PhoneNumber("+5511888888888")
user.profile = "financeiro"  # Obrigatório e válido
'''