import flet as ft
from services.firebase_interface import signup_fb
from utils.field_validation_functions import validate_email, validate_password_strength, validate_phone


# https://github.com/webtechmoz/autenticator/blob/master/autenticador/main.py#L12


def Signup(page: ft.Page, plano: str = None):
    name_input = ft.TextField(
        hint_text='Nome completo',
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

    def show_error_message(message: str):
        snack_bar = ft.SnackBar(
            content=ft.Text(message),
            bgcolor=ft.colors.RED_100,
            show_close_icon=True,
            close_icon_color=ft.colors.RED,
            padding=ft.padding.all(10),
            duration=7000,
            behavior=ft.SnackBarBehavior.FLOATING,
            margin=ft.margin.all(10),
        )
        page.overlay.append(snack_bar)
        page.update()
        snack_bar.open = True  # Abre o SnackBar após adicioná-lo
        page.update()

    def show_success_message(message: str):
        snack_bar = ft.SnackBar(
            content=ft.Text(message),
            bgcolor=ft.colors.GREEN_400,
            duration=10000,
        )
        page.overlay.append(snack_bar)
        page.update()
        snack_bar.open = True  # Abre o SnackBar após adicioná-lo
        page.update()


    def validate_form() -> bool:
        """Valida todos os campos do formulário"""
        if not name_input.value or len(name_input.value.strip()) < 3:
            show_error_message("O nome deve ter pelo menos 3 caracteres")
            return False

        # Validação de email
        is_valid_email, email_msg = validate_email(email_input.value)
        if not is_valid_email:
            show_error_message(email_msg)
            return False

        # Validação de telefone
        is_valid_phone, phone_msg = validate_phone(phone_input.value)
        if not is_valid_phone:
            show_error_message(phone_msg)
            return False

        # Validação de senha
        is_valid_password, password_msg = validate_password_strength(
            password_input.value)
        if not is_valid_password:
            show_error_message(password_msg)
            return False

        # Validação de confirmação de senha
        if password_input.value != password_again_input.value:
            show_error_message("As senhas não coincidem")
            return False

        return True

    def on_click_registrar(e):
        if not validate_form():
            return

        try:
            # Chama a função de registro do Firebase
            result = signup_fb({
                'name': name_input.value,
                'email': email_input.value,
                'phone': phone_input.value,
                'password': password_input.value
            })

            if result:
                show_success_message("Registro realizado com sucesso!")
                page.go('/login')
            else:
                show_error_message(
                    "Erro ao realizar o registro. Tente novamente.")

        except Exception as e:
            print(f"Error: {str(e)}")
            show_error_message(f"Erro: {str(e)}")

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
