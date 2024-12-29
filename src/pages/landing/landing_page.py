import math
import flet as ft
from typing import List, Dict, Union

from src.pages.landing.landing_itens import MainContentItem


class PriceItem(ft.UserControl):
    def __init__(self, plano: str, price: int, items_included: List[Dict[str, Union[str, bool]]], col: Dict):
        super().__init__()
        self.plano = plano
        self.price = price
        self.items_included = items_included
        self.col = col

    def create_item_row(self, item):
        return ft.Row(
            controls=[
                ft.Icon(
                    name=ft.icons.CHECK if item['is_included'] else ft.icons.CLOSE,
                    color=ft.colors.AMBER if item['is_included'] else ft.colors.RED,
                ),
                ft.Text(
                    value=item['title'],
                    theme_style=ft.TextThemeStyle.BODY_MEDIUM
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def build(self):
        price_text = f' {self.price} ' if self.price > 0 else "CONSULTE"
        pormes_text = '/mês' if self.price > 0 else "-NOS"
        btn_plano = 'QUERO ESTE' if self.price > 0 else "CONSULTAR"

        # Criar lista de linhas de itens incluídos
        items_rows = [self.create_item_row(item)
                      for item in self.items_included]

        content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            controls=[
                ft.Text(
                    value=self.plano,
                    theme_style=ft.TextThemeStyle.LABEL_LARGE
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            text='R$',
                            style=ft.TextStyle(color=ft.colors.WHITE)
                        ),
                        ft.TextSpan(
                            text=price_text,
                            style=ft.TextStyle(
                                color=ft.colors.AMBER, weight=ft.FontWeight.BOLD, size=50)
                        ),
                        ft.TextSpan(
                            text=pormes_text,
                            style=ft.TextStyle(color=ft.colors.WHITE)
                        ),
                    ]
                ),
                ft.Column(
                    controls=items_rows,
                    spacing=10,
                ),
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                value=btn_plano,
                                theme_style=ft.TextThemeStyle.BODY_LARGE,
                                color=ft.colors.WHITE
                            ),
                            ft.Icon(
                                name=ft.icons.ARROW_FORWARD_IOS,
                                size=14,
                                color=ft.colors.WHITE
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    on_click=lambda _: self.page.go(f'/signup/{self.plano}')
                )
            ]
        )

        return ft.Container(
            bgcolor=ft.colors.BLUE_GREY_800,
            padding=ft.padding.symmetric(vertical=20, horizontal=50),
            col=self.col,
            border_radius=10,
            expand=True,
            content=content
        )


class PriceItemPopular(PriceItem):
    def build(self):
        price_container = super().build()

        return ft.Stack(
            controls=[
                price_container,
                ft.Container(
                    bgcolor=ft.colors.AMBER,
                    content=ft.Text(
                        value='Popular',
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.BOLD
                    ),
                    padding=ft.padding.symmetric(vertical=5, horizontal=40),
                    right=-40,
                    top=10,
                    rotate=math.radians(40),
                )
            ]
        )


def LandingPage(page: ft.Page):
    title_bar = ft.Text(
        value="TMS.CLOUD  Gerenciamento de Transporte e logística",
        color=ft.colors.WHITE,
        font_family=ft.FontWeight.BOLD,
    )

    def update_text_size():
        # Ajusta o tamanho do texto com base na largura da tela
        width = page.width
        size = 20

        title_bar.value = "TMS.CLOUD  Gerenciamento de Transporte e logística"
        title_bar.size = size

        action_buttons.clear()
        action_buttons.extend([
            ft.TextButton(
                content=ft.Text(value="Inscrever-se", size=16),
                style=ft.ButtonStyle(color=ft.colors.WHITE),
                on_click=lambda _: page.go('/signup/DFe-1000'),
            ),
            ft.TextButton(
                content=ft.Text(value="Login", size=16),
                style=ft.ButtonStyle(color=ft.colors.WHITE),
                on_click=lambda _: page.go('/login'),
            ),
        ])

        if width < 600:         # xs
            size = 14
            # title_bar.size = 14
            title_bar.max_lines = 2

            if width < 576:
                # title_bar.size = 12
                size = 12
                if width < 545:
                    title_bar.value = "TMS.CLOUD" if width >= 435 else "TMS"
                    if width < 385:
                        # Exclui o botão "Inscrever-se" da posição 0 da List action_buttons
                        action_buttons.pop(0)
        elif width < 900:       # sm
            size = 14
        elif width < 1200:      # md
            size = 16
        elif width < 1500:      # lg
            size = 20
        else:                   # xl
            size = 22

        # Controla o tamanho do fonte no título da barra de ações (Menu Principal)
        title_bar.size = size

        # Controla o tamanho do fonte nos botões da barra de ação (Menu Principal) com tamanho máximo de 16
        btn_size = size if size < 17 else 16
        btn_increver = action_buttons[0]
        btn_increver.content = ft.Text(value="Inscrever-se", size=btn_size)

        btn_login = action_buttons[1]
        btn_login.content = ft.Text(value="Login", size=btn_size)

        page.update()

    action_buttons = [
        ft.TextButton(
            content=ft.Text(value="Inscrever-se", size=16),
            style=ft.ButtonStyle(color=ft.colors.WHITE),
            on_click=lambda _: page.go('/signup/DFe-1000'),
        ),
        ft.TextButton(
            content=ft.Text(value="Login", size=16),
            style=ft.ButtonStyle(color=ft.colors.WHITE),
            on_click=lambda _: page.go('/login'),
        ),
    ]

    page.appbar = ft.AppBar(
        leading=ft.Image(
            src='images/tms_cloud_1024x724.png',
            tooltip="TMS.CLOUD | Sistrom Web",
        ),
        leading_width=120,
        title=title_bar,
        center_title=False,
        bgcolor=ft.colors.BLUE_GREY_800,
        actions=action_buttons,
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

    prices = ft.Container(
        padding=20,
        # bgcolor=ft.colors.BLUE_GREY_800,
        border_radius=10,
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
                        {"title": "Armazenamento ilimitado",
                            "is_included": False},
                        {"title": "Usuários ilimitados", "is_included": False},
                        {"title": "Emissão de CTe 4.0", "is_included": True},
                        {"title": "Emissão de MDFe", "is_included": True},
                        {"title": "Por emitente (CNPJ)",
                            "is_included": True},
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
                        {"title": "Armazenamento ilimitado",
                            "is_included": False},
                        {"title": "Usuários ilimitados", "is_included": False},
                        {"title": "Emissão de CTe 4.0", "is_included": True},
                        {"title": "Emissão de MDFe", "is_included": True},
                        {"title": "Por emitente (CNPJ)",
                            "is_included": True},
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
                        {"title": "Armazenamento ilimitado",
                            "is_included": False},
                        {"title": "Usuários ilimitados", "is_included": False},
                        {"title": "Emissão de CTe 4.0", "is_included": True},
                        {"title": "Emissão de MDFe", "is_included": True},
                        {"title": "Por emitente (CNPJ)",
                            "is_included": True},
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
                        {"title": "Armazenamento ilimitado",
                            "is_included": False},
                        {"title": "Usuários ilimitados", "is_included": False},
                        {"title": "Emissão de CTe 4.0", "is_included": True},
                        {"title": "Emissão de MDFe", "is_included": True},
                        {"title": "Por emitente (CNPJ)",
                            "is_included": True},
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
                        {"title": "Armazenamento ilimitado",
                            "is_included": True},
                        {"title": "Usuários ilimitados", "is_included": True},
                        {"title": "Emissão de CTe 4.0", "is_included": True},
                        {"title": "Emissão de MDFe", "is_included": True},
                        {"title": "Por emitente (CNPJ)",
                            "is_included": True},
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
                        {"title": "Armazenamento ilimitado",
                            "is_included": True},
                        {"title": "Usuários ilimitados", "is_included": True},
                        {"title": "Emissão de CTe 4.0", "is_included": True},
                        {"title": "Emissão de MDFe", "is_included": True},
                        {"title": "Por emitente (CNPJ)",
                            "is_included": True},
                    ],
                    col={'xs': 12, 'lg': 4},
                ),
                PriceItem(
                    plano='DFe-PLUS',
                    price=0,
                    items_included=[
                        {"title": "Acima de 2000 Emissões/mês",
                            "is_included": True},
                        {"title": "Consulte para preços especiais",
                            "is_included": True},
                        {"title": "Inclui todas opções DFe-2000",
                            "is_included": True},
                    ],
                    # col={'xs': 12, 'lg': 6},
                    col=12,
                ),
            ],
        )
    )

    register_button = ft.ElevatedButton(
        "Registre-se Agora",
        bgcolor=ft.colors.AMBER_500,
        color=ft.colors.WHITE,
        on_click=lambda _: page.go('/signup/DFe-1000'),
    )

    def section_title(title: str):
        return ft.Container(
            margin=ft.margin.only(top=40),
            padding=ft.padding.symmetric(vertical=20),
            content=ft.Text(
                value=title, theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        )

    main_content = ft.Column(
        controls=[
            title,
            subtitle,
            section_title(title="Gestão de Transporte"),
            MainContentItem(
                title="Transforme sua Gestão de Transporte com TMS.CLOUD",
                description="O TMS.CLOUD é a solução completa para o gerenciamento de transporte e logística. Automatize processos, controle suas operações em tempo real e reduza custos com uma plataforma intuitiva e eficiente. Leve a gestão do seu transporte de cargas para o próximo nível.",
                image="images/tms_lp_1.webp",
                image_left=True,
            ),
            section_title(title="CTe 4.0"),
            MainContentItem(
                title="Emita CTe 4.0 com Facilidade",
                description="Simplifique a emissão do CT-e 4.0 diretamente no TMS.CLOUD. Garanta conformidade com a legislação, reduza erros e ganhe agilidade no transporte de carga. Tudo integrado e automatizado para otimizar suas operações.",
                image="images/tms_lp_2.png",
                image_left=False
            ),
            section_title(title="MDFe"),
            MainContentItem(
                title="Gerencie seus MDFe",
                description="Emita e gerencie MDF-e de forma rápida e segura. O TMS.CLOUD facilita o controle de cargas em trânsito, centraliza informações e garante a conformidade com a legislação fiscal. Otimize suas rotas e operações.",
                image="images/tms_lp_3.webp",
                image_left=True
            ),
            section_title(title="Faturamento"),
            MainContentItem(
                title="Controle Total do Faturamento dos CT-es Emitidos",
                description="Gere e acompanhe o faturamento dos seus CT-es com o TMS.CLOUD. Tenha relatórios precisos, automatize cobranças e otimize a gestão financeira da sua empresa. Mais controle, menos burocracia.",
                image="images/tms_lp_4.webp",
                image_left=False
            ),
            section_title(title="Certificado Digital"),
            MainContentItem(
                title="Certificado",
                description="Assine documentos com certificado digital A1 e-CNPJ",
                image="images/certificado-A1.webp",
                image_left=True,
                image_size=150,
                url="https://certbr.gfsis.com.br/gestaofacil/loja/index?local=500&indicacao=779310&videoconferencia=sim&ocultarValidacao=sim",
                tooltip="Link: Clique para mais informações",
            ),
            section_title(title="Preços"),
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

    page.on_resized = lambda _: update_text_size()
    update_text_size()

    lp_main_content = ft.Container(
        content=main_content,
        width=1400,
        expand=True,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLUE_GREY_900,
        padding=20,
    )

    lp_footer = ft.Container(
        content=footer,
        # width=1400,
        alignment=ft.alignment.center,
    )

    main_container = ft.Container(
        content=ft.Column(
            controls=[
                lp_main_content,
                lp_footer
            ],
            spacing=0,
            alignment=ft.alignment.center,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        bgcolor=ft.colors.BLUE_GREY_900,
        height=page.height,
        alignment=ft.alignment.center,
    )

    return main_container
