import flet as ft
from services.firebase_interface import signup_fb
from utils.field_validation_functions import validate_email, validate_password_strength, validate_phone
from utils.message_snackbar import message_snackbar


# https://github.com/webtechmoz/autenticator/blob/master/autenticador/main.py#L12


def Signup(page: ft.Page, plano: str = None):
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
        if not validate_form():
            return

        try:
            # Decidir se cria o objeto User aqui e valida pelo objeto ou usa validação do formulário desta página: validate_form()
            # Chama a função de registro do Firebase
            user = {
                'email': email_input.value,
                'display_name': name_input.value.strip(),
                'phone_number': phone_input.value,
                'password': password_input.value,
                'profile': "admin"
            }
            result = signup_fb(user)

            # Debug
            print(" ")
            print(f"Type de result: {type(result)}")
            print(f"Result: {result}")

            # Atualiza o nome do usuário na tela principal
            # app.current_user = result['name']  # Assumindo que o nome é o 'name' do Firebase

            # Atualiza o nome do usuário na barra de navegação
            # app.navigation_bar.title = f'Bem-vindo, {result["name"]}'  # Assumindo que o nome é o 'name' do Firebase

            # Atualiza a imagem do usuário na barra de navegação
            # app.navigation_bar.icon = ft.Image(
            #     source=get_user_icon(result['email']),
            #     width=24,
            #     height=24,
            # )  # Assumindo que o email é usado para buscar a imagem do Firebase

            # Atualiza a lista de contatos na tela principal

            # Verifica se o resultado é um erro ou o objeto do usuário
            if f"{result}" == "The user with the provided email already exists (EMAIL_EXISTS).":
                message_snackbar(
                    page, "Erro ao registrar: O usuário com o e-mail fornecido já existe!")
            else:
                message_snackbar(
                    page=page,
                    message="Registro realizado com sucesso!",
                    msg_error=False
                )

                page.go('/home')

        except Exception as e:
            print(f"Error: {str(e)}")
            message_snackbar(page, f"Erro inesperado: {str(e)}")

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
