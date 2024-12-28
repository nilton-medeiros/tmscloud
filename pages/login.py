import flet as ft


def Login(page: ft.Page):
    return ft.Container(
        bgcolor='amber',
        height=300,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('Login em construção!', size=40, color=ft.colors.WHITE),
                ft.ElevatedButton(
                    text="Voltar para Landing-Page",
                    color=ft.colors.WHITE,
                    on_click=lambda _: page.go('/')
                )
            ],
            spacing=20,
            alignment=ft.alignment.center,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        )
    )
