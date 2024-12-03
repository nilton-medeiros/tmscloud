import flet as ft


class MainContentItem():
    def __init__(self, title: str, description: str, image: str, image_left=True):
        self.title = title
        self.description = description
        self.image_left = image_left
        self.image = ft.Image(
            src=image,
            # width=750,
            # height=300,
            # fit=ft.ImageFit.CONTAIN,
        )

    def build(self):
        description = ft.Column(
            controls=[
                ft.Text(value=self.title,
                        theme_style=ft.TextThemeStyle.TITLE_LARGE),
                ft.Text(value=self.description,
                        theme_style=ft.TextThemeStyle.TITLE_SMALL),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        image_ctnr = ft.Container(
            content=self.image,
            col={"md": 5},
            alignment=ft.alignment.center
        )
        descr_ctnr = ft.Container(
            content=description,
            col={"md": 7},
            alignment=ft.alignment.center
        )

        side_left = image_ctnr if self.image_left else descr_ctnr
        side_right = descr_ctnr if self.image_left else image_ctnr
        bgcolor = ft.colors.BLUE_GREY_700 if self.image_left else ft.colors.BLUE_GREY_800

        return ft.Container(
            content=ft.ResponsiveRow(
                controls=[side_left, side_right],
                spacing=20,
                # run_spacing={"xs": 10},
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(top=40),
            bgcolor=bgcolor,
            padding=20,
            border_radius=10,
            alignment=ft.alignment.center,
        )


class LandingPage():
    def __init__(self, page: ft.Page):
        self.page = page
        self.title_bar = ft.Text(
            value="TMS.CLOUD   Gerenciamento de Transporte e logística",
            color=ft.colors.WHITE,
        )

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

            # Debug
            # print(f"Width: {width}")

            self.title_bar.value = "TMS.CLOUD   Gerenciamento de Transporte e logística"

            self.actions_button.clear()
            self.actions_button.extend([
                ft.TextButton(
                    text="Inscrever-se",
                    style=ft.ButtonStyle(color=ft.colors.WHITE),
                    on_click=on_signup_click,
                ),
                ft.TextButton(
                    text="Login",
                    style=ft.ButtonStyle(color=ft.colors.WHITE),
                    on_click=on_login_click,
                ),
            ])

            if width < 600:         # xs
                self.title_bar.size = 14
                self.title_bar.max_lines = 3

                if width < 570:
                    self.title_bar.size = 12
                    if width < 500:
                        self.title_bar.value = "TMS.CLOUD" if width >= 435 else "TMS"
                        if width < 385:
                            self.actions_button.pop(0)
                            # self.actions_button.clear()
                            # self.actions_button.append(
                            #     ft.TextButton(
                            #         text="Login",
                            #         style=ft.ButtonStyle(
                            #             color=ft.colors.WHITE),
                            #         on_click=on_login_click,
                            #     ),
                            # )
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
            ft.TextButton(
                text="Inscrever-se",
                style=ft.ButtonStyle(color=ft.colors.WHITE),
                on_click=on_signup_click,
            ),
            ft.TextButton(
                text="Login",
                style=ft.ButtonStyle(color=ft.colors.WHITE),
                on_click=on_login_click,
            ),
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
            controls=[
                title,
                subtitle,
                MainContentItem(
                    title="Transforme sua Gestão de Transporte com TMS.CLOUD",
                    description="O TMS.CLOUD é a solução completa para o gerenciamento de transporte e logística. Automatize processos, controle suas operações em tempo real e reduza custos com uma plataforma intuitiva e eficiente. Leve a gestão do seu transporte de cargas para o próximo nível.",
                    image="images/lobo.jpg",
                    image_left=True,
                ).build(),
                MainContentItem(
                    title="Emita CTe 4.0 com Facilidade",
                    description="Simplifique a emissão do CT-e 4.0 diretamente no TMS.CLOUD. Garanta conformidade com a legislação, reduza erros e ganhe agilidade no transporte de carga. Tudo integrado e automatizado para otimizar suas operações.",
                    image="images/lobo.jpg",
                    image_left=False
                ).build(),
                MainContentItem(
                    title="Gerencie seus MDFe's",
                    description="Emita e gerencie MDF-e de forma rápida e segura. O TMS.CLOUD facilita o controle de cargas em trânsito, centraliza informações e garante a conformidade com a legislação fiscal. Otimize suas rotas e operações.",
                    image="images/lobo.jpg",
                    image_left=True
                ).build(),
                MainContentItem(
                    title="Controle Total do Faturamento dos CT-es Emitidos",
                    description="Gere e acompanhe o faturamento dos seus CT-es com o TMS.CLOUD. Tenha relatórios precisos, automatize cobranças e otimize a gestão financeira da sua empresa. Mais controle, menos burocracia.",
                    image="images/lobo.jpg",
                    image_left=False
                ).build(),
                register_button,
            ],
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
