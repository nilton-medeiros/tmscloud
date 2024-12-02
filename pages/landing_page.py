import flet as ft


class LandingPage():
    def __init__(self, page: ft.Page):
        self.page = page
        self.title_bar = ft.Text(
            "TMS.CLOUD Gerenciamento de Transporte e logística", color=ft.colors.WHITE)

    def build(self):
        def on_signup_click(e):
            dlg = ft.AlertDialog(
                title=ft.Text("Inscrição"),
                content=ft.Text(
                    "Página de inscrição ainda em desenvolvimento."),
                on_dismiss=lambda e: self.page.update()
            )
            self.page.open(dlg)

        def on_login_click(e):
            dlg = ft.AlertDialog(
                title=ft.Text("Login"),
                content=ft.Text("Página de login ainda em desenvolvimento."),
                on_dismiss=lambda e: self.page.update()
            )
            self.page.open(dlg)

        def update_text_size():
            # Ajusta o tamanho do texto com base na largura da tela
            width = self.page.width

            self.title_bar.value = "TMS.CLOUD Gerenciamento de Transporte e logística"

            self.actions_button.clear()
            self.actions_button.extend([
                ft.TextButton("Inscrever-se", on_click=on_signup_click),
                ft.TextButton("Login", on_click=on_login_click),
            ])

            if width < 600:         # xs
                self.title_bar.size = 14
                self.title_bar.max_lines = 3

                if width < 500:
                    self.title_bar.size = 12
                if width < 450:
                    self.title_bar.value = "TMS.CLOUD"
                    if width < 390:
                        self.actions_button.clear()
                        self.actions_button.append(ft.TextButton(
                            "Login", on_click=self.on_login_click))
            elif width < 900:       # sm
                self.title_bar.size = 16
            elif width < 1200:      # md
                self.title_bar.size = 18
            elif width < 1500:      # lg
                self.title_bar.size = 22
            else:                   # xl
                self.title_bar.size = 24

            self.page.update()

        self.actions_button = [
            ft.TextButton("Inscrever-se", on_click=on_signup_click),
            ft.TextButton("Login", on_click=on_login_click),
        ]

        # Menu AppBar
        self.page.appbar = ft.AppBar(
            leading=ft.Image(
                src='images/tms_cloud_2048x1024-white.png',
                tooltip="TMS.CLOUD | Sistrom Web",
            ),
            # Largura do image em leanding, altura não pode ser alterada.
            leading_width=120,
            title=self.title_bar,
            center_title=False,
            bgcolor=ft.colors.BLUE_GREY_800,
            actions=self.actions_button,
        )

        # Corpo Principal
        title = ft.Text(
            "Bem-vindo ao Tms.Cloud!",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        )

        subtitle = ft.Text(
            "Otimize sua logística, reduza custos e entregue mais rápido com o nosso TMS.",
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

        def on_register_click(e):
            dlg = ft.AlertDialog(
                title=ft.Text("Obrigado!"),
                content=ft.Text("Você se registrou com sucesso!"),
                on_dismiss=lambda e: self.page.update()
            )
            self.page.open(dlg)

        register_button = ft.ElevatedButton(
            "Registre-se Agora",
            bgcolor=ft.colors.GREEN_500,
            color=ft.colors.WHITE,
            on_click=on_register_click,
        )

        main_content = ft.Column(
            [
                title,
                subtitle,
                image,
                register_button,
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

        self.page.on_resized = lambda _: update_text_size()
        update_text_size()

        return [
            ft.Container(
                content=main_content,
                width=1400,
                expand=True,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_GREY_900,
                padding=20,
            ),
            ft.Container(
                content=footer,
                # width=1400,
                alignment=ft.alignment.center,
            )
        ]
