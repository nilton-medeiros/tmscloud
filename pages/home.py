import flet as ft


def HomePage(page: ft.Page):
    return ft.Container(
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Text('HomePage em construção!',
                        size=40, color=ft.colors.WHITE),
                ft.ElevatedButton(
                    text="Voltar para LandingPage",
                    color=ft.colors.WHITE,
                    on_click=lambda _: page.go('/')
                )
            ],
            spacing=20,
            alignment=ft.alignment.center,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
