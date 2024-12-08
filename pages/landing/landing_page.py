import math
import flet as ft
from typing import List, Dict, Union

from pages.landing.landing_itens import MainContentItem


class PriceItem(ft.UserControl):
    def __init__(self, plano: str, price: int, items_included: List[Dict[str, Union[str, bool]]], col: Dict):
        super().__init__()
        self.plano = plano
        self.price = price
        self.items_included = items_included
        self.url = ''
        self.col = col

    def build(self):
        price_text = f' {self.price} ' if self.price > 0 else "CONSULTE"
        pormes_text = '/mês' if self.price > 0 else "-NOS"
        btn_plano = 'QUERO ESTE' if self.price > 0 else "CONSULTAR"

        return ft.Container(
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            padding=ft.padding.symmetric(vertical=20, horizontal=50),
            col=self.col,
            border_radius=10,
            expand=True,
            # margin=ft.margin.only(top=20, left=20),
            margin=ft.margin.all(20),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
                controls=[
                    ft.Text(value=self.plano,
                            theme_style=ft.TextThemeStyle.LABEL_LARGE),
                    ft.Text(
                        spans=[
                            ft.TextSpan(text='R$', style=ft.TextStyle(
                                color=ft.colors.WHITE)),
                            ft.TextSpan(text=price_text, style=ft.TextStyle(
                                color=ft.colors.PRIMARY, weight=ft.FontWeight.BOLD, size=50)),
                            ft.TextSpan(text=pormes_text, style=ft.TextStyle(
                                color=ft.colors.WHITE)),
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.CHECK if item['is_included'] else ft.icons.CLOSE,
                                        color=ft.colors.PRIMARY,
                                    ),
                                    ft.Text(
                                        value=item['title'], theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ) for item in self.items_included
                        ]
                    ),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value=btn_plano, theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.colors.PRIMARY),
                                ft.Icon(name=ft.icons.ARROW_FORWARD_IOS,
                                        size=14, color=ft.colors.PRIMARY),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        url=self.url,
                    )
                ]
            )
        )


class PriceItemPopular(PriceItem):
    def build(self):
        price_item = super().build()

        return ft.Stack(
            controls=[
                price_item,
                ft.Container(
                    bgcolor=ft.colors.PRIMARY,
                    content=ft.Text(
                        value='Popular', color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    padding=ft.padding.symmetric(vertical=5, horizontal=40),
                    right=-20,
                    top=50,
                    rotate=ft.Rotate(angle=math.radians(40)),
                )
            ]
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
                src='images/tms_cloud_1024x1024.png',
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


        prices = ft.Container(
            padding=20,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=10,
            margin=ft.margin.only(top=40),
            alignment=ft.alignment.center,
            expand=True,
            content=ft.ResponsiveRow(
                columns=12,
                spacing=30,
                run_spacing=30,
                expand=True,
                controls=[
                    PriceItem(
                        plano='DFe-100',
                        price=45,
                        items_included=[
                            {"title": "100 Emissões/mês", "is_included": True},
                            {"title": "Suporte ilimitado", "is_included": False},
                            {"title": "Compatível A1", "is_included": True},
                            {"title": "Armazenamento ilimitado", "is_included": False},
                            {"title": "Usuários ilimitados", "is_included": False},
                            {"title": "Emissão de CTe 4.0", "is_included": True},
                            {"title": "Emissão de MDFe", "is_included": True},
                            {"title": "Por emitente (CNPJ)", "is_included": True},
                        ],
                        col={'xs': 12, 'lg': 4},
                    ),
                    PriceItem(
                        plano='DFe-200',
                        price=90,
                        items_included=[
                            {"title": "200 Emissões/mês", "is_included": True},
                            {"title": "Suporte ilimitado", "is_included": False},
                            {"title": "Compatível A1", "is_included": True},
                            {"title": "Armazenamento ilimitado", "is_included": False},
                            {"title": "Usuários ilimitados", "is_included": False},
                            {"title": "Emissão de CTe 4.0", "is_included": True},
                            {"title": "Emissão de MDFe", "is_included": True},
                            {"title": "Por emitente (CNPJ)", "is_included": True},
                        ],
                        col={'xs': 12, 'lg': 4},
                    ),
                    PriceItem(
                        plano='DFe-300',
                        price=135,
                        items_included=[
                            {"title": "300 Emissões/mês", "is_included": True},
                            {"title": "Suporte ilimitado", "is_included": False},
                            {"title": "Compatível A1", "is_included": True},
                            {"title": "Armazenamento ilimitado", "is_included": False},
                            {"title": "Usuários ilimitados", "is_included": False},
                            {"title": "Emissão de CTe 4.0", "is_included": True},
                            {"title": "Emissão de MDFe", "is_included": True},
                            {"title": "Por emitente (CNPJ)", "is_included": True},
                        ],
                        col={'xs': 12, 'lg': 4},
                    ),
                    PriceItem(
                        plano='DFe-500',
                        price=225,
                        items_included=[
                            {"title": "500 Emissões/mês", "is_included": True},
                            {"title": "Suporte ilimitado", "is_included": False},
                            {"title": "Compatível A1", "is_included": True},
                            {"title": "Armazenamento ilimitado", "is_included": False},
                            {"title": "Usuários ilimitados", "is_included": False},
                            {"title": "Emissão de CTe 4.0", "is_included": True},
                            {"title": "Emissão de MDFe", "is_included": True},
                            {"title": "Por emitente (CNPJ)", "is_included": True},
                        ],
                        col={'xs': 12, 'lg': 4},
                    ),
                    PriceItemPopular(
                        plano='DFe-1000',
                        price=450,
                        items_included=[
                            {"title": "1000 Emissões/mês", "is_included": True},
                            {"title": "Suporte ilimitado", "is_included": True},
                            {"title": "Compatível A1", "is_included": True},
                            {"title": "Armazenamento ilimitado", "is_included": True},
                            {"title": "Usuários ilimitados", "is_included": True},
                            {"title": "Emissão de CTe 4.0", "is_included": True},
                            {"title": "Emissão de MDFe", "is_included": True},
                            {"title": "Por emitente (CNPJ)", "is_included": True},
                        ],
                        col={'xs': 12, 'lg': 4},
                    ),
                    PriceItem(
                        plano='DFe-2000',
                        price=750,
                        items_included=[
                            {"title": "2000 Emissões/mês", "is_included": True},
                            {"title": "Suporte ilimitado", "is_included": True},
                            {"title": "Compatível A1", "is_included": True},
                            {"title": "Armazenamento ilimitado", "is_included": True},
                            {"title": "Usuários ilimitados", "is_included": True},
                            {"title": "Emissão de CTe 4.0", "is_included": True},
                            {"title": "Emissão de MDFe", "is_included": True},
                            {"title": "Por emitente (CNPJ)", "is_included": True},
                        ],
                        col={'xs': 12, 'lg': 4},
                    ),
                    PriceItem(
                        plano='DFe-PLUS',
                        price=0,
                        items_included=[
                            {"title": "Acima de 2000 Emissões/mês", "is_included": True},
                            {"title": "Consulte para preços especiais",
                                "is_included": True},
                            {"title": "Inclui todas opções DFe-2000", "is_included": True},
                        ],
                        # col={'xs': 12, 'lg': 6},
                        col=12,
                    ),
                ],
            )
        )

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
                    image="images/tms_lp-01.webp",
                    image_left=True,
                ).build(),
                MainContentItem(
                    title="Emita CTe 4.0 com Facilidade",
                    description="Simplifique a emissão do CT-e 4.0 diretamente no TMS.CLOUD. Garanta conformidade com a legislação, reduza erros e ganhe agilidade no transporte de carga. Tudo integrado e automatizado para otimizar suas operações.",
                    image="images/tms_lp-02.png",
                    image_left=False
                ).build(),
                MainContentItem(
                    title="Gerencie seus MDFe",
                    description="Emita e gerencie MDF-e de forma rápida e segura. O TMS.CLOUD facilita o controle de cargas em trânsito, centraliza informações e garante a conformidade com a legislação fiscal. Otimize suas rotas e operações.",
                    image="images/tms_lp-03.webp",
                    image_left=True
                ).build(),
                MainContentItem(
                    title="Controle Total do Faturamento dos CT-es Emitidos",
                    description="Gere e acompanhe o faturamento dos seus CT-es com o TMS.CLOUD. Tenha relatórios precisos, automatize cobranças e otimize a gestão financeira da sua empresa. Mais controle, menos burocracia.",
                    image="images/tms_lp-05.webp",
                    image_left=False
                ).build(),
                MainContentItem(
                    title="Certificado",
                    description="Assine documentos com certificado digital A1 e-CNPJ",
                    image="images/certificado-A1.webp",
                    image_size=150,
                    image_left=True,
                    url="https://certbr.gfsis.com.br/gestaofacil/loja/index?local=500&indicacao=779310&videoconferencia=sim&ocultarValidacao=sim",
                    tooltip="Link: Clique para mais informações",
                ).build(),
                prices,
                register_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        # Rodapé
        footer = ft.Container(
            content=ft.Row(
                expand=True,
                controls=[
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value="© 2024 Sistrom Sistemas Web. Todos os direitos reservados.",
                                    color=ft.colors.GREY_400,
                                    size=12,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Icon(
                                    name="images/logo_sistrom.png", size=14),
                            ],
                            tight=True,
                        ),
                        url="https://sistrom.com.br/site/#sistemas",
                        tooltip="Clique aqui para acessar o site",
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
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
