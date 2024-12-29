import re
from typing import Tuple


def validate_password_strength(password: str) -> Tuple[bool, str]:
    """
    Valida a força da senha seguindo critérios de segurança.
    Retorna uma tupla (is_valid, message)
    """
    if len(password) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres"

    checks = [
        (r'[A-Z]', "pelo menos uma letra maiúscula"),
        (r'[a-z]', "pelo menos uma letra minúscula"),
        (r'[0-9]', "pelo menos um número"),
        (r'[!@#$%^&*(),.?":{}|<>]', "pelo menos um caractere especial")
    ]

    failed_checks = [msg for pattern,
                     msg in checks if not re.search(pattern, password)]

    if failed_checks:
        return False, "A senha deve conter " + ", ".join(failed_checks)

    return True, "Senha forte"


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Valida o formato do email usando regex.
    Retorna uma tupla (is_valid, message)
    """
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        return False, "O email é obrigatório"
    if not re.match(email_pattern, email):
        return False, "Formato de email inválido"
    return True, "Email válido"


def format_phone_number(phone: str) -> str:
    """
    Formata o número de telefone para o padrão E.164.
    """
    # Remove todos os caracteres não numéricos
    phone = re.sub(r'\D', '', phone)
    # phone = ''.join(filter(str.isdigit, phone)) // Outra forma de remover caracteres

    # Adiciona o código do país (+55 para Brasil) se não estiver presente
    if not phone.startswith('55'):
        phone = '55' + phone

    # Retorna o número formatado no padrão E.164
    return f"+{phone}"


def validate_phone(phone: str) -> Tuple[bool, str]:
    """
    Valida o número de telefone.
    Retorna uma tupla (is_valid, message)
    """
    # Remove todos os caracteres não numéricos para a validação
    numbers = re.sub(r'\D', '', phone)
    # numbers = ''.join(filter(str.isdigit, phone)) // Outra forma de remover caracteres

    if not numbers:
        return False, "O telefone é obrigatório"

    if len(numbers) < 10:
        return False, "O telefone deve ter pelo menos 10 dígitos"

    if len(numbers) > 11:
        return False, "O telefone não pode ter mais de 11 dígitos"

    if len(numbers) == 11 and numbers[2] not in '9678':
        return False, "Celular inválido (deve começar com 9)"

    dispositivo = 'Celular' if len(numbers) == 11 and numbers[2] in '9678' else 'Telefone'
    return True, f"{dispositivo} válido"


def get_first_and_last_name(full_name: str) -> Tuple[str, str | None]:
    """
    Extrai o primeiro e o último nome de uma string de nome completo.

    Parametrôs:
        full_name (str): Nome e/ou sobrenome do usuário.
    Retorna uma tupla (primeiro_nome, ultimo_nome).
    """
    list_names = full_name.split()
    first_name = list_names[0].strip().capitalize()
    last_name = list_names[-1].strip().capitalize() if len(list_names) > 1 else None

    return first_name, last_name
