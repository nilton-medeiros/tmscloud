import flet as ft


def main(page: ft.Page):
    page.title = "By ChatGPT"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.BLUE_GREY_900

    # Menu Superior
    def on_signup_click(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Inscrição"),
            content=ft.Text("Página de inscrição ainda em desenvolvimento."),
            on_dismiss=lambda e: page.update()
        )
        page.open(dlg)
        page.update()

    def on_login_click(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Login"),
            content=ft.Text("Página de login ainda em desenvolvimento."),
            on_dismiss=lambda e: page.update()
        )
        page.open(dlg)
        page.update()

    menu = ft.AppBar(
        title=ft.Text("Inspiração Digital", color=ft.colors.WHITE),
        center_title=False,
        bgcolor=ft.colors.BLUE_GREY_800,
        actions=[
            ft.TextButton("Inscrever-se", on_click=on_signup_click),
            ft.TextButton("Login", on_click=on_login_click),
        ],
    )

    # Corpo Principal
    title = ft.Text(
        "Bem-vindo ao Inspiração Digital!",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    subtitle = ft.Text(
        "Descubra o poder da tecnologia e inspire-se para o futuro.",
        size=18,
        color=ft.colors.GREY_300,
        text_align=ft.TextAlign.CENTER,
    )

    # Imagem (URL de exemplo)
    image = ft.Image(
        # src="https://1drv.ms/i/s!Arw7KAe8DRzRlOgzY81X2Fc5XvR-ww?e=RZmpcJ",  # Substitua pela URL da sua imagem
        src="images/lobo.jpg",  # Substitua pela URL da sua imagem
        # width=750,
        # height=300,
        # fit=ft.ImageFit.CONTAIN,
    )

    # Botão de CTA no Corpo Principal
    def on_cta_click(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Obrigado!"),
            content=ft.Text("Você se registrou com sucesso!"),
            on_dismiss=lambda e: page.update()
        )
        page.open(dlg)
        page.update()

    cta_button = ft.ElevatedButton(
        "Registre-se Agora",
        bgcolor=ft.colors.GREEN_500,
        color=ft.colors.WHITE,
        on_click=on_cta_click,
    )

    main_content = ft.Column(
        [
            title,
            subtitle,
            image,
            cta_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    # Rodapé
    footer = ft.Container(
        content=ft.Text(
            "© 2024 Inspiração Digital. Todos os direitos reservados.",
            color=ft.colors.GREY_400,
            size=12,
            text_align=ft.TextAlign.CENTER,
        ),
        padding=10,
        bgcolor=ft.colors.BLUE_GREY_800,
        alignment=ft.alignment.center,
    )

    # Layout da página
    page.add(
        menu,
        ft.Container(
            content=main_content,
            expand=True,
            alignment=ft.alignment.center,
        ),
        footer,
    )


# Executa o app
ft.app(target=main, assets_dir="assets")
