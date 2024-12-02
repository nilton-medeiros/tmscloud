import flet as ft


def main(page: ft.Page):
    # Título da página
    page.title = "By Gemini"

    # Barra de navegação
    nav_bar = ft.AppBar(
        title=ft.Text("Meu Aplicativo"),
        center_title=True,
        actions=[
            ft.TextButton("Inscrever-se"),
            ft.TextButton("Login"),
        ]
    )

    # Conteúdo principal
    content = ft.Column([
        ft.Text("Bem-vindo à minha landing page!", size=20),
        ft.Text(
            "Este é um exemplo simples de como criar uma página de destino com Flet."),
        ft.Image(src="https://picsum.photos/id/237/800/600",
                 fit=ft.ImageFit.CONTAIN),
    ])

    # Rodapé
    footer = ft.Container(
        content=ft.Text("Todos os direitos reservados."),
        alignment="center",
    )

    # Organizando a página
    page.add(
        nav_bar,
        content,
        footer
    )


ft.app(target=main)
