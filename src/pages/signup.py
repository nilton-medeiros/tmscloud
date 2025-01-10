import flet as ft
from src.controllers.user_controller import handle_save_user
from src.utils.field_validation_functions import get_first_and_last_name, validate_email, validate_password_strength, validate_phone
from src.utils.message_snackbar import message_snackbar


# https://github.com/webtechmoz/autenticator/blob/master/autenticador/main.py#L12


def Signup(page: ft.Page, plano: str = 'DFe-1000'):
    '''
    Função para criar uma página (container) de formulário de
    registro de novos usuários.

    Parâmetros:
        page (ft.Page): Página principal do app.
        plano (str): Plano de assinatura (padrão: 'DFe-1000').

    Retorna:
        ft.Container: Container com o formulário de registro.
    '''

    name_input = ft.TextField(
        hint_text='Nome e Sobrenome',
        prefix_icon=ft.icons.PERSON,
        text_vertical_align=-0.30,
        border=ft.InputBorder.UNDERLINE,
        border_width=2,
        border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
        hint_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
        ),
        text_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(
                0.9, ft.colors.BLACK)
        ),
        capitalization=ft.TextCapitalization.WORDS,
    )

    email_input = ft.TextField(
        hint_text='E-mail',
        prefix_icon=ft.icons.EMAIL,
        text_vertical_align=-0.30,
        border=ft.InputBorder.UNDERLINE,
        border_width=2,
        border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
        hint_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(0.4, ft.colors.BLACK)
        ),
        text_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(0.9, ft.colors.BLACK)
        ),
        keyboard_type=ft.KeyboardType.EMAIL
    )

    phone_input = ft.TextField(
        hint_text='Celular',
        prefix_icon=ft.icons.PHONE,
        text_vertical_align=-0.30,
        border=ft.InputBorder.UNDERLINE,
        border_width=2,
        border_color=ft.colors.with_opacity(0.4, ft.colors.BLACK),
        hint_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(
                0.4, ft.colors.BLACK)
        ),
        text_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(
                0.9, ft.colors.BLACK)
        ),
        keyboard_type=ft.KeyboardType.PHONE
    )

    password_input = ft.TextField(
        hint_text='Digite a sua senha',
        prefix_icon=ft.icons.LOCK,
        text_vertical_align=-0.30,
        border=ft.InputBorder.UNDERLINE,
        border_width=2,
        border_color=ft.colors.with_opacity(
            0.4, ft.colors.BLACK),
        hint_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(
                0.4, ft.colors.BLACK)
        ),
        text_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(
                0.9, ft.colors.BLACK)
        ),
        password=True,
        can_reveal_password=True
    )

    password_again_input = ft.TextField(
        hint_text='Digite a senha novamente',
        prefix_icon=ft.icons.LOCK,
        text_vertical_align=-0.30,
        border=ft.InputBorder.UNDERLINE,
        border_width=2,
        border_color=ft.colors.with_opacity(
            0.4, ft.colors.BLACK),
        hint_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(
                0.4, ft.colors.BLACK)
        ),
        text_style=ft.TextStyle(
            size=14,
            weight='bold',
            color=ft.colors.with_opacity(
                0.9, ft.colors.BLACK)
        ),
        password=True,
        can_reveal_password=True
    )

    def validate_form() -> bool:
        """Valida todos os campos do formulário"""
        if not name_input.value or len(name_input.value.strip()) < 3:
            message_snackbar(page, "O nome deve ter pelo menos 3 caracteres")
            return False

        # Validação de email
        is_valid_email, email_msg = validate_email(email_input.value)
        if not is_valid_email:
            message_snackbar(page, email_msg)
            return False

        # Validação de telefone
        is_valid_phone, phone_msg = validate_phone(phone_input.value)
        if not is_valid_phone:
            message_snackbar(page, phone_msg)
            return False

        # Validação de senha
        is_valid_password, password_msg = validate_password_strength(
            password_input.value)
        if not is_valid_password:
            message_snackbar(page, password_msg)
            return False

        # Validação de confirmação de senha
        if password_input.value != password_again_input.value:
            message_snackbar(page, "As senhas não coincidem")
            return False

        return True

    def on_click_registrar(e):
        '''Registra o novo usuário no banco após validação dos campos do formulário'''
        if not validate_form():
            return

        first_name, last_name = get_first_and_last_name(name_input.value)

        message, is_error = handle_save_user(
            email=email_input.value,
            first_name=first_name,
            last_name=last_name,
            phone=phone_input.value,
            password=password_input.value
        )

        message_snackbar(page, message, is_error)

        page.go('/home')

    signup_button = ft.ElevatedButton(
        text='Registrar',
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE,
        width=400,
        height=40,
        on_click=on_click_registrar,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(value=f'Registro ({plano})', weight='bold',
                        size=20, color=ft.colors.BLACK),
                ft.Divider(height=1, color=ft.colors.with_opacity(
                    0.25, ft.colors.GREY), thickness=1),
                ft.Column(
                    controls=[
                        name_input,
                        email_input,
                        phone_input,
                        password_input,
                        password_again_input,
                        signup_button,
                    ],
                    spacing=15,
                    alignment=ft.alignment.center,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.TextButton(
                            text='Já tenho uma conta',
                            on_click=lambda _: page.go('/login')
                        )
                    ],
                    alignment=ft.alignment.center,
                )
            ],
            spacing=10,
            alignment=ft.alignment.center,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        width=400,
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
    )
