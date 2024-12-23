import flet as ft

# https://github.com/webtechmoz/autenticator/blob/master/autenticador/main.py#L12


def Signup(page: ft.Page, plano: str = None):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(value=f'Registro ({plano})', weight='bold',
                        size=20, color=ft.colors.BLACK),
                ft.Divider(height=1, color=ft.colors.with_opacity(
                    0.25, ft.colors.GREY), thickness=1),
                ft.Column(
                    controls=[
                        ft.TextField(
                            hint_text='Primeiro nome',
                            prefix_icon=ft.icons.PERSON,
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
                            )
                        ),
                        ft.TextField(
                            hint_text='Segundo nome',
                            prefix_icon=ft.icons.PERSON,
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
                            )
                        ),
                        ft.TextField(
                            hint_text='Segundo o seu email',
                            prefix_icon=ft.icons.EMAIL,
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
                            keyboard_type=ft.KeyboardType.EMAIL
                        ),
                        ft.TextField(
                            hint_text='Digite o seu telefone',
                            prefix_icon=ft.icons.PHONE,
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
                            keyboard_type=ft.KeyboardType.PHONE
                        ),
                        ft.TextField(
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
                        ),
                        ft.TextField(
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
                        ),
                        ft.ElevatedButton(
                            text='Register',
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE,
                            width=400,
                            height=40
                        )
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
