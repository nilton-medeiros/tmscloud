# Exemplo de Código com Menu, Corpo Principal e Rodapé


import flet as ft


def main(page: ft.Page):
    page.title = "By Perplexity"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Menu Superior
    def on_signup_click(e):
        page.add(ft.SnackBar(ft.Text("Página de Inscrição"), open=True))

    def on_login_click(e):
        page.add(ft.SnackBar(ft.Text("Página de Login"), open=True))

    menu = ft.Row(
        [
            ft.ElevatedButton("Inscrever-se", on_click=on_signup_click),
            ft.ElevatedButton("Fazer Login", on_click=on_login_click),
        ],
        alignment=ft.MainAxisAlignment.END,
        spacing=20,
        # padding=10,
    )

    # Corpo Principal
    title = ft.Text("Bem-vindo à minha Landing Page!",
                    size=30, weight=ft.FontWeight.BOLD)
    description = ft.Text(
        "Aqui você pode encontrar informações sobre meu trabalho e projetos.", size=20)

    # Botão que exibe uma mensagem ao ser clicado
    def on_button_click(e):
        page.add(ft.SnackBar(ft.Text("Obrigado por visitar!"), open=True))

    main_content = ft.Column(
        [
            title,
            description,
            ft.ElevatedButton("Clique aqui", on_click=on_button_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        # padding=20,
    )

    # Rodapé
    footer = ft.Text(
        "© 2024 Minha Empresa. Todos os direitos reservados.", size=12, color="grey")

    # Adicionando os componentes à página
    page.add(menu, main_content, footer)


ft.app(target=main)
